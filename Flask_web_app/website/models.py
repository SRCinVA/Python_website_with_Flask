from time import timezone
from . import db  # here the dot refers to the overall package. Form outside the directory it would be 'website'
from flask_login import UserMixin
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func

class Note(db.Model):  # this is a "much more general class" (not sure what he means by that ...)
    id = db.Column(db.Integer, primary_key=True)  # all notes will need a unique id (db software is smart enough to increment these by one)
    data = db.Column(db.String(10000))
    date = db.Column(db.DateTime(timezone=True), default=func.now) # func.now just pulls out the current date and time
    user_id = db.column(db.Integer, db.ForeignKey('user.id')) # he's doing this to set up the user_id as a foreign key for the notes 
                                                                # we will have to pas an exiting, valid ID in this field to create a note object
                                                                # "user" refers to each instance of the class below, while ".id" is that attribute attached to it.
                                                                # for Foreign Keys, it's lower case

# class Reminder(db.Model):
#    pass

class User(db.Model, UserMixin):  # below is the schema for storing all of our users
    id = db.Column(db.Integer, primary_key=True)  # we need a primary key
    email = db.Column(db.String(150), unique=True) # here we're populating the column with the data type for each item (150 char. max.)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
    notes = db.relationship('Note')  # this is a field that establishes a relationship between the db and the Note table 
                                    # 'notes' will be just another attribute attached to the User object
                                    # for relationships, it's upper case (a strange inconsistency.)
