-- Create  a databasea_social_media_platform_api
CREATE DATABASE IF NOT EXISTS a_social_media_platform_api;
USE a_social_media_platform_api;

-- Create a users table
CREATE TABLE IF NOT EXISTS users (
    user_id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    username VARCHAR(50) NOT NULL,
    email VARCHAR(50) NOT NULL,
    password VARCHAR(255) NOT NULL
);

-- Create a posts table
CREATE TABLE IF NOT EXISTS posts (
    content_id INT AUTO_INCREMENT PRIMARY KEY,
    content_title VARCHAR(255) NOT NULL,
    content TEXT NOT NULL,
    created_at DATETIME NOT NULL
);

-- Create Relationship
ALTER TABLE posts ADD COLUMN user_id INT NOT NULL;
ALTER TABLE posts ADD CONSTRAINT fk_user_id FOREIGN KEY (user_id) REFERENCES users(user_id);
