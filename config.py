import os

class MyConfig(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or os.urandom(12).hex()