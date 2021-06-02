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
    return render_template('profile.html', user=current_user.user)