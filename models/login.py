from flask import jsonify, make_response
from werkzeug.security import check_password_hash
from flask_jwt_extended import create_access_token, JWTManager
from models.register import app, mysql
from datetime import timedelta

# Configure JWT
app.config['JWT_SECRET_KEY'] = app.config['JWT_SECRET_KEY']
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = timedelta(days=1)

# Initialize JWTManager
jwt = JWTManager(app)


def login_user(username, password):
    cursor = mysql.connection.cursor()
    cursor.execute(
        'SELECT * FROM users WHERE username = %s', (username,))
    account = cursor.fetchone()

    if account:
        user_id = account[0]
        hashed_password = account[5]
        password_matches = check_password_hash(hashed_password, password)
        if password_matches:
            # Generate access token
            access_token = create_access_token(identity=user_id)

            # Set the access token as HTTP-only token
            response = make_response(jsonify({'success': 'Login successful'}))
            response.set_cookie('access_token', access_token, httponly=True)
            return response
        else:
            return jsonify({'signin_password_error': 'Password is incorrect'})
    else:
        return jsonify({'signin_username_error': 'Username is incorrect!'})
