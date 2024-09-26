from mongoengine import Document, StringField
from werkzeug.security import generate_password_hash, check_password_hash

class User(Document):
    username = StringField(required=True, unique=True)
    password = StringField(required=True)

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)
