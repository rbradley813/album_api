from flask import request
from flask_restx import Namespace, Resource, fields

from app.api.albums.crud import (get_all_albums, create_album)
from app.api.albums.parsers import parser_album_post
from app.api.artists.crud import get_artist_by_name

namespace = Namespace("albums")
album = namespace.model(
    "Album",
    {
        "id": fields.Integer(readOnly=True),
        "artist_id": fields.Integer(required=True),
        "name": fields.String(required=True),
        "release_date": fields.String(required=True),
        "price": fields.Float(required=True)
    },
)

class Albums(Resource):
    @namespace.marshal_with(album, as_list=True)
    def get(self):
        """get all albums"""
        albums = get_all_albums()
        # TODO: API Error Handling
        return albums, 200
    
    @namespace.expect(parser_album_post, validate=True)
    @namespace.marshal_with(album)
    def post(self):
        """create a new album"""
        args = parser_album_post.parse_args()
        artist = get_artist_by_name(args["artist_name"])
        if artist is None:
            namespace.abort(404, "Artist not found. Cannot add album for non-existent Artist.")
        # TODO: Date Validation and Error Handling
        new_album = create_album(
            artist_id=artist.id,
            name=args["name"],
            release_date=args["release_date"],
            price=args["price"]
        )
        # TODO: API Error Handling
        return new_album, 201
    
namespace.add_resource(Albums, "")