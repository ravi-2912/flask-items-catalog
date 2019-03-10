
from flask import Flask

# basic configurations
app = Flask(__name__)

from flaskitemscatalog import routes

if __name__ == "__main__":
    # debug mode
    # app.debug = True
    app.run()