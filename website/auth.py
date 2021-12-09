from flask import Blueprint, request, render_template, flash, redirect, url_for
from .models import User, Avion, Owner, Pagos
from website import db
from flask_login import login_user, login_required, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from tabla import email_user
import sqlite3

auth = Blueprint('auth', __name__)


@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('psw')

        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, password):
                flash('logeado!!', category='success')
                login_user(user, remember=True)
                return redirect('/')
            else:
                flash('Password incorrecta', category='error')
        else:
            flash('Email incorrecto', category='error')

    return render_template('login.html', user=current_user)


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))


@auth.route('/sign_up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        name = request.form.get('name')
        password = request.form.get('psw')
        password_2 = request.form.get('psw2')

        user = User.query.filter_by(email=email).first()
        if user:
            flash('email ya existe!!', category='error')
        elif len(email) < 4:
            flash('email tiene que ser mayor a 4 caracteres!', category='error')
        elif len(name) < 2:
            flash('nombre tiene que ser mayor a 2 caracteres!', category='error')
        elif password != password_2:
            flash('Las passwords no son iguales', category='error')
        else:
            new_user = User(email=email, password=generate_password_hash(password, method='sha256'), name=name)
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user, remember=True)
            flash('Creado!', category='success')
            return redirect('/')

    return render_template('sign-up.html', user=current_user)


@auth.route('/registrar_owner', methods=['GET', 'POST'])
def registrar_owner():
    if request.method == 'POST':
        email = request.form.get('email')
        name = request.form.get('name')
        password = request.form.get('psw')
        password_2 = request.form.get('psw2')
        modelo = request.form.get('modelo')
        pilotos = request.form.get('pilotos')
        tripulacion = request.form.get('crew')
        hacia = request.form.get('hacia')
        desde = request.form.get('desde')
        azafatas = request.form.get('azafatas')
        precio = request.form.get('precio')
        equipaje = request.form.get('equipaje')
        fecha = request.form.get('fecha')
        if len(email) < 4:
            flash('email tiene que ser mayor a 4 caracteres!', category='error')
        elif password != password_2:
            flash('Las passwords no coinciden', category='error')
        else:
            new_owner = Owner(email=email, password=generate_password_hash(password, method='sha256'), name=name)
            new_avion = Avion(modelo=modelo, pilotos=pilotos, tripulacion=tripulacion, hacia=hacia, desde=desde,
                              azafatas=azafatas, precio=precio, equipaje=equipaje, fecha=fecha)
            db.session.add(new_avion)
            db.session.add(new_owner)
            db.session.commit()
            flash('Creado!', category='success')
            return redirect('/')

    return render_template('registrar_owner.html')


'''
@auth.route('/registrar_avion', methods=['GET','POST'])
def registrar_avion():
    if request.method == 'POST':
        modelo = request.form.get('modelo')
        pilotos = request.form.get('pilotos')
        tripulacion = request.form.get('crew')
        hacia = request.form.get('hacia')
        desde = request.form.get('desde')
        azafatas = request.form.get('azafatas')
        precio = request.form.get('precio')
        equipaje = request.form.get('equipaje')
        fecha = request.form.get('fecha')
        if hacia == desde:
            flash('Mismo Destino de entrada y salida', category='error')
        else:
            new_avion = Avion(modelo = modelo,tripulacion=tripulacion,pilotos=pilotos,azafatas=azafatas,equipaje=equipaje,precio=precio,hacia=hacia,desde=desde,fecha=fecha)
            db.session.add(new_avion)
            db.session.commit()
            flash('Creado!',category='success')
            return redirect('/')

    return render_template('registrar_modelo.html')
'''


@auth.route('/paga', methods=['GET', 'POST'])
def pagar():
    if request.method == 'POST':
        conexion = sqlite3.connect('database.db')
        cursor = conexion.cursor()
        sentenciaSQL = cursor.execute("SELECT email FROM user")
        tabla_email_user = cursor.fetchall()
        for tupl_email_user in tabla_email_user:
            for email_user in tupl_email_user:
                pass
        email = request.form.get('email')
        nombre = request.form.get('nombre')
        tarjeta = request.form.get('tarjeta')
        nro_tarjeta = request.form.get('nro_de_tarjeta')
        c_seguridad = request.form.get('c_seguridad')
        if email_user != email:
            flash('Email no conocido, registrate primero!',category='error')
        elif len(nro_tarjeta) < 16:
            flash('Nro de tarjeta muy corto, no usar espacios!!',category='error')
        elif len(nro_tarjeta) > 16:
            flash('Nro de tarjeta muy largo, no usar espacios!!',category='error')
        elif len(c_seguridad) > 4:
            flash('Codigo de seguridad muy largo',category='error')
        elif len(c_seguridad) < 3:
            flash('codigo de seguridad muy corto',category='error')
        else:
            pago = Pagos(email=email,nombre=nombre,tarjeta=tarjeta,nro_tarjeta=nro_tarjeta,codigo_seguridad=c_seguridad)
            db.session.add(pago)
            db.session.commit()
            flash('Disfruta!')
            return redirect('/')
    return render_template('pagar.html')