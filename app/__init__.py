from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from app.api import api

db = SQLAlchemy()

from app.api.albums.models import Album

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///temp.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
api.init_app(app)

with app.app_context():
    db.drop_all()
    db.create_all()
    db.session.commit()