from flask import Blueprint, render_template, request, flash, redirect, url_for
from . import db
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import (login_user, login_required, logout_user, current_user)
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

        # print(email, password)
        user = User.query.filter_by(email=email).first()
        # Check user exists in database.
        if user:
        # Check password is correct.
            if check_password_hash(user.password, password):
                flash('Logged in successfully!', category='success')
                # Login user.
                login_user(user, remember=True)
                # redirect to homepage.
                return redirect(url_for('views.home'))
            else:
                # If password is not correct, flash error
                flash('Incorrect Password: Please try again.', category='error')
        else:
            # If user does not exist flash error.
            flash('Invalid User: Please enter valid login details.', category='error')    
        
    return render_template("login.html", user=current_user)

@auth.route('/logout')
@login_required
def logout():
    '''
    Defines the view funtionality for the logout page.
    
    Returns: the logout page.
    '''
    # Logout user
    logout_user()
    return redirect(url_for('auth.login'))

@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    '''
    Defines view functionality for the sign up page.
    
    Returns: The sign up page.
    '''
    if request.method == 'POST':
        first_name = request.form.get('first_name')
        email = request.form.get('email')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        user = User.query.filter_by(email=email).first()
        if user:
            flash('This account already exists. Login or use a different email', category='error')
        elif len(email) < 4:
            flash('Email is too short. Please enter a valid email', category='error')
        elif len(password1) < 7:
            flash('Password must be at least 7 characters', category='error')
        elif password1 != password2:
            flash('Passwords do not match', category='error')  
        else:
            # Create new user
            new_user = User(first_name=first_name, email=email, password=generate_password_hash(password1))
            # Add new user to the database
            db.session.add(new_user)
            db.session.commit()
            # LOgin user
            login_user(new_user, remember=True)
            # Print/Flash success message.
            flash('Account created', category='success')
            # Redirect to homepage.
            return redirect(url_for('views.home'))
        
    return render_template("sign_up.html", user=current_user)