from website import db
from flask_login import UserMixin


class Avion(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    modelo = db.Column(db.String(150))
    tripulacion = db.Column(db.Integer)
    pilotos = db.Column(db.Integer)
    azafatas = db.Column(db.Integer)
    equipaje = db.Column(db.Integer)
    precio = db.Column(db.Integer)
    hacia = db.Column(db.String(150))
    desde = db.Column(db.String(150))
    fecha = db.Column(db.String)
    '''

    owner_id = db.Column(db.Integer,db.ForeignKey('owner.id'))

    '''


class Owner(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    name = db.Column(db.String(150))
    '''
    aviones = db.relationship('Avion')
    '''


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    name = db.Column(db.String(150))

class Pagos(db.Model):
    id = db.Column(db.Integer,primary_key = True)
    email = db.Column(db.String(150),unique = True)
    nombre = db.Column(db.String(150))
    tarjeta = db.Column(db.String(150))
    nro_tarjeta = db.Column(db.Integer)
    codigo_seguridad = db.Column(db.Integer)



