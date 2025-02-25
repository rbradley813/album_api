from flask_restx import reqparse

parser_album_post = reqparse.RequestParser()
parser_album_post.add_argument("artist_name", required=True)
parser_album_post.add_argument("name", required=True)
parser_album_post.add_argument("release_date", required=True)
parser_album_post.add_argument("price", required=True)