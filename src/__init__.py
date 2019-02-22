import os
from os import environ
from flask import Flask 
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_restful import Api
from flask_jwt_extended import JWTManager
from flask_cors import CORS
from flask_compress import Compress
from flask_caching import Cache

# connect flask to database, these tell flask where to look for files
# template folder define html path(relative to this script)
# static folder define file path(relative to this script)
# static url path define the url path
app = Flask(__name__,template_folder='build',static_url_path='/static',static_folder='build/static')

# create gzip instances
compress = Compress(app)
# create cors instance
CORS(app)
# create cache instance
cache = Cache(app,config={'CACHE_TYPE': 'simple'})

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