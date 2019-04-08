import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_restful import Resource, Api
from flask_login import LoginManager

app = Flask(__name__)

app.config['SECRET_KEY'] = 'mysecretkey'


############################
###       db setup       ###
############################

basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+os.path.join(basedir,'data.sqlite')
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] =False


db =SQLAlchemy(app)
Migrate(app,db)


############################
###  Blueprint Register  ###
############################
login_manager= LoginManager()

login_manager.init_app(app)
login_manager.login_view = 'my_views.login'

from BYY.my_views.views import my_views
from BYY.public_view.views import public_view

app.register_blueprint(my_views)
app.register_blueprint(public_view)
