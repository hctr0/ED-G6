from flask import Blueprint, render_template, redirect, url_for, request, flash, app
from flask_login import login_user, logout_user, login_required
from flask_marshmallow import Marshmallow
from sqlalchemy.orm import query
from werkzeug.security import generate_password_hash, check_password_hash
from .models import  User
from src.resources.ListNodes import *
from . import db
authA = Blueprint('authA', __name__)
@authA.route('/solicitudesA')  # las rutas de administrador deben ser distintas a las del usuario auth*--- verificar el html en solicitudes hay un ejemplo de if 
def solicitudesA():
    return render_template('querA.html')
