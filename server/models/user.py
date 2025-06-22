from . import db
class User (db.Model):
    __tablename__ = 'users'

    id=db.Column(db.Integer)
    username= db.Column(db.String, unique= True)
    #password_hash=