
import logging
from flask import request, jsonify
from services.user_service import UserService
from tasks import store_last_login

logger = logging.getLogger("default")
user_service = UserService()


def index():
    logger.info("Checking the flask scaffolding logger")
    return "Welcome to the flask scaffolding application"


def login():
    """
    Authenticate user credentials and return a JSON response.

    :return: JSON response and an appropriate status code
    """
    
    try:
        # Parse JSON request
        data = request.json
        username = data.get("username")
        password = data.get("password")

        # Validate input
        if not username or not password:
            return jsonify({"error": "Username and password are required"}), 400

        # Authenticate user
        user = user_service.login_user(username, password)
        
        # Trigger Celery task to store last login information
        store_last_login.delay(username)

        # If authentication is successful
        return jsonify({"message": "Login successful", "user": {
            "username": user.username,
            "email": user.email
        }}), 200

    except ValueError as e:
        # Handle authentication errors
        return jsonify({"error": str(e)}), 401

    except Exception as e:
        # Handle other exceptions
        logger.error(f"Error during login: {str(e)}")
        return jsonify({"error": "An error occurred during login"}), 500





