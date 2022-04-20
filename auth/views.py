from flask import Blueprint, render_template, request, flash ,redirect, url_for
from werkzeug.security import generate_password_hash, check_password_hash

#from . import db
#from flask_login import login_user, login_required, logout_user, current_user

auth = Blueprint('auth',__name__,template_folder='templates/auth')

@auth.route('/')
def index():
    return render_template('index.html')

@auth.route('/login')
def login():
    pass

@auth.route('/logout')
def logout():
    pass

@auth.route('/sign-up')
def sign_up():
    pass