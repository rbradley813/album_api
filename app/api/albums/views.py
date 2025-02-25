from flask import request
from flask_restx import Namespace, Resource, fields

from app.api.albums.crud import (get_all_albums)

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
    
namespace.add_resource(Albums, "")