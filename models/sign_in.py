#!/usr/bin/python3
"""This module defines the sign-in functionality of the app."""

from flask import jsonify, make_response
from werkzeug.security import check_password_hash
from flask_jwt_extended import create_access_token, JWTManager
from models.sign_up import app, mysql
from datetime import timedelta

# Configure JWT
app.config['JWT_SECRET_KEY'] = app.config['JWT_SECRET_KEY']
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = timedelta(days=1)

# Initialize JWTManager
jwt = JWTManager(app)


def signin_user(username, password):
    """Signs in a user, validating their credentials."""
    cursor = mysql.connection.cursor()
    cursor.execute(
        'SELECT * FROM users WHERE username = %s', (username,))
    account = cursor.fetchone()

    if account:
        # The user_id will be used to generate an access token.
        user_id = account[0]
        # The password in the database is hashed.
        hashed_password = account[5]
        # Checks if the hashed password in the database is the same as
        # the password the user inputs for sign-in.
        password_matches = check_password_hash(hashed_password, password)
        if password_matches:
            # Generate access token
            access_token = create_access_token(identity=user_id)

            # Set the access token as HTTP-only token
            response = make_response(
                jsonify({'success': 'Signed in Successfully'}))
            response.set_cookie('access_token', access_token, httponly=True)
            return response
        else:
            return jsonify({'signin_password_error': 'Password is incorrect!'})
    else:
        return jsonify({'signin_username_error': 'Username is incorrect!'})
