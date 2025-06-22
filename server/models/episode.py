from . import db

class Episode (db.Model):
    __tablename__ = 'episodes'

    id = db.Column(db.Integer)
    date = db.Column(db.Date)
    number = db.Column(db.Integer, nullable = False)

    #cascade thing