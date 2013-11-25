from app import app
from flask import render_template, request
from config import BASE_URL


@app.route('/')
def index():
    page_url = BASE_URL + request.path
    social = {
        'title': "Dorothy's List",
        'subtitle': 'A montly read-along with VPR for young adults',
        'img': 'http://www.vpr.net/apps/dorothy/static/img/dec-book.jpg',
        'description': "Dorothy's List is a monthly series by VPR based on the Dorothy Canfield Fisher reading list",
        'twitter_text': "Read along with Dorothy's List, a VPR series",
        'twitter_hashtag': 'reading'
    }

    return render_template('content.html', social=social, page_url=page_url)
