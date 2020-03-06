from .. import db

class Category(db.Model):

    __tablename__ = 'category'

    appId = db.Column(db.Integer, primary_key=True)
    category = db.Column(db.String(45))