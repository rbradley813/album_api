from typing import List
from app import db
from app.api.albums.models import Album

def get_all_albums() -> List[Album]:
    """returns all albums"""

    albums = None
    try:
        albums = Album.query.all()
    except Exception as ex:
        # TODO: implement error handling / logging
        pass
    return albums

def create_album(artist_id:int, name:str, release_date:str, price:float) -> Album:
    """creates an album"""
    album = None
    try:
        album = Album(artist_id=artist_id, name=name, release_date=release_date, price=price)
        db.session.add(album)
        db.session.commit()
    except Exception as ex:
        # TODO: implement error handling / logging
        pass
    return album