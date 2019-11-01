import os

DEBUG = True
# SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL", "sqlite:///data.db")
SQLALCHEMY_DATABASE_URI = os.environ.get("ELEPHANT_DB_URL", "sqlite:///data.db")
SQLALCHEMY_TRACK_MODIFICATIONS = False
PROPAGATE_EXCEPTIONS = True
SECRET_KEY = 'secret-key'

MAIL_DEFAULT_SENDER = ("David", "ugberodavid@gmail.com")