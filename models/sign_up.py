#!/usr/bin/python3
"""This module defines a logic to sign up"""
from werkzeug.security import generate_password_hash
from flask import Flask, jsonify
from flask_mysqldb import MySQL
from email_validator import validate_email, EmailNotValidError
import re


app = Flask(__name__, template_folder='../templates',
            static_folder='../static')


# Load configuration from database_config.py
app.config.from_pyfile('database_config.py')

# Configure MySQL
app.config['MYSQL_HOST'] = app.config['MYSQL_HOST']
app.config['MYSQL_USER'] = app.config['MYSQL_USER']
app.config['MYSQL_PASSWORD'] = app.config['MYSQL_PASSWORD']
app.config['MYSQL_DB'] = app.config['MYSQL_DB']

mysql = MySQL(app)


def signup_user(first_name, last_name, username, email, password,
                confirm_password):
    """ This method accepts user information from the frontend and stores
        it in a database after necessary validation.
    """
    # Check if username is alphanumeric
    if not re.match("^[a-zA-Z0-9]+$", username):
        return jsonify({'username_msg': 'Invalid username!'})

    # Check if the email is valid
    try:
        validate_email(email)
    except EmailNotValidError:
        return jsonify({'email_msg': 'Invalid email!'})

    cur = mysql.connection.cursor()
    # Check if username or email already exists in the database
    cur.execute(
        'SELECT * FROM users WHERE username = %s', (username,))

    existing_username = cur.fetchone()

    cur.execute(
        'SELECT * FROM users WHERE email = %s', (email,))

    existing_email = cur.fetchone()

    if existing_username:
        return jsonify({'username_msg': 'Username already taken!'})
    elif existing_email:
        return jsonify({'email_msg': 'Email already taken!'})
    else:
        # Store user information in database
        # Check if the passwords match and hashed it
        if password != confirm_password:
            return jsonify({'password_msg': 'Password do not match!'})

        # Hash and store it into the database.
        hashed_password = generate_password_hash(password)
        query = 'INSERT INTO users (first_name, last_name, username, email,\
                                    password) VALUES (%s, %s, % s, %s, %s)'
        values = (first_name, last_name, username, email, hashed_password)
        cur.execute(query, values)
        mysql.connection.commit()

        # Return success message
        return jsonify({'success_msg': 'Successfully Signed up!'})
