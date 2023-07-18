# A Social Media Platform API

This is a social media platform API built using Flask, MySQL, and JWT authentication. It provides endpoints for user registration, sign-in, sign-out, post creation, and post deletion. The API allows users to interact with the platform by creating posts, and accessing their feeds.

[Link to the deployed site](https://www.bante.tech)

[Link to blog post](https://bantamlak-tilahun.hashnode.dev/building-a-user-focused-social-media-platform-personal-journey)

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)
- [Technologies Used](#technologies-used)
- [Contributing](#contributing)
- [Related Projects](#related-projects)
- [License](#license)
- [Author](#author)

## Features

- `User Registration`: Users can create a new account by providing their personal information.
- `User sign-in`: Registered users can sign in to access their account and perform actions.
- `User sign-out`: Users can log out of their account to end their session.
- `Post Creation`: signed-in users can create new posts by providing the post content.
- `Post Deletion`: Users can delete their own posts.
- `Responsive UI`: Both mobile and desktop responsive user interface.

## Installation

1. Clone the repository:

   ```shell
   git clone https://github.com/Bantamlak12/social-media-platform-api.git
   ```

2. Install the dependencies:

   ```shell
   cd social-media-platform-api
   pip install -r requirements.txt
   ```

3. Set up the database:

   - If your database is already set up, run

   ```shell
   cat setup_mysql_database.sql | mysql -uroot -p
   ```

4. Export all environmental variables:

   ```shell
   export FLASK_ENV=development \
   MYSQL_HOST=localhost \
   MYSQL_USER=root \
   MYSQL_PASSWORD=******* \
   MYSQL_DB=a_social_media_platform_api \
   JWT_SECRET_KEY=d20cfa4b6040a44bc0810fa58d1fe5097239531ca1e835f399c21aabd9e92e01
   ```

5. Run the application:

   ```shell
   python3 -m api.v1.app
   ```

   Note: While running the app, you should be in the root directory of `social-media-platform-api`.

The API will be accessible at `http://127.0.0.1:5000`.

## Usage

To use the API, you can make HTTP requests to the provided endpoints using a tool like `curl` or an API testing tool like Postman.

For instance, To register a user:

```shell
curl -X POST http://0.0.0.0:5000/signup \
-H "Content-Type: application/json" \
-d '{ "firstName": "John", "lastName": "Smith", "username": "John", "email": "john12@gmail.com.com", "password": "password123", "confirmPassword": "password123"}'
```

The output looks like:

```
{"success_msg":"Successfully Signed up!"}
```

To sign in:

```shell
curl -X POST http://0.0.0.0:5000/signin -H "Content-Type: application/json" -d '{ "username": "John", "password": "password123"}'
```

The output looks like:

```
{"success":"Signed in Successfully"}
```

Refer to the [API Endpoints](#api-endpoints) section below for detailed information on each endpoint and their usage.

## API Endpoints

- `['GET'] /home`: Home page
- `['GET', 'POST'] /signup`: Register a new user.
- `['GET', 'POST'] /signin`: Sign in an existing user.
- `['POST'] /signout`: Sign out the current user.
- `['GET', 'POST'] /feeds`: Create a new post and interact with other user's posts.
- `['DELETE'] /delete`: Delete a post.

## Technologies Used

- `Flask`: Web framework used to build the API.
- `MySQL`: Database management system for storing user and post data.
- `JWT`: JSON Web Tokens used for user authentication and authorization.
- `Gunicorn`: WSGI server used to run the application.

## Contributing

Contributions to this project are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.

## Related Projects

[AirBnB Clone](https://github.com/Bantamlak12/AirBnB_clone)

[AirBnB_clone_v2](https://github.com/Bantamlak12/AirBnB_clone_v2)

[AirBnB_clone_v3](https://github.com/Bantamlak12/AirBnB_clone_v3)

[AirBnB_clone_v4](https://github.com/Bantamlak12/AirBnB_clone_v4)

## License

This project is licensed under the [MIT License](https://github.com/git/git-scm.com/blob/main/MIT-LICENSE.txt).

## Author

Bantamlak Tilahun <bantamlak29@gmail.com>
| [Twitter](https://twitter.com/Bantamlak_T)
| [LinkedIn](https://www.linkedin.com/in/bantamlak-tilahun)
