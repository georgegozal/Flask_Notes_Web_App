from app.extensions import db 
from flask_login import UserMixin 


class User(db.Model,UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True, nullable=False, index=True)
    password = db.Column(db.String(150), nullable=False)
    first_name = db.Column(db.String(150), nullable=False, index=True)
    # role = db.Column(db.String(100), default='user')
    notes = db.relationship('Note') # allow user to see its notes
