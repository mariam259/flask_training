from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func
from datetime import datetime

# define our schema for database
# we have database model for users and for notes


# Note table
class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(10000))
    # func.now save the created date for the note
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    # user_id is a forigen key from User table (one to many relation)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))


# create User object (table)
class User(db.Model, UserMixin):
    # define columns in user table
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), nullable=True, unique=True)
    password = db.Column(db.String(150), nullable=True)
    first_name = db.Column(db.String(150))
    # create one to many relation with Note
    notes = db.relationship('Note')
