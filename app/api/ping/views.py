from flask_restx import Namespace, Resource

namespace = Namespace("ping")

class Ping(Resource):
    def get(self):
        """health check"""
        return {"message":"pong!"}, 200

namespace.add_resource(Ping, "")