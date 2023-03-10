from flask import Flask
from os.path import join, dirname, realpath

app = Flask(__name__)

app.config['SECRET_KEY'] = '598849722efc0faeb634444805fec10e'
app.config['UPLOAD_FOLDER'] = join(dirname(realpath(__file__)), 'static/')
from app import routes
