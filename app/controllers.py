from werkzeug.exceptions import BadRequest
from app import db
from app.models import Candidate, Campaign

USERNAME = "username"
PASSWORD = "password"
EMAIL = "email"
FIRST_NAME = "first_name"
MIDDLE_NAME = "middle_name"
LAST_NAME = "last_name"

expected_register_info = [USERNAME, PASSWORD,
                          EMAIL, FIRST_NAME, MIDDLE_NAME, LAST_NAME]


def register_user(data):

    # Quick/dirty validation for now
    if not all(key in data for key in expected_register_info):
        raise BadRequest("Registration did not include " +
                         ','.join(expected_register_info))

    # Create and setup our candidate
    candidate = Candidate(username=data[USERNAME], email=data[EMAIL],
                          first_name=data[FIRST_NAME], middle_name=data[MIDDLE_NAME],
                          last_name=data[LAST_NAME])
    candidate.set_password(password=data[PASSWORD])

    # Push to db
    db.session.add(candidate)
    db.session.commit()

    return "Created candidate: " + candidate.candidate_id
