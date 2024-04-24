


from models.user import User
import bcrypt


class UserService(object):
    """
    Service functions for user-related business logic
    """

    def login_user(self, username, password):
        """
        Authenticate user credentials and return the user identifier.

        :param username: Username of the user
        :param password: Password of the user
        :return: User object if authentication is successful, otherwise None
        """

        # Find the user by username
        user = User.objects(username=username).first()

        # If the user does not exist
        if not user:
            raise ValueError("User not found")

        # Verify the password
        if bcrypt.checkpw(password.encode('utf-8'), user.password_hash):
            return user
        else:
            raise ValueError("Invalid password")
