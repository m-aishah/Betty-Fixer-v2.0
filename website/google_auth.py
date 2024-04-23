from flask import Blueprint, redirect, request, url_for
from flask_login import (login_user, current_user)
from . import db
import os
import requests
import json
from werkzeug.security import generate_password_hash
from oauthlib.oauth2 import WebApplicationClient
from .models import User


google_auth = Blueprint('google_auth', __name__)

# Configuration for Sign up with Google Button
GOOGLE_CLIENT_ID = os.environ.get("GOOGLE_CLIENT_ID")
GOOGLE_CLIENT_SECRET = os.environ.get("GOOGLE_CLIENT_SECRET")
GOOGLE_DISCOVERY_URL = (
    "https://accounts.google.com/.well-known/openid-configuration"
)

# OAuth 2 client setup
client = WebApplicationClient(GOOGLE_CLIENT_ID)
    

def get_google_provider_cfg():
    '''
    Retrieves Google's provider configuration.'''
    return requests.get(GOOGLE_DISCOVERY_URL).json()

@google_auth.route('/google_login', methods=['GET', 'POST'])
def google_login():
    '''
    Initiate OAuth 2 flow with Google form my client application.
    '''
    # Find out what URL to hit for Google login
    google_provider_cfg = get_google_provider_cfg()
    authorization_endpoint = google_provider_cfg["authorization_endpoint"]

    # Use library to construct the request for Google login and provide
    # scopes to allow retrieval of user's profile from Google
    request_uri = client.prepare_request_uri(
        authorization_endpoint,
        redirect_uri=url_for('google_auth.callback', _external=True),
        scope=["openid", "email", "profile"]
    )
    return redirect(request_uri)

@google_auth.route("/google_login/callback")
def callback():
    '''
    Login call back endpoint. Contains OIDC steps.
    '''
    # Get authorization code Google sent back to you.
    code = request.args.get("code")
    # Find out what URL to hit to get tokens specific to user.
    google_provider_cfg = get_google_provider_cfg()
    token_endpoint = google_provider_cfg["token_endpoint"]
    
    # Prepare and send request to get tokens!
    token_url, headers, body = client.prepare_token_request(
        token_endpoint,
        authorization_reponse=request.url,
        redirect_url=request.base_url,
        code=code
    )
    token_response = requests.post(
        token_url,
        headers=headers,
        data=body,
        auth=(GOOGLE_CLIENT_ID, GOOGLE_CLIENT_SECRET),
    )
    # Parse the tokens!
    client.parse_request_body_response(json.dumps(token_response.json()))

    # Find and hit the URL
    # from Google that gives the user's profile information,
    # including their Google profile email
    userinfo_endpoint = google_provider_cfg["userinfo_endpoint"]
    uri, headers, body = client.add_token(userinfo_endpoint)
    userinfo_response = requests.get(uri, headers=headers, data=body)

    # Check that email is verified - added layer of security.
    # Get andp arse user information - 
    # sub - unique identifier for the user in Google,
    # email, given_name, picture?
    if userinfo_response.json().get("email_verified"):
        unique_id = userinfo_response.json()["sub"]
        email = userinfo_response.json()["email"]
        # picture = userinfo_response.json()["picture"]
        # users_name = userinfo_response.json()["given_name"]
    else:
        # flash error!
        return "User email not avaialable or not verified by Google.", 400
    
    # If user is not already in database,
    user = User.query.filter_by(email=email).first()
    if not user:
        # create user in database, add user to database.
        user = User(email=email, password=generate_password_hash(unique_id))
        # Add new user to the database
        db.session.add(user)
        db.session.commit()

    # LOgin user
    login_user(user, remember=True)
    # Print/Flash success message.
    # flash('Welcome!', category='success')
    # Redirect to homepage.
    return redirect(url_for('views.home'))