import os

SECRET_KEY = 'Renat12345'


SQLALCHEMY_DATABASE_URI = f'mysql+mysqlconnector://user1:Qwerty1234@rc1b-637htu11i17n18re.mdb.yandexcloud.net/db1'

SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_ECHO = True

UPLOAD_FOLDER = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'media', 'images')

ADMIN_ROLE_ID = 1
MODERATOR_ROLE_ID = 2
USER_ROLE_ID = 3
