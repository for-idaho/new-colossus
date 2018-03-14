import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
  def __init__(self):
    if 'SECRET_KEY' in os.environ:
      self.SECRET_KEY = os.environ.get('SECRET_KEY')
    else:
      raise Exception("Must set environment variable SECRET_KEY")
  SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
    'sqlite:///' + os.path.join(basedir, 'app.db')
  SQLALCHEMY_TRACK_MODIFICATIONS = False
