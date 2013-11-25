import sys
from app import app, db, admin
from app.models import Book
from flask_frozen import Freezer
from flask.ext.admin.contrib.sqla import ModelView
from upload_s3 import set_metadata

freezer = Freezer(app)

if __name__ == '__main__':
    if len(sys.argv) > 1 and sys.argv[1] == 'build':
        freezer.freeze()
        set_metadata()
    else:
        admin.add_view(ModelView(Book, db.session))
        db.create_all()
        app.run(debug=True)
