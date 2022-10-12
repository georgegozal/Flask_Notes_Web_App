from app.extensions import db 
from sqlalchemy.sql import func
from flask_admin.contrib.sqla import ModelView
from flask import redirect, url_for
from flask_login import current_user


class Note(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    text = db.Column(db.String(10000))
    date = db.Column(db.DateTime(timezone=True),default=func.now())
    user_id = db.Column(db.Integer,db.ForeignKey('user.id')) 
    
    def __repr__(self):
        return '<Note %r>' % self.id


class NoteView(ModelView):

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
    column_searchable_list = ['id','note_user.first_name' ]
    column_list = ('id', 'text', 'note_user.first_name', 'date')
