from app import db

class Album(db.Model):
    __tablename__ = "albums"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    artist_id = db.Column(db.Integer, nullable=False)
    name = db.Column(db.String(256), nullable=False)
    release_date = db.Column(db.String(256), nullable=False)
    price = db.Column(db.Float, nullable=False)

    def __init__(self, artist_id=0, name="", release_date="", price=0.0):
        self.artist_id = artist_id
        self.name = name
        self.release_date = release_date
        self.price = price