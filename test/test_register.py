import os
import sys
import tempfile
import json
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import pytest
import app

from werkzeug.exceptions import BadRequest
from app.controllers import register_user
from itertools import combinations

SQLALCHEMY_DATABASE_URI = "sqlite://" + os.path.join(basedir, 'tmp', 'app.db')
TESTING = True


def setupTest():
    app.app.testing = True
    return app.app.test_client()


def test_regiser_with_no_entries():
    client = setupTest()
    response = client.post("/register")
    assert 400 == response.status_code


def test_register_success():
    client = setupTest()
    data = json.dumps(
        {"username": "jack",
         "password": "foojazzbar00!",
         "email": "spaceis@there.gov",
         "first_name": "John",
         "middle_name": "Fitzgerald",
         "last_name": "Kennedy"})
    response = client.post("/register",
                           content_type="application/json",
                           data=data)
    assert 200 == response.status_code


def test_register_all_entries():
    """ 
    Tests every possible combination of "good" entries to prove 
    that the minimum required parameters are truly the minimum 
    required parameters. (IE: There's no smaller subset where  
    the request succeeds)
    """

    # The good stuff
    required_params = [
        ("username", "jack"),
        ("password", "because-they-are-hard"),
        ("email", "spaceis@there.gov"),
        ("first_name", "John"),
        ("middle_name", "Fitzgerald"),
        ("last_name", "Kennedy")
    ]

    all_combos = [list(combinations(required_params, i))
                  for i in range(len(required_params))]

    for combos in all_combos:
        for combo in combos:

            # Only the full list shall succeed
            if (len(combo) != len(required_params)):

                # Check that we're raising something
                with pytest.raises(BadRequest) as excinfo:
                    register_user(combo)
            else:
                register_user(combo)  # if this errors, the test fails

    # You can assume if we got here and there's no error, then we did it


test_register_all_entries()
