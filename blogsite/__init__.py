from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager

db = SQLAlchemy()
DB_NAME = "database.db"

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = "Yet Another Python Flask Blog"
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    db.init_app(app) 
    
    from .views import views    # from .views import views as views_blueprint
    from .auth import auth      # from .auth import auth as auth_blueprint
     
    app.register_blueprint(blueprint=views, url_prefix='/')
    app.register_blueprint(blueprint=auth, url_prefix='/')
    
    from .models import User

    create_database(app=app)

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)
    
    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))
    
    return app

def create_database(app):
    if not path.exists('blogsite/' + DB_NAME):
        with app.app_context():
            db.create_all()
            print("deneme")
    print('Created Database!')