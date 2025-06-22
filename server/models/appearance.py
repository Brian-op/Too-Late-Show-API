from . import db

class Appearance(db.Model):
    __tablename__ = 'appearances'

    id = db.Column(db.Integer)
    rating = db.Column(db.Integer) 
    guest_id = db.Column(db.Integer, db.ForeignKey('guests.id'))
    episode_id = db.Column(db.Integer, db.ForeignKey('episodes.id'))
