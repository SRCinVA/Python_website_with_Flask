from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path  # this will help us determine if hte path the DB exists.

db = SQLAlchemy() # this initializes the DB as an object
DB_NAME = "database.db"  # (obviously) this is the name.

def create_app(): # this initializes the app
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'MySecretKey'  # for encrypting session data, etc.
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}' # this will store the DB in the website folder

    # here's where we register our Blueprints, to tell flask what's going on.
    # that means we need to start to import them ...

    # here, we're going to initialize our database by giving it our Flask app.
    db.init_app(app)  # we're telling db (up top) that this is the app we'll be using it in.

    from .views import views
    from .auth import auth

    # in both of these cases, a slash means "no prefix":
    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    from .models import User, Note # we do this to make sure that these files run before we create the DB (makes sense)

    create_database(app)

    return app

def create_database(app):  # this will check to see if the DB exists. If it doesn't, it will create one. If it does, it won't overwrite it.
    if not path.exists("website/" + DB_NAME):
        db.create_all(app = app)  # actually creates the db (if it doesn't exist)
        print("Created database!")