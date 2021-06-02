from flask import Blueprint, render_template, redirect, url_for, request, flash, app
from flask_login import login_user, logout_user, login_required
from flask_marshmallow import Marshmallow
from sqlalchemy.orm import query
from werkzeug.security import generate_password_hash, check_password_hash
from .models import User
from src.resources.ListNodes import *
from . import db
from .Crud import *
auth = Blueprint('auth', __name__)
funciones =Crud()
def create_local_list_users():
    ma = Marshmallow(app)
    class TaskSchema(ma.Schema):
            class Meta:
                fields = ('id','user','password')
    tasks_schema= TaskSchema(many=True)
    try:
        all_task = User.query.all()
    except Exception as error:
        raise error
    finally:
        db.session.close()
    result_lista = tasks_schema.dump(all_task)
    #print(type(result_lista), result_lista[0])
    global lista_nodos
    lista_nodos = funciones.AgregarDatosListas(result_lista)
@auth.route('/login')
def login():
    create_local_list_users()
    #print(User.query.all())
    return render_template('login.html')

@auth.route('/login', methods=['POST'])
def login_post():
    user = request.form.get('email')
    password = request.form.get('password')
    remember = True if request.form.get('remember') else False
    print(funciones.BuscarDato(lista_nodos, user).user)
    if  funciones.ExisteDato_boolean(lista_nodos,user):
        user1 = funciones.BuscarDato(lista_nodos, user)
        print("user 1 ",user1)
        if user1.password==password:
            try:
                user2 = User.query.filter_by(user=user1.user).first()
            except Exception as error:
                raise error
            finally:
                db.session.close_all()
                db.session.remove()
            try:
                login_user(user2, remember=remember, duration=True)    
            except Exception as error:
                raise error
            finally:
                db.session.close()
            
            print('paso1')
            return redirect(url_for('main.profile'))
        else:
            flash('Please check your login details and try again.')
            return redirect(url_for('main.profile'))
    else:
        flash('Please check your login details and try again.')
        return redirect(url_for('main.profile'))
        
    

@auth.route('/signup')
def signup():
    return render_template('signup.html')

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.index'))
@auth.route('/signup', methods=['POST'])
def signup_post():
    user = request.form.get('email')
    password = request.form.get('password')
    print('paso')
    user1 = User.query.filter_by(user=user).first() # if this returns a user, then the email already exists in database
    if user1: # if a user is found, we want to redirect back to signup page so user can try again
        return redirect(url_for('auth.signup'))
    print(request.form)
    # create a new user with the form data. Hash the password so the plaintext version isn't saved.
    new_user = User(user=user, password=password)

    # add the new user to the database
    db.session.add(new_user)
    db.session.commit()
    db.session.close()
    #funciones.InsertDato(lista_nodos,new_user[0][2])
    if user1: # if a user is found, we want to redirect back to signup page so user can try again
        flash('Email address already exists')
        return redirect(url_for('auth.signup'))

    return redirect(url_for('auth.login'))
@auth.route('/solicitudes')
def solicitudes():
    return render_template('quer.html')
@auth.route('/solicitudes', methods=['POST'])
def solicitudes_post():
    solicitud = request.form.get('Solicitudes')
    return render_template('formulario.html', solicitud=solicitud)