from flask import Blueprint, render_template
from flask_login import login_required, current_user
'''Contains views definitions for the website.'''

views = Blueprint('views', __name__)

@views.route('/')
@login_required
def home():
    '''
    Defines the homepage functionality.
    
    Returns: the homepage.
    '''
    return render_template("home.html", user=current_user)
