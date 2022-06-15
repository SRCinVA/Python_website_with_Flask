from flask import Flask
from flask_sqlalchemy import SQLAlchemy

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

    return app
