from flask import request
from flask_restx import Namespace, Resource, fields

from app.api.albums.crud import (get_all_albums, create_album)
from app.api.albums.parsers import parser_album_post

namespace = Namespace("albums")
album = namespace.model(
    "Album",
    {
        "id": fields.Integer(readOnly=True),
        "name": fields.String(required=True)
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
        # TODO: API Error Handling
        return create_album(args["name"]), 201
    
namespace.add_resource(Albums, "")