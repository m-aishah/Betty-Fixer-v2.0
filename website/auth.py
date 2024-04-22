from flask import Blueprint, render_template, request, flash, redirect, url_for
'''
Contains functionalities for authorization pages (login, signup, logout).
'''

# NEED TO IMPLEMENT CONTINUE WITH GOOGLE BUTTON! LOOK UP HOW TO DO IT!!!

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    '''
    Defines view functionality for the login page.

    Returns: The login page.
    '''
    if request.method == 'POST':
        email = request.form.get('email')
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

@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    '''
    Defines view functionality for the sign up page.
    
    Returns: The sign up page.
    '''
    if request.method == 'POST':
        email = request.form.get('email')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        if len(email) < 4:
            flash('Email is too short. Please enter a valid email', category='error')
        elif len(password1) < 7:
            flash('Password must be at least 7 characters', category='error')
        elif password1 != password2:
            flash('Passwords do not match', category='error')  
        else:
            # Create new user
            # Add new user to the database
            # LOgin user
            # Print/Flash success message.
            flash('Account created', category='success')
            # Redirect to homepage.
            return redirect(url_for('views.home'))
        
    return render_template("sign_up.html")

