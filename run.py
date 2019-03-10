#!/usr/bin/python
import sys
import logging
logging.basicConfig(stream=sys.stderr)
sys.path.insert(0,"/var/www/flaskitemscatalog/")

from flaskitemscatalog import app
# super secure key for flash messaging
app.secret_key = "super secret key"
