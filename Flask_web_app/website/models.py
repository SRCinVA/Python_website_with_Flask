from time import timezone
from . import db  # here the dot refers to the overall package. Form outside the directory it would be 'website'
from flask_login import UserMixin
from sqlalchemy.sql import func

class Note(db.Model):  # this is a "much more general class" (not sure what he means by that ...)
    id = db.Column(db.Integer, primary_key=True)  # all notes will need a unique id (db software is smart enough to increment these by one)
    data = db.Column(db.String(10000))
    date = db.Column(db.DateTime(timezone=True), default=)

class User(db.Model, UserMixin):  # below is the schema for storing all of our users
    id = db.Column(db.Integer, primary_key=True)  # we need a primary key
    email = db.Column(db.String(150), unique=True) # here we're populating the column with the data type for each item (150 char. max.)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))

