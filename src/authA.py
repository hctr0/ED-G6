from flask import Blueprint, render_template, redirect, url_for, request, flash, app
from flask_login import login_user, logout_user, login_required, current_user
from flask_marshmallow import Marshmallow
from sqlalchemy.orm import query
from werkzeug.security import generate_password_hash, check_password_hash
from .models import  User
from src.resources.ListNodes import *
from . import db
from .models import User, Solicitudes
from .CrudF import *
from time import time
import numpy as np
authA = Blueprint('authA', __name__)
colaPrioridadSolicitud =CrudF()

#UN ESTUDIANTE LOGEADO PUEDE ACCEDER AQUI, BUSCAR UNA FORMA DE NO VALIDAR EL INGRESO
# USANDO EL BYTE DE LA BASE DE DATOS


@authA.route('/solicitudesA', methods=['GET', 'POST'])  # las rutas de administrador deben ser distintas a las del usuario auth*--- verificar el html en solicitudes hay un ejemplo de if
def solicitudesA():
    return render_template('querA.html')


#ESTO NECESITA MOSTRAR LOS DATOS EN LA LISTA Y TERMINADO


@authA.route('/Historial_Administrativo', methods=['POST'])
@login_required
def historialsolicitudesA():
    solicitudes = db.session.query(Solicitudes).all()
    colaPrioridad= colaPrioridadSolicitud.crearColaPrioridadConRespuesta(solicitudes)
    solicitud2=colaPrioridadSolicitud.devolverLista(colaPrioridad)
    return render_template('historialsolicitudesA.html',solicitud_usuario=solicitud2)

@authA.route('/Solicitudes_Pendientes_Admin', methods=['GET','POST'])
@login_required
def solicitudespendientes():
    global solicitud_usuario
    solicitudes = db.session.query(Solicitudes).all()
    colaPrioridad= colaPrioridadSolicitud.crearColaPrioridadSinRespuesta(solicitudes)
    solicitud_usuario=colaPrioridadSolicitud.devolverLista(colaPrioridad)
    return render_template('todas_las_solicitudesA.html', solicitud_usuario=solicitud_usuario)
@authA.route('/solicitudesAdmin', methods=['POST'])
@login_required
def respondQuery():
    solucionQuery=request.form.get('Solicitudes')
    valores=solucionQuery.split()
    solicitudSeleccionada= valores[0]
    idUser=int(valores[1])
    global querRespond
    for query in solicitud_usuario:
        #print(query.idUser,idUser,"query",query.solicitud,solicitudSeleccionada,query.idUser==idUser,query.solicitud==solicitudSeleccionada)
        if (query.idUser==idUser and query.solicitud==solicitudSeleccionada):
            querRespond=query
            return render_template('solicitudesAdmin.html', solicitud=query)
@authA.route('/respuestaAdmin', methods=['POST'])
@login_required
def respuestaAdmin():
    respuesta = request.form.get('Respuesta')
    solicitud1=db.session.query(Solicitudes).filter_by(id = querRespond.id).first()
    solicitud1.respuesta = respuesta
    db.session.commit()
    db.session.close()
    return render_template('formulario-completado.html')
    
