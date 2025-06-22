from . import db

class Guest (db.Model):
    __tablename__ = 'guests'

    id = db.Column(db.Integer)
    name = db.Column(db.String, nullable = False)
    occupation =db.Column(db.String, nullable = False)