from flask.sessions import NullSession
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
        self.role=1
    def get_id(self):
        return self.id
    def get_role(self):
        return int.from_bytes(self.role,byteorder='big')
class Solicitudes(db.Model):
    __tablename__ = 'Solicitudes'
    id = db.Column(db.Integer, primary_key=True)
    idUser = db.Column(db.Integer, unique=True)
    solicitud = db.Column(db.String(255))
    nombre = db.Column(db.String(16))
    programa = db.Column(db.String(255))
    justificacion = db.Column(db.Text(255))
    respuesta = db.Column(db.Text(255), nullable=True)
    def __init__(self, idUser, solicitud, nombre, programa, justificacion):
            self.idUser=idUser
            self.solicitud=solicitud
            self.nombre =nombre
            self.programa = programa
            self.justificacion = justificacion

