from flask import request
from flask_restx import Namespace, Resource

namespace = Namespace("albums")

class Albums(Resource):
    def get(self):
        """get all albums"""
        # TODO: get all albums from database
        response = {"message":"Not yet implemented..."}
        return response, 200
    
namespace.add_resource(Albums, "")