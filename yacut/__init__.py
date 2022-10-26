from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from settings import Config


app: Flask = Flask(__name__)
app.config.from_object(Config)

db: SQLAlchemy = SQLAlchemy(app)
migrate: Migrate = Migrate(app, db)

from . import api_views, constants, error_handlers, views
