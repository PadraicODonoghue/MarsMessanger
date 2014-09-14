from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.bootstrap import Bootstrap
from flask.ext.moment import Moment

app = Flask(__name__, instance_relative_config=True)

# Now we can access the configuration variables via app.config["VAR_NAME"]
app.config.from_object('config')

# Init database system
db = SQLAlchemy(app)

bootstrap = Bootstrap(app)
moment = Moment(app)

from app import views, models
