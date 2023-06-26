from flask import request, jsonify, render_template, redirect, url_for
from models.register import register_user, app, mysql
from models.login import login_user
from models.create_post import create_post
from flask_jwt_extended import decode_token
from datetime import datetime, timedelta


@app.route('/', methods=['GET'], strict_slashes=False)
def home():
    # Home page
    return render_template('home.html')


@app.route('/register', methods=['GET', 'POST'], strict_slashes=False)
def register():
    # Get user input from request body
    if request.method == 'POST':
        data = request.json

        result = register_user(
            data['firstName'],
            data['lastName'],
            data['username'],
            data['email'],
            data['password'],
            data['confirmPassword']
        )
        # Check the registration result
        return result

    return render_template('register.html')


@app.route('/login', methods=['GET', 'POST'], strict_slashes=False)
def login():
    if request.method == 'POST':
        data = request.json
        result = login_user(
            data['username'],
            data['password']
        )
        # Check the registration resuls
        if request.get_json('signin_username_error') or request.get_json('signin_password_error'):
            return result

    return render_template('login.html')


@app.route('/feeds', methods=['GET', 'POST'], strict_slashes=False)
def feeds():
    access_token = request.cookies.get('access_token')

    if request.method == 'GET':
        # If there is access token, redirect to the feeds page else to login page
        if access_token:
            decoded_token = decode_token(access_token)

            # Validate the token
            if decoded_token:
                user_id = decoded_token.get('sub')
                # Check if the user_id is in the decoded token
                if user_id:
                    cursor = mysql.connection.cursor()
                    cursor.execute(
                        'SELECT first_name FROM users WHERE user_id = %s', (
                            user_id,)
                    )
                    user_tuple = cursor.fetchone()
                    first_name = user_tuple[0]
                else:
                    jsonify({'error': 'User ID is not found'})
            else:
                jsonify({'error': 'Invalid access token'})

            cursor = mysql.connection.cursor()
            cursor.execute(
                'SELECT posts.user_id, username, content_title, content, created_at, content_id FROM posts JOIN users ON users.user_id = posts.user_id ORDER BY created_at DESC'
            )
            database_result = cursor.fetchall()

            # posts = jsonify({'posts': database_result})
            # return posts

            return render_template('feeds.html', first_name=first_name, posts=database_result, post_owner_id=user_id)
        else:
            return redirect(url_for('login'))

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
    """Delete the post based on its content id"""
    content_id = request.form.get('content_id')
    cursor = mysql.connection.cursor()
    cursor.execute('DELETE FROM posts WHERE content_id = %s', (content_id,))
    cursor.connection.commit()
    return jsonify({'mesg': 'Post successfully deleted'})


@app.route('/logout', methods=['POST'], strict_slashes=False)
def logout():
    logout_message = 'Successful Sign out'
    response = jsonify({'message': logout_message})

    # Clear the access token cookie setting the date already passed
    response.set_cookie('access_token', '',
                        expires=datetime.now() - timedelta(days=1))

    return response


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
