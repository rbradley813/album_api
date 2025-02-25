from flask_restx import reqparse

parser_album_post = reqparse.RequestParser()
parser_album_post.add_argument("name", required=True)