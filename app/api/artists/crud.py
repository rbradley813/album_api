from typing import List
from app import db
from app.api.artists.models import Artist

def get_all_artists() -> List[Artist]:
    """returns all artists"""

    artists = None
    try:
        artists = Artist.query.all()
    except Exception as ex:
        # TODO: implement error handling / logging
        pass
    return artists

def create_artist(name:str) -> Artist:
    """creates an artist"""
    artist = None
    try:
        artist = Artist(name=name)
        db.session.add(artist)
        db.session.commit()
    except Exception as ex:
        # TODO: implement error handling / logging
        pass
    return artist