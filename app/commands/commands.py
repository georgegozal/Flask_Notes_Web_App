import click
from flask.cli import with_appcontext
from app.extensions import db
from app.auth.models import User
from werkzeug.security import generate_password_hash


@click.command('init_db')
@with_appcontext
def init_db():
    db.drop_all()
    db.create_all()
    db.session.commit()
    click.echo("Created database")


@click.command('make_admin')
@with_appcontext
def create_admin_user():
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
