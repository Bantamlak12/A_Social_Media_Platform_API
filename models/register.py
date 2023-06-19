import re
from flask import Flask, jsonify
from flask_mysqldb import MySQL
from werkzeug.security import generate_password_hash

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


def register_user(first_name, last_name, username, email, password, confirm_password):
    # Check if username is alphanumeric
    if not re.match("^[a-zA-Z0-9]+$", username):
        return 'Username is invalid!'

    # Check if email is valid
    if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
        return 'Email is invalid!'

    cur = mysql.connection.cursor()
    # Check if username or email already exists in the database
    cur.execute(
        'SELECT * FROM users WHERE username = %s', (username,))

    existing_username = cur.fetchone()

    cur.execute(
        'SELECT * FROM users WHERE email = %s', (email,))

    existing_email = cur.fetchone()

    if existing_username:
        return 'Username already taken!'
    elif existing_email:
        return 'Email already taken!'
    else:
        # Store user information in database
        # Check if the passwords match and hashed it
        if password != confirm_password:
            return 'Password do not match!'

        hashed_password = generate_password_hash(password)
        cur.execute('INSERT INTO users (first_name, last_name, username, email, password) VALUES (%s, %s, % s, %s, %s)',
                    (first_name, last_name, username, email, hashed_password))
        mysql.connection.commit()

        # Return message on success
        return 'You have successfully registered!'
