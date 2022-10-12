from flask import Flask, render_template
from flask_login import LoginManager
from app.config import Config
from app.auth.models import User
from app.note.models import Note
from app.auth.views import auth
from app.note.views import note
from app.extensions import db, migrate, mail, ckeditor, login_manager



BLUEPRINTS = [auth,note]
COMMANDS = []


def create_app():

    app = Flask(__name__)

    app.config.from_object(Config)

    register_extensions(app)
    register_blueprints(app)

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    # Invalid URL
    @app.errorhandler(404)
    def page_not_found(e):
        return render_template('404.html'), 404

    # Internal Server Error
    @app.errorhandler(500)
    def internal_server_error(e):
        return render_template('500.html'), 500

    return app


def register_blueprints(app):

    for blueprint in BLUEPRINTS:
        app.register_blueprint(blueprint)


def register_extensions(app):

    # Setup Flask-SQLAlchemy
    db.init_app(app)

    # Setup Flask-Migrate
    migrate.init_app(app, db)

    # Setup Flask-Mail
    mail.init_app(app)

    # Setup Flask-CKEditor
    ckeditor.init_app(app)

    # Flask-RESTful
    # api.init_app(app)

    # Flask-Login
    @login_manager.user_loader
    def load_user(id_):
        return User.query.get(id_)

    login_manager.init_app(app)


# def create_database(app):
#     if not path.exists('.' + DB_NAME):
#         db.create_all(app=app)
#         print('Created Database!')
