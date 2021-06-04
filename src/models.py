from flask_login import UserMixin
from . import db
class User(UserMixin, db.Model):
        __tablename__ = 'user'
        id = db.Column(db.Integer, primary_key=True)
        user = db.Column(db.String(255), unique=True)
        password = db.Column(db.String(16))
        role=db.Column(db.Integer)
        def __init__(self, user, password):
            self.user=user
            self.password=password
        def get_id(self):
            return self.id
        def get_role(self):
            return int.from_bytes(self.role,byteorder='big')
        

