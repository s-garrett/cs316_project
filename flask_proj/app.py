from flask import Flask, render_template, redirect, url_for, send_from_directory
from flask_sqlalchemy import SQLAlchemy
import models
import forms

app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)

@app.route('/js/<path:path>')
def send_js(path):
    return app.send_static_file('js/'+ path)

@app.route('/css/<path:path>')
def send_css(path):
    return app.send_static_file('css/'+ path)

@app.route('/images/<path:path>')
def send_image(path):
	return app.send_static_file('img/'+ path)


@app.route('/')
def home():
	return render_template('index.html')
	

@app.route("/all-athletes")
def all_athletes():
    athletes = db.session.query(models.athlete)
    meets = db.session.query(models.athletecompetein)
    return render_template('all-athletes.html', meets=meets, athletes=athletes)

    
@app.route('/athlete/<name>')
def athlete(name):
    athlete = db.session.query(models.athlete)\
        .filter(models.athlete.athlete_name == name)
    return render_template('athlete.html', athlete=athlete)

@app.route('/teams')
def teams():
    teams = db.session.query(models.athletecompetein.school_name.distinct().label('team_name'))
    return render_template('teams.html', teams=teams)


@app.route('/teams/<name>')
def team(name):
    athletessq = db.session.query(models.athlete.athlete_name.label('athlete_name'), models.athlete.school_name)\
        .filter(models.athlete.school_name == name).subquery()
    distathletes=db.session.query(athletessq.c.athlete_name.distinct().label('athlete_name'))
    return render_template('team.html', athletes=distathletes, name=name)

@app.route('/hypothetical')
def hypothetical():
    rightschools=db.session.query(models.athlete.athlete_name.label('athlete_name'), models.athlete.school_name.label('school_name'), models.athlete.event.label('event'), models.athlete.best_mark.label('best_mark'), models.athlete.gender.label('gender')).filter(and_(or_(models.athlete.school_name=='Duke', models.athlete.school_name=='North Carolina') , models.athlete.gender=='M', models.athlete.event=='8K')).order_by(asc(models.athlete.best_mark)).subquery()
    sq1=db.session.query(rightschools.c.athlete_name.label('athlete_name'), rightschools.c.school_name.label('school_name'), rightschools.c.best_mark.label('mark'),  func.rank().over(order_by=rightschools.c.best_mark.asc(), partition_by=rightschools.c.school_name).label('tmsrnk')).subquery()
    sq2=db.session.query(func.row_number().over(order_by=sq1.c.mark).label('points'), sq1.c.tmsrnk, sq1.c.athlete_name.label('athlete_name'), sq1.c.school_name.label('school_name'), sq1.c.mark.label('mark')).filter(sq1.c.tmsrnk<8).order_by('mark').subquery()
    q2=db.session.query(func.row_number().over(order_by=sq1.c.mark).label('points'), sq1.c.tmsrnk, sq1.c.athlete_name.label('athlete_name'), sq1.c.school_name.label('school_name'), sq1.c.mark.label('mark')).filter(sq1.c.tmsrnk<8).order_by('mark')
    q3=db.session.query(sq2.c.school_name.label('school_name'), func.sum(sq2.c.points).label('points')).group_by(sq2.c.school_name)
    return render_template('hypo.html', hypo=q2, teams=q3)


@app.template_filter('pluralize')
def pluralize(number, singular='', plural='s'):
   return singular if number in (0, 1) else plural



if __name__ == '__main__':
    app.config['DEBUG'] = True
    app.run(host='0.0.0.0', port=5000)
