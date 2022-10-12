from flask import Flask, render_template
from flask_login import LoginManager
from app.config import Config
from flask_admin import Admin
from flask_admin.menu import MenuLink
from app.auth.models import User, UserView
from app.note.models import Note, NoteView
from app.auth.views import auth
from app.note.views import note
from app.extensions import db, migrate, mail, login_manager # ckeditor 
from app.commands.commands import init_db, create_admin_user


BLUEPRINTS = [auth,note]
COMMANDS = [init_db, create_admin_user]


def create_app():

    app = Flask(__name__)

    app.config.from_object(Config)

    register_extensions(app)
    register_blueprints(app)
    register_commands(app)
    register_admin_panel(app)

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


def register_commands(app):

    for command in COMMANDS:
        app.cli.add_command(command)


def register_extensions(app):

    # Setup Flask-SQLAlchemy
    db.init_app(app)

    # Setup Flask-Migrate
    migrate.init_app(app, db)

    # Setup Flask-Mail
    mail.init_app(app)

    # Setup Flask-CKEditor
    # ckeditor.init_app(app)

    # Flask-RESTful
    # api.init_app(app)

    # Flask-Login
    @login_manager.user_loader
    def load_user(id_):
        return User.query.get(id_)

    login_manager.init_app(app)


def register_admin_panel(app):
    admin = Admin(app)
    admin.add_view(UserView(User, db.session))
    admin.add_view(NoteView(Note, db.session))
    # admin.add_view(FileView(
    #     Config.PROJECT_ROOT + '/static/uploads', name='Static Files'))
    # https://flask-admin.readthedocs.io/en/latest/api/mod_contrib_fileadmin/
    admin.add_link(MenuLink(name="Return Home", url='/'))
