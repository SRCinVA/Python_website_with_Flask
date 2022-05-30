from flask import Flask

def create_app(): # this initializes the app
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'MySecretKey'  # for encrypting session data, etc.

    # here's where we register our Blueprints, to tell flask what's going on.
    # that means we need to start to import them ...

    from .views import views
    from .auth import auth

    # in both of these cases, a slash means "no prefix":
    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    return app
