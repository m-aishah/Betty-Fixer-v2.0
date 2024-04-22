from flask import Blueprint, render_template, request, flash, redirect, url_for
'''
Contains functionalities for authorization pages (login, signup, logout).
'''

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    '''
    Defines view functionality for the login page.

    Returns: The login page.
    '''
    if request.method == 'POST':
        email = request.form.get('emmail')
        password = request.form.get('password')

        print(email, password)
        # Check user exists in database.
        # Check password is correct.
        # redirect to homepage.
        return redirect(url_for('views.home'))
        # Login user.
        # If password is not correct, flash error
        # If user does not exist flash error.
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

