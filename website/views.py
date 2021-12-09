from flask import Blueprint, render_template, request,flash, redirect,url_for,jsonify
from sqlite3.dbapi2 import Timestamp
import sqlite3
from flask_login import login_user, login_required, logout_user, current_user


views = Blueprint('views',__name__)

@views.route('/')
def home():
    conexion = sqlite3.connect('database.db')
    cursor = conexion.cursor()
    sentenciaSQL = cursor.execute("SELECT modelo,precio,hacia,desde,fecha,equipaje FROM avion")
    tabla = cursor.fetchall()
    headings = ['modelo','precio','Destino','Salida','fecha','equipaje','pago']
    tabla = tabla
    return render_template("VPI.html",headings=headings,tabla=tabla,user=current_user)


'''
'''