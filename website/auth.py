from flask import Blueprint, render_template
'''
Contains functionalities for authorization pages (login, signup, logout).
'''

auth = Blueprint('auth', __name__)

@auth.route('/login')
def login():
    '''
    Defines view functionality for the login page.

    Returns: The login page.
    '''
    return render_template("login.html")

@auth.route('/logout')
def logout():
    '''
    Defines the view funtionality for the logout page.
    
    Returns: the logout page.
    '''
    return "<h1>Logout</h1>"

@auth.route('/sign-up')
def sign_up():
    '''
    Defines view functionality for the sign up page.
    
    Returns: The sign up page.
    '''
    return render_template("sign_up.html")

