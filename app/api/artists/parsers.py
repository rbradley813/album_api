from flask_restx import reqparse

parser_artist_post = reqparse.RequestParser()
parser_artist_post.add_argument("name", required=True)