from flask import Flask
'''Init website module.'''

def create_app():
    '''
    Create and setup Flask application.
    
    Returns: the flask application.
    '''
    app = Flask(__name__)
    # Initialize application's secret key.
    app.config['SECRET_KEY'] = 'This is my secret key.'

    return app