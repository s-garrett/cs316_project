from sqlalchemy import sql, orm
from app import db

class athlete(db.Model):
    TABLE_NAME = 'athlete'
    athlete_name = db.Column('athletename', db.String(20), primary_key=True)
    school_name = db.Column('schoolname', db.String(20), primary_key=True)
    gender = db.Column('gender', db.String(20))
    best_mark = db.Column('bestmark', db.Integer)
    event = db.Column('event', db.String(20), primary_key=True)

class athletecompetein(db.Model):
    TABLE_NAME = 'athletecompetein'
    athlete_name = db.Column('athletename', db.String(20), primary_key=True)
    school_name = db.Column('schoolname', db.String(20), primary_key=True)
    #event_name = db.Column('event', db.String(20), primary_key=True)
    round = db.Column('round', db.String(20), primary_key=True)
    gender = db.Column('gender', db.String(20), primary_key=True)
    meet_name = db.Column('meetname', db.String(20), primary_key=True)
    #meet_date = db.Column('meet_date', db.String(20), primary_key=True)
    sport = db.Column('sport', db.String(20))
    place = db.Column('place', db.Integer)
    mark = db.Column('mark', db.Float)
    year = db.Column('year', db.Integer)
