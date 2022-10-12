from app.extensions import db 
from flask_login import UserMixin 
from flask_admin.contrib.sqla import ModelView
from flask import redirect, url_for
from flask_login import current_user


class User(db.Model,UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True, nullable=False, index=True)
    password = db.Column(db.String(150), nullable=False)
    first_name = db.Column(db.String(150), nullable=False, index=True)
    role = db.Column(db.String(100), default='user')
    notes = db.relationship('Note', backref='note_user') # allow user to see its notes

    def __repr__(self):
        return self.first_name

    def is_admin(self):
        return self.role == "admin"


class UserView(ModelView):

    def is_accessible(self):
        try:
            is_admin = current_user.is_admin()
        except AttributeError as a:
            print(a)
            is_admin = False
        return is_admin

    def inaccessible_callback(self, name, **kwargs):
        return redirect(url_for('auth.login'))

    can_create = False
    can_delete = False
    can_edit = True
    column_exclude_list = ['password']
    column_searchable_list = ['id', 'first_name', 'email']
    column_filters = ['role']
    column_editable_list = ['role']
    column_list = ('id', 'first_name', 'email', 'role')
