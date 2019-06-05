import os

SECRET_KEY = 'teste'

UPLOAD_PATH = os.path.dirname(os.path.abspath(__file__)) + '/uploads'

MYSQL_HOST = 'localhost'
MYSQL_PASSWORD = 'admin'
MYSQL_DB = 'jogoteca'
MYSQL_USER = 'root'
MYSQL_PORT = 3306