import sys
from app import app, db, admin
from app.models import BookAdmin
from flask_frozen import Freezer
from upload_s3 import set_metadata
import os.path as op

freezer = Freezer(app)

if __name__ == '__main__':
    if len(sys.argv) > 1 and sys.argv[1] == 'build':
        freezer.freeze()
        set_metadata()
    else:
        path = op.join(op.dirname(__file__), 'app/static/uploaded')
        admin.add_view(BookAdmin())
        db.create_all()
        app.run(debug=True)
