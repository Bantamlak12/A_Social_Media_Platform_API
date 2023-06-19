from flask import request, jsonify, render_template
from models.register import register_user, app


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
        return jsonify({'message': result})

    return render_template('register.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
