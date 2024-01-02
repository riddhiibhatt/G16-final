import os


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or b'\x84\x98\r\xa5\xb7\xe6Sv\x02\x9fL3@\xf0\x15\x01'