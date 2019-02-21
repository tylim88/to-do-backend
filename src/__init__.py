import os, logging
from os import environ
from flask import Flask 
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_restful import Api
from flask_jwt_extended import JWTManager
from flask_cors import CORS

# connect flask to database, these tell flask where to look for files
app = Flask(__name__, static_folder='src/templates/static')
# create cors instance
CORS(app)
# read configuration from file
app.config.from_object(environ.get('ENV_PATH'))

# get file + directory + absolute path name
basedir = os.path.abspath(os.path.dirname(__file__))

# dynamically configuration database URI
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + \
    os.path.join(basedir, 'data.sqlite')

# create database instance
db = SQLAlchemy(app)
# create migration instance
migrate = Migrate(app, db)
# create api instance
aPi = Api(app)
# create jwt instance
jwt = JWTManager(app)

# from folder/package/module import module/function
from src import models, routes, api
logging.getLogger('flask_cors').level = logging.DEBUG