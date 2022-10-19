from openroad import db
from flask_login import UserMixin
from sqlalchemy.sql import func


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(50))
    first_name = db.Column(db.String(50))
    notes = db.relationship('Triproute')

    def __repr__(self):
        # __repr__ to represent itself in the form of a string
        return self.id

class Triproute(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(5000))
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        # __repr__ to represent itself in the form of a string
        return self.id, self.data, self.date
    
