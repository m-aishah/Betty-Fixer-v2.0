from flask import Blueprint
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
    return "<h1>Login</h1>"

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
    return "<h1>Sign Up</h1>"

