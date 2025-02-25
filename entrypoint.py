from app import db, startup_app
from app.api.albums.models import Album

app = startup_app()

with app.app_context():
    db.drop_all()
    db.create_all()
    db.session.commit()