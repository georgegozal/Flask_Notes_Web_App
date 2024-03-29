import click
from flask.cli import with_appcontext
from app.extensions import db
from app.auth.models import User
from werkzeug.security import generate_password_hash


def init_db():
    db.drop_all()
    db.create_all()
    db.session.commit()
    click.echo("Created database")


@click.command('init_db')
@with_appcontext
def init_db_command():
    init_db()


def add_admin():
    admin_user = User(
        first_name='Admin',
        email='admin@gmail.com',
        password=generate_password_hash('admin', 'sha256'),
        role='admin'
    )
    try:
        db.session.add(admin_user)
        db.session.commit()
        click.echo('Admin has been added!')
    except Exception as e:
        click.echo(e)


@click.command('add_admin')
@with_appcontext
def add_admin_command():
    add_admin()
