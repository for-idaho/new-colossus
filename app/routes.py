from flask import render_template, flash, redirect, url_for, request, jsonify
from app import app, db
from deploy.s3 import create_bucket
import json
from jsonschema import validate
import time


@app.route('/')
@app.route('/index')
def index():
    return 'Hello, world!'


@app.route('/sites/new', methods=["POST"])
def new_site():
    schema = {
        "files": {
            "index": {"type": "string"},
            "error": {"type": "string"}
        }
    }

    data = request.get_json()
    validate(data, schema)

    files = data['files']

    # TODO: Change this to be the JWT user when auth is working
    # timestamp right now for easy-ish testing
    name_TODO_CHANGE_ME_TO_JWT_USER = str(time.time())

    return create_bucket(name_TODO_CHANGE_ME_TO_JWT_USER,
                         files['index'], files['error'])
