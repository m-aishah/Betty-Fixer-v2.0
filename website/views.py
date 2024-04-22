from flask import Blueprint
'''Contains views definitions for the website.'''

views = Blueprint('views', __name__)

@views.route('/')
def home():
    '''
    Defines the homepage functionality.
    
    Returns: the homepage.
    '''
    return "<h1>Homepage</h1>"
