from sqlalchemy import sql, orm
from app import db

class athlete(db.Model):
    TABLE_NAME = 'Athlete'
    athlete_name = db.Column('athletename', db.String(20), primary_key=True)
    school_name = db.Column('schoolname', db.String(20), primary_key=True)
    gender = db.Column('gender', db.String(20))
    best_mark = db.Column('bestmark', db.Integer)
    event = db.Column('event', db.String(20), primary_key=True)
