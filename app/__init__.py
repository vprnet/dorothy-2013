from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.admin import Admin
from flask.ext.admin.contrib.sqla import ModelView

app = Flask(__name__)
app.config.from_object('config')
admin = Admin(app, name="Dorothy's List")
db = SQLAlchemy(app)

from app import views, models
