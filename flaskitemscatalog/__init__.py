
from flask import Flask

# basic configurations
app = Flask(__name__)

from flaskitemscatalog import routes

# make this _init