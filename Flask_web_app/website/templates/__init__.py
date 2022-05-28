from flask import Flask

def create_app(): # this initializes the app
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'MySecretKey'  # for encrypting session data, etc.

    return app