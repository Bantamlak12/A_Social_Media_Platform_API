#!/usr/bin/python3
""" This module contains all the routes necessary to run the Flask application.
"""

from flask import request, jsonify, render_template, redirect, url_for
from models.sign_up import signup_user, app, mysql
from models.sign_in import signin_user
from models.create_post import create_post
from flask_jwt_extended import decode_token
from datetime import datetime, timedelta


@app.route('/', methods=['GET'], strict_slashes=False)
def home():
    """This route defines the home/landing page."""
    return render_template('index.html')


@app.route('/signup', methods=['GET', 'POST'], strict_slashes=False)
def signup():
    """ This route accepts the user information necessary for the signup and
        sends it to the backend models/signup.py file to process the signup.
    """
    # Get user input from request body
    if request.method == 'POST':
        data = request.json

        result = signup_user(
            data['firstName'],
            data['lastName'],
            data['username'],
            data['email'],
            data['password'],
            data['confirmPassword']
        )
        # Sends the result to the frontend Javascript.
        return result

    return render_template('signup.html')


@app.route('/signin', methods=['GET', 'POST'], strict_slashes=False)
def signin():
    """ This route authenticates and signs in a registered user based on their
        credentials.It takes the user credentials from the request body, and
        sends it to models/sign_in.py
    """
    if request.method == 'POST':
        data = request.json
        result = signin_user(
            data['username'],
            data['password']
        )
        # Check the registration resuls
        if request.get_json('signin_username_error') or \
                request.get_json('signin_password_error'):
            return result

    return render_template('signin.html')


@app.route('/feeds', methods=['GET', 'POST'], strict_slashes=False)
def feeds():
    """ This route can only be accessed if a user signs in. It defines the
        methods GET and POST
    """
    # Get the access_token from the cookies
    access_token = request.cookies.get('access_token')

    # If the request method is GET, feeds page will be rendered.
    if request.method == 'GET':
        # If there is an access token, redirect the user to the feeds page
        # else to sign-in page.
        if access_token:
            # If there is an access token, decode it and get the user_id,
            # this user_id will be used to validate the owner of the post
            # when a post is created.
            decoded_token = decode_token(access_token)

            # Validate the token
            if decoded_token:
                user_id = decoded_token.get('sub')
                # If the user_id is in the decoded token, then make connection.
                if user_id:
                    cursor = mysql.connection.cursor()
                    cursor.execute(
                        'SELECT first_name FROM users WHERE user_id = %s', (
                            user_id,)
                    )
                    user_tuple = cursor.fetchone()

                    # This first_name will be displayed on the welcome header
                    # of the feeds page.
                    first_name = user_tuple[0]
                else:
                    jsonify({'error': 'User ID is not found'})
            else:
                jsonify({'error': 'Invalid access token'})

            # Gets the necessary columns from the databases and
            # sends them to feeds.html
            cursor.execute(
                'SELECT posts.user_id, username, content_title, content, \
                        created_at, content_id \
                 FROM posts \
                 JOIN users ON users.user_id = posts.user_id \
                 ORDER BY created_at DESC'
            )
            database_result = cursor.fetchall()

            return render_template('feeds.html', first_name=first_name,
                                   posts=database_result,
                                   post_owner_id=user_id)
        else:
            return redirect(url_for('signin'))

    # If the request method is POST, the user_id will be used to create a post.
    if access_token and request.method == 'POST':
        decoded_token = decode_token(access_token)

        user_id = decoded_token.get('sub')

        # Take the the post content from the client and save to database
        post_data = request.json
        if user_id:
            result = create_post(
                post_data['title'],
                post_data['post'],
                user_id=user_id
            )
            return result
    else:
        return jsonify({'error': 'Permission denied'})


@app.route('/delete', methods=['DELETE'], strict_slashes=False)
def delete():
    """ Deletes the post based on its content_id.
        Gets the content_id from the frontend Javascript.
    """
    content_id = request.form.get('content_id')
    cursor = mysql.connection.cursor()
    cursor.execute('DELETE FROM posts WHERE content_id = %s', (content_id,))
    cursor.connection.commit()
    return jsonify({'mesg': 'Post successfully deleted'})


@app.route('/signout', methods=['POST'], strict_slashes=False)
def signout():
    """ The access token in the cookies will expire when a user accesses
        this route. Sets the date to the past.
    """
    logout_message = 'Successful Sign out'
    response = jsonify({'message': logout_message})

    # Clear the access token cookie setting the date already passed
    response.set_cookie('access_token', '',
                        expires=datetime.now() - timedelta(days=1))

    return response


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
