from . import db
from sqlalchemy.sql import func

class Articles(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(500))
    body = db.Column(db.Text())
    date = db.Column(db.DateTime(timezone=True), default=func.now())

    def __init__(self, title, body):
        self.title = title
        self.body = body

