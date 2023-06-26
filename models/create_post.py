from flask import jsonify
from models.register import mysql
from datetime import datetime


def create_post(title, post, user_id):
    # Create a database connection if the post exists
    if post:
        timestamp = datetime.now()
        formatted_timestamp = timestamp.strftime("%Y-%m-%d %H:%M:%S")

        # return jsonify({'content_title': title, 'content': post,
        #                 'created_at': formatted_timestamp, 'user_id': user_id})

        cursor = mysql.connection.cursor()
        cursor.execute(
            'INSERT INTO posts (content_title, content, created_at, user_id) VALUES (%s, %s, %s, %s)', (
                title, post, formatted_timestamp, user_id)
        )
        cursor.connection.commit()

        # Return success message
        return jsonify({'msg': 'Post successfully created'})
    else:
        return jsonify({'error': 'Empty string'})
