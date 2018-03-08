from app import db, login
import datetime
from hashlib import md5
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin


class Candidate(UserMixin, db.Model):
  candidate_id = db.Column(db.String(32), primary_key=True)
  username = db.Column(db.String(32), index=True, unique=True)
  email = db.Column(db.String(128), index=True, unique=True)
  password_hash = db.Column(db.String(128))
  first_name = db.Column(db.String(64))
  middle_name = db.Column(db.String(64))
  last_name = db.Column(db.String(64), index=True)
  create_timestamp = db.Column(db.DateTime, default=datetime.datetime.utcnow)
  last_seen = db.Column(db.DateTime, default=datetime.datetime.utcnow)

  def __repr__(self):
    return '<Candidate {}>'.format(self.username)
  def set_password(self, password):
    self.password_hash = generate_password_hash(password)
  def check_password(self, password):
    return check_password_hash(self.password_hash, password)
  def get_id(self):
    return self.user_id

@login.user_loader
def load_user(user_id):
  return Candidate.query.get(user_id)


class Campaign(db.Model):
  campaign_id = db.Column(db.String(32), primary_key=True)
  candidate_id = db.Column(db.String(32), db.ForeignKey('candidate.candidate_id'))
  state = db.Column(db.String(32))
  district = db.Column(db.String(32))
  office = db.Column(db.String(64))
  year = db.Column(db.Integer)
  create_timestamp = db.Column(db.DateTime, default=datetime.datetime.utcnow)

  def __repr__(self):
    return '<Campaign: Candidate {} office {} year {}>'.format(
        self.candidate_id, self.office, self.year)
