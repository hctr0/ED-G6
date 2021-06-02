from flask import Flask
from sqlalchemy.orm import session
from sqlalchemy.pool import NullPool
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_login import LoginManager, current_user

# init SQLAlchemy so we can use it later in our models
db = SQLAlchemy()
def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI']='mysql+pymysql://uzxpqo8j0ozt5cpg:IdBAaIBrbhWUxxRBqPSi@bg5m5ny2senqgkimy678-mysql.services.clever-cloud.com/bg5m5ny2senqgkimy678'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SQLALCHEMY_POOL_SIZE']=200
    #app.config['SQLALCHEMY_ENGINE_OPTIONS'] = {
    #'poolclass': NullPool,
    #}
    app.secret_key = 'super secret key'
    app.config['SESSION_TYPE'] = 'filesystem'
    db = SQLAlchemy(app)
    
    db.init_app(app)
    engine_container = db.get_engine(app)
    def cleanup(session):
        print("clean")
        db.session.close()
        db.drop_all()
        db.session.remove()
        session.close()
        engine_container.dispose()
    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)
    from .models import User
    @login_manager.user_loader
    def load_user(user_id):
        print('paso2')
        # since the user_id is just the primary key of our user table, use it in the query for the user
        try:
            #user1= User.query.get(int(user_id))
            id = user_id
            user1 = db.session.query(User).filter_by(id = id).first()
            print(db.session.query(User).filter_by(id = id).first())
        except Exception as error:
            raise error
        finally:
            cleanup(db.session)
        return user1
        #return current_user
    # blueprint for auth routes in our app
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    # blueprint for non-auth parts of app
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app





    
        