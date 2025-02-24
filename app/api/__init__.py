from flask_restx import Api

from app.api.ping.views import namespace as ping

api = Api(
    version="1.0",
    title="Music Catalog API",
    prefix="/api/v1",
    doc="/api/v1/docs"
)

api.add_namespace(ping)
