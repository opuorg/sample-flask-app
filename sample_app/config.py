import os

class Config:
    DATABASE_USER = os.environ.get('DATABASE_USER')
    DATABASE_PASSWORD = os.environ.get('DATABASE_PASSWORD')
    DATABASE_NAME = os.environ.get('DATABASE_NAME')
    DATABASE_HOST = os.environ.get('DATABASE_HOST')
    