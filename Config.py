import os

class Config:
    SECRET_KEY = '04f541fa5cdb247004c31335b8df4c32a0b8bab128f4a54a'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    ADMIN_PASSWORD_HASH = '$2b$12$dWbE2sV2WOhjHBqVATAiE./RxsYjw0gr5yCOXLUcAUxpaCvhES8EO'