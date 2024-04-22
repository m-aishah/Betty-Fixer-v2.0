from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func
'''COntains schemas of database model'''

class User(db.Model, UserMixin):
    '''
    Defines User table.
    '''
    # Attributes
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
