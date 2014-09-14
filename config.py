import os
DEBUG = True  # Turns on debugging features in Flask
BCRYPT_LEVEL = 12  # Configuration for the Flask-Bcrypt extension
MAIL_FROM_EMAIL = "broadcasting@nuimsu.com"  # For use in application emails
basedir = os.path.abspath(os.path.dirname(__file__))
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')
TITLE = "MarsMessage"
SECRET_KEY ="SECRET_KEY"
