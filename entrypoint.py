from app import db, startup_app
from app.api.albums.models import Album
from app.api.artists.models import Artist

app = startup_app()

with app.app_context():
    db.drop_all()
    db.create_all()
    db.session.commit()
    init_artist = Artist("init")
    db.session.add(init_artist)
    db.session.commit()
    init_album = Album("init")
    db.session.add(init_album)
    db.session.commit()
    db.drop_all()
    db.create_all()
    db.session.commit()
