#!/usr/bin/python3
"""This module defines a function that create a post for a user."""

from flask import jsonify
from models.sign_up import mysql
from datetime import datetime


def create_post(title, post, user_id):
    """Creates a post for a user if the post exists."""
    if post:
        timestamp = datetime.now()
        formatted_timestamp = timestamp.strftime("%Y-%m-%d %H:%M:%S")

        cursor = mysql.connection.cursor()
        query = 'INSERT INTO posts(content_title, content, created_at, \
                                   user_id) VALUES(%s, %s, %s, %s)'
        values = (title, post, formatted_timestamp, user_id)
        cursor.execute(query, values)
        cursor.connection.commit()

        # Return success message
        return jsonify({'msg': 'Post successfully created'})
    else:
        return jsonify({'error': 'Empty string'})
