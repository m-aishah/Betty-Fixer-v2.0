from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
'''COntains schemas of database model'''

class User(db.Model, UserMixin):
    '''
    Defines User table.
    '''
    # Attributes
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(150))
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    code_history = relationship("codeHistory", back_populates="user")


class codeHistory(db.Model):
    '''
    Defines the code history table
    '''
    # Attributes
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(150))
    content = db.Column(db.Text)
    timestamp = db.Column(db.DateTime(timezone=True), default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    user = relationship("User", back_populates="code_history")