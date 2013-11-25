from app import db


class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(128))
    author = db.Column(db.String(128))
    description = db.Column(db.Text)
    air_date = db.Column(db.Date)

    def __repr__(self):
        return '<Book %r>' % (self.title)
