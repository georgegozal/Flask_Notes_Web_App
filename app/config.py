import os
PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))


class Config(object):

    SECRET_KEY = 'hjshjhdjah kasdw21jshkjdhjs'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') \
        or 'sqlite:///' + os.path.join(PROJECT_ROOT, 'db.sqlite')
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'asd;lkajs-90 as;doaks ;;/A'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
