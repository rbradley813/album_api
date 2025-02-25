from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def startup_app():
    from app.api.albums.models import Album
    from app.api.artists.models import Artist

    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///temp.db"
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    from app.api import api
    api.init_app(app)
    return app