import os

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'vjrwr1r!S0r6q0jdf9@?1oKYH4j7)s'
