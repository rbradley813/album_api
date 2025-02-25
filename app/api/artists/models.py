from app import db

class Artist(db.Model):
    __tablename__ = "artist"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(256), nullable=False)

    def __init__(self, name=""):
        self.name = name