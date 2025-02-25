from flask import request
from flask_restx import Namespace, Resource, fields

from app.api.artists.crud import (get_all_artists, create_artist)
from app.api.artists.parsers import parser_artist_post

namespace = Namespace("artists")
artist = namespace.model(
    "artist",
    {
        "id": fields.Integer(readOnly=True),
        "name": fields.String(required=True)
    },
)

class Artists(Resource):
    @namespace.marshal_with(artist, as_list=True)
    def get(self):
        """get all artists"""
        artists = get_all_artists()
        # TODO: API Error Handling
        return artists, 200
    
    @namespace.expect(parser_artist_post, validate=True)
    @namespace.marshal_with(artist)
    def post(self):
        """create a new artist"""
        args = parser_artist_post.parse_args()
        # TODO: API Error Handling
        return create_artist(args["name"]), 201
    
namespace.add_resource(Artists, "")