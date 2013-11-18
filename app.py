import sys
from upload_s3 import set_metadata
from settings import AWS_BUCKET, AWS_DIRECTORY

from flask import Flask, render_template, request
from flask_frozen import Freezer

app = Flask(__name__)
freezer = Freezer(app)

app.config['FREEZER_DEFAULT_MIMETYPE'] = 'text/html'
app.config['FREEZER_IGNORE_MIMETYPE_WARNINGS'] = True

if AWS_DIRECTORY:
    base_url = 'http://' + AWS_BUCKET + '/' + AWS_DIRECTORY
    app.config['FREEZER_BASE_URL'] = base_url
else:
    base_url = 'http://' + AWS_BUCKET

# If Flask is needed to generate URLs, use freezer.register_generator
# see: http://pythonhosted.org/Frozen-Flask/#url-generators


@app.route('/')
def index():
    page_url = base_url + request.path
    social = {
        'title': "Dorothy's List",
        'subtitle': 'A montly read-along with VPR for young adults',
        'img': 'http://www.vpr.net/apps/dorothy/static/img/dec-book.jpg',
        'description': "Dorothy's List is a monthly series by VPR based on the Dorothy Canfield Fisher reading list",
        'twitter_text': "Read along with Dorothy's List, a VPR series",
        'twitter_hashtag': 'reading'
    }

    return render_template('content.html', social=social, page_url=page_url)

if __name__ == '__main__':
    if len(sys.argv) > 1 and sys.argv[1] == 'build':
        freezer.freeze()
        set_metadata()
    else:
        app.run(debug=True)
