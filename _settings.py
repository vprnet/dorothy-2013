# Amazon S3 Settings
AWS_KEY = ''
AWS_SECRET_KEY = ''
AWS_BUCKET = 'www.vpr.net'
AWS_DIRECTORY = 'apps/dorothy'

# Cache Settings (units in seconds)
STATIC_EXPIRES = 60 * 24 * 3600
HTML_EXPIRES = 3600

# Upload Settings (ignores anything included below)
IGNORE_DIRECTORIES = ['.git', 'venv', 'sass', 'templates']
IGNORE_FILES = ['.DS_Store']
IGNORE_FILE_TYPES = ['.gz', '.pyc', '.py', '.rb', '.md']
