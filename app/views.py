from app import app
from flask import render_template, request
from config import BASE_URL


@app.route('/')
def index():
    page_url = BASE_URL + request.path
    social = {
        'title': "Dorothy's List",
        'subtitle': "VPR's Book Club For Kids",
        'img': 'http://www.vpr.net/apps/dorothys-list/static/img/wonder.jpg',
        'description': "Each month VPR highlights a book nominated for the Dorothy Canfield Fisher Children's Book Award. This month's book is 'Wonder' by R.J. Palacio.",
        'twitter_text': "Read along with Dorothy's List, a VPR book club for kids:",
        'twitter_hashtag': 'books,reading'
    }

    return render_template('content.html', social=social, page_url=page_url)
