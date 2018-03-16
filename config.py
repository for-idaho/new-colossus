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
  # Configure application to store JWTs in cookies
  JWT_TOKEN_LOCATION = ['cookies']

  # Only allow JWT cookies to be sent over https. In production, this
  # should likely be True
  JWT_COOKIE_SECURE = False if os.environ.get('STAGE') == 'DEV' else True

  # Set the cookie paths, so that you are only sending your access token
  # cookie to the access endpoints, and only sending your refresh token
  # to the refresh endpoint. Technically this is optional, but it is in
  # your best interest to not send additional cookies in the request if
  # they aren't needed.
  JWT_ACCESS_COOKIE_PATH = '/api/'
  JWT_REFRESH_COOKIE_PATH = '/token/refresh'

  # Enable csrf double submit protection. See this for a thorough
  # explanation: http://www.redotheweb.com/2015/11/09/api-security.html
  JWT_COOKIE_CSRF_PROTECT = True

  JWT_SECRET_KEY = os.environ.get('SECRET_KEY')