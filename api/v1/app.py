from flask import request, jsonify, render_template, redirect, url_for
from models.register import register_user, app
from models.login import login_user


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

    # If there is access token, redirect to the feeds page else to login page
    if access_token:
        return render_template('feeds.html')
    return redirect(url_for('login'))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
