# this file is making our website folder treated as python package

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager

# create our database object which will be used to handle database staff
db = SQLAlchemy()
DB_NAME = " database.db"


def create_app():
    # first we initialize our app
    app = Flask(__name__)

    # then we secure our cookies data by using config secret key
    app.config['SECRET_KEY'] = 'secret key'

    # store our database at this location 'sqlite:///{DB_NAME}'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    # intialize our database
    # db = SQLAlchemy(app)

    db.init_app(app)

    from .views import views
    from .auth import auth
    # register our blueprint for different views for the app
    # this prefix will load all the views in the specified file
    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    from .models import User, Note
    with app.app_context():
        db.create_all()

    # after we create database we handle user state(login)
    login_manager = LoginManager()
    # user should go to login page if it's not logged in
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):  # return the user that match this id or None if user doesn't exist
        return User.query.get(int(id))

    return app


# function to check if we create database don't override it else create it
# def create_database(app):
#     if not path.exists('website/' + DB_NAME):
#         with app.app_context():
#             db.create_all()
#             print('Created Database!')
