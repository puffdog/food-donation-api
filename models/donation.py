from mongoengine import Document, StringField, IntField, DateTimeField
from datetime import datetime

class Donation(Document):
    food_item = StringField(required=True)
    quantity = IntField(required=True)
    location = StringField(required=True)
    created_at = DateTimeField(default=datetime.utcnow)
