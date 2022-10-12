from app.extensions import db 
from sqlalchemy.sql import func

class Note(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    text = db.Column(db.String(10000))
    date = db.Column(db.DateTime(timezone=True),default=func.now())
    user_id = db.Column(db.Integer,db.ForeignKey('user.id')) 
    
    def __repr__(self):
        return '<Note %r>' % self.id
