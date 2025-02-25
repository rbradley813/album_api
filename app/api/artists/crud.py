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

def get_artist_by_name(artist_name) -> Artist:
    """return artist by name"""
    artist = None
    try:
        artist = Artist.query.filter_by(name=artist_name).first()
    except Exception as ex:
        # TODO: implement error handling / logging
        pass
    return artist

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