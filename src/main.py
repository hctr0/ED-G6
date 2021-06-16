from flask import Blueprint, app,request, render_template, jsonify
from flask_login import login_required, current_user
from . import db
main = Blueprint('main', __name__)

#@main.route("/", methods= ['GET', 'POST'])
#def hello():
#    if request.method == 'POST':
        #userdetails= request.form
#        user = request.json['user']
#        password = request.json['password']
        #new_user=User(user, password)
        #db.session.add(new_user)
        #db.session.commit()
        #return task_schema.jsonify(new_user)
#    return render_template("index.html")
#@main.route("/profile", methods= ['GET'])
#def profile():
#    return render_template("profile.html")


@main.route('/')
def index():
        return render_template('index.html')

@main.route('/profile')
@login_required
def profile():
    user =current_user.user
    user_rol = int.from_bytes(current_user.role,byteorder='big')        
    rol=''
    print(user_rol)
    if user_rol:
        rol='estudent'
    else:
        rol='admin'
    return render_template('profile.html', user=user,rol=rol)
@main.route('/profileA')
@login_required
def profileA():
        user =current_user.user
        user_rol = int.from_bytes(current_user.role,byteorder='big')        
        rol=''
        print(user_rol)        
        rol=''
        if user_rol:
            rol='estudent'
        else:
            rol='admin'
        return render_template('profileA.html', user=user, rol=rol)