from flask import render_template, flash, redirect, url_for, request, jsonify
from app import app, db
from deploy.s3 import put


@app.route('/')
@app.route('/index')
def index():
    return 'Hello, world!'


@app.route('/sites/new', methods=["POST"])
def new_site():
    return "TODO"
