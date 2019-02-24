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
from flask_talisman import Talisman
from flask_seasurf import SeaSurf

# connect flask to database, these tell flask where to look for files
# template folder define html path(relative to this script)
# static folder define file path(relative to this script)
# static url path define the url path
app = Flask(__name__,template_folder='build',static_url_path='/static',static_folder='build/static')

# create gzip instances
compress = Compress(app)
# create cors instance
cors = cors = CORS(app, resources={r"/api/*": {"origins": "https://flask.tylim.com/"}})
# create cache instance
cache = Cache(app,config={'CACHE_TYPE': 'simple'})
# create secure header instances
csp = {
    'default-src': ['\'self\''],
    'style-src':['\'self\'','https://*.bootstrapcdn.com','\'unsafe-inline\''],
    'font-src': ['\'self\'','data:'],
    'script-src':['\'self\'',
    '\'unsafe-inline\'']# https://stackoverflow.com/questions/45366744/refused-to-load-the-font-datafont-woff-it-violates-the-following-content/50504870
}
talisman = Talisman(app, content_security_policy=csp)

# create seasurf instances
csrf = SeaSurf(app)

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