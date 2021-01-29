from .db import db

class Item(db.Document):
    name = db.StringField(required=True, unique=True)
    price = db.StringField(required=True, unique=True)