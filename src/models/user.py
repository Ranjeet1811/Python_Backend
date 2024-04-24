from mongoengine import Document, StringField, EmailField, BinaryField
import bcrypt

class User(Document):
    """
    TASK: Create a model for user with minimalistic
          information required for user authentication

    HINT: Do not store password as is.
    """

    username = StringField(required=True, unique=True)
    email = EmailField(required=True, unique=True)
    password_hash = BinaryField(required=True)

    @staticmethod
    def hash_password(password):
        salt = bcrypt.gensalt()
        return bcrypt.hashpw(password.encode('utf-8'), salt)

    def set_password(self, password):
        self.password_hash = self.hash_password(password)

