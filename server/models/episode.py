from . import db

class Episode (db.Model):
    __tablename__ = 'episodes'

    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date)
    number = db.Column(db.Integer, nullable = False)

    def __repr__(self):
         return f"<Episode id={self.id} number={self.number} date={self.date}>"