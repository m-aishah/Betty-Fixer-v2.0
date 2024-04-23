from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os
from os import path
from flask_login import LoginManager

'''Init website module.'''

# Create database object.
db = SQLAlchemy()
DB_NAME = "database.db"


def create_app():
    '''
    Create and setup Flask application.
    
    Returns: the flask application.
    '''
    app = Flask(__name__)
    # Initialize application's secret key.
    app.config['SECRET_KEY'] = os.environ.get("BETTY_FIXER_SECRET", None) or os.urandom(24)
    # COnfigure database.
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    db.init_app(app)

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    # Create the blueprint for the views.
    from .views import views
    from .auth import auth
    from .google_auth import google_auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')
    app.register_blueprint(google_auth, url_prefix='/')

    from .models import User
    create_database(app)
    
    # Flask-Login helper to retrieve a user from our db
    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))
    
    
    return app

def create_database(app):
    '''
    Creates a database for a flask application.
    
    Args:
    app (obj): The flask application.
    '''
    if not path.exists('website/' + DB_NAME):
        with app.app_context():
            db.create_all()
            print('Created Database!')
