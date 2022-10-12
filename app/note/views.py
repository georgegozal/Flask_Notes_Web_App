from flask import Blueprint, render_template, request, flash ,redirect, url_for
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_required, current_user
from app.extensions import db
from .models import Note


note = Blueprint('note_bl',__name__,template_folder='templates/note')

@note.route('/', methods=['GET', 'POST'])
@login_required
def home():
    if request.method == 'POST':
        note = request.form.get('text')

        if len(note.strip()) < 1:
            flash('Note is too short!', category='error')
        else:
            new_note = Note(text=note, user_id=current_user.id)
            
            try:
                db.session.add(new_note)
                db.session.commit()
                flash('Note added!', category='success')
            except:
                flash('There was an issue adding your task',category='error')
                
    notes = Note.query.filter_by(user_id=current_user.id).order_by(Note.date).all()

    return render_template("home1.html", user=current_user,notes=notes)


@note.route('/delete/<int:id>')
def delete(id):
    task_to_delete = Note.query.get_or_404(id)

    try:
        db.session.delete(task_to_delete)
        db.session.commit()
        return redirect('/')
    except:
        flash('There was a problem deleting that task',category='error')


@note.route('/update/<int:id>', methods=['GET','POST'])
def update(id):
    note = Note.query.get_or_404(id)
    # task has value content. task.content
    print(note.text)
    if request.method == 'POST':
        # here we rewrite task.content new value from request form
        note.text = request.form['text']
        
        if len(note.text.strip()) > 0:

            try:
                db.session.commit()
                return redirect('/')
            except:
                flash('There was an issue updating your task', category='error')
        
        else:
            return redirect(f'/update/{id}')
        
    else:
        return render_template('update.html',note=note,user=current_user)