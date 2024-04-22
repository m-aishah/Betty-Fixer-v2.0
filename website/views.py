from flask import Blueprint, render_template
'''Contains views definitions for the website.'''

views = Blueprint('views', __name__)

@views.route('/')
def home():
    '''
    Defines the homepage functionality.
    
    Returns: the homepage.
    '''
    return render_template("home.html")
