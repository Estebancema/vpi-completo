import sqlite3
from flask import Blueprint, render_template, request,flash, redirect,url_for,jsonify


datos = Blueprint('datos',__name__)

@datos.route('/clientes',methods=['GET'])
def clientes():
    conexion = sqlite3.connect('database.db')
    cursor = conexion.cursor()
    sentenciaSQL = cursor.execute('SELECT name,email FROM user')
    todos_clientes = cursor.fetchall()
    list = []
    for x in todos_clientes:
        list.append(x)
    return jsonify(list)

@datos.route('/viajes',methods=['GET'])
def viajes():
    conexion = sqlite3.connect('database.db')
    cursor = conexion.cursor()
    sentenciaSQL = cursor.execute('SELECT * FROM avion')
    todos_viajes = cursor.fetchall()
    viajes = []
    for x in viajes:
        viajes.append(x)
    return jsonify(viajes)

@datos.route('/pagos',methods=['GET'])
def pagos():
    conexion = sqlite3.connect('database.db')
    cursor = conexion.cursor()
    sentenciaSQL = cursor.execute('SELECT * FROM pagos')
    todos_pagos = cursor.fetchall()
    pagos = []
    for x in pagos:
        pagos.append(x)
    return jsonify(pagos)
