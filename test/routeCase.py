import os
import sys
from flask_testing import TestCase

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app import create_app, db


class RouteCase(TestCase):
    SQLALCHEMY_DATABASE_URI = "sqlite://" + \
        os.path.join(basedir, 'tmp', 'app.db')
    TESTING = True

    def create_app(self):

        # pass in test configuration
        return create_app(self)

    def setUp(self):

        db.create_all()

    def tearDown(self):

        db.session.remove()
        db.drop_all()
