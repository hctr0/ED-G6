from flask import Blueprint, render_template, redirect, url_for, request, flash, app
from flask_login import login_user, logout_user, login_required
from flask_marshmallow import Marshmallow
from sqlalchemy.orm import query
from werkzeug.security import generate_password_hash, check_password_hash
from .models import  User
from src.resources.ListNodes import *
from . import db
authA = Blueprint('authA', __name__)



#UN ESTUDIANTE LOGEADO PUEDE ACCEDER AQUI, BUSCAR UNA FORMA DE NO VALIDAR EL INGRESO
# USANDO EL BYTE DE LA BASE DE DATOS


#ESTO NECESITA BACKEND ENTERO -- VER querA.html para más info
@authA.route('/solicitudesA', methods=['GET', 'POST'])  # las rutas de administrador deben ser distintas a las del usuario auth*--- verificar el html en solicitudes hay un ejemplo de if
def solicitudesA():
    return render_template('querA.html')



#ESTO NECESITA BACKEND ENTERO -- VER historialsolicitudesA.html para más info
@authA.route('/Historial_Administrativo', methods=['GET','POST'])
@login_required
def historialsolicitudesA():
    return render_template('historialsolicitudesA.html')

@authA.route('/Solicitudes_Pendientes_Admin', methods=['GET','POST'])
@login_required
def solicitudespendientes():
    return render_template('todas_las_solicitudesA.html')
