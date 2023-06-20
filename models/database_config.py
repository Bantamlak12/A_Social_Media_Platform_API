from os import getenv

# Database configuration
MYSQL_HOST = getenv('MYSQL_HOST')
MYSQL_USER = getenv('MYSQL_USER')
MYSQL_PASSWORD = getenv('MYSQL_PASSWORD')
MYSQL_DB = getenv('MYSQL_DB')
JWT_SECRET_KEY = getenv('JWT_SECRET_KEY')
