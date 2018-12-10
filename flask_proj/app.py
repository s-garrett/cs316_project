from flask import Flask, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import models
import forms

app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)

@app.route("/")
def all_athletes():
    athletes = db.session.query(models.athlete)
    return render_template('all-athletes.html', athletes=athletes)

@app.route('/athlete/<name>')
def athlete(name):
    athlete = db.session.query(models.athlete)\
        .filter(models.athlete.athlete_name == name)
    return render_template('athlete.html', athlete=athlete)



@app.template_filter('pluralize')
def pluralize(number, singular='', plural='s'):
   return singular if number in (0, 1) else plural

if __name__ == '__main__':
    app.config['DEBUG'] = True
    app.run(host='0.0.0.0', port=5000)
