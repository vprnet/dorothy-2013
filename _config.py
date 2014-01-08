import os

# DB Configuration
basedir = os.path.abspath(os.path.dirname(__file__))
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
SQLALCHEMY_ECHO = True

# Frozen Flask
FREEZER_DEFAULT_MIMETYPE = 'text/html'
FREEZER_IGNORE_MIMETYPE_WARNINGS = True

# Amazon S3 Settings
AWS_KEY = ''
AWS_SECRET_KEY = ''
AWS_BUCKET = 'www.vpr.net'
AWS_DIRECTORY = 'apps/dorothys-list'

# Cache Settings (units in seconds)
STATIC_EXPIRES = 60 * 24 * 3600
HTML_EXPIRES = 3600

# Upload Settings (ignores anything included below)
IGNORE_DIRECTORIES = ['.git', 'venv', 'sass', 'templates']
IGNORE_FILES = ['.DS_Store']
IGNORE_FILE_TYPES = ['.gz', '.pyc', '.py', '.rb', '.md']

if AWS_DIRECTORY:
    BASE_URL = 'http://' + AWS_BUCKET + '/' + AWS_DIRECTORY
    FREEZER_BASE_URL = BASE_URL
else:
    BASE_URL = 'http://' + AWS_BUCKET
