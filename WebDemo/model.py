from app import db
import datetime


class Content(db.Document):
    text = db.StringField()

class Summary(db.Document):
    text = db.StringField()

class Article(db.Document):
    article = db.ReferenceField(Content)
    abstract = db.ReferenceField(Summary)
    date = db.DateTimeField(default=datetime.datetime.utcnow)
