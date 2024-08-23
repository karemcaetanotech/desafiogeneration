import os

class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'mysql://root:curs@123@127.0.0.1/school_db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
