from flask import render_template, flash, redirect, url_for, request, jsonify
from flask_jwt import JWT, jwt_required, current_identity
from app import app, db
from app.models import Candidate


def authenticate(username, password):
    user = User.query.filter_by(username=username)
    if user is not None and user.check_password(password):
        return user

@app.route('/')
@app.route('/index')
def index():
    return 'Hello, world!'


@app.route('/register', methods=['POST'])
def register():
    data = request.body

@app.route('/test_protected'):
@jwt_required
def test_protected():
    return '{}'.format(current_identity)
