from flask import render_template, flash, redirect, url_for, request, jsonify
from app import app, db
from app.controllers import register_user


@app.route('/')
@app.route('/index')
def index():
    return 'Hello, world!'


@app.route('/register', methods=['POST'])
def register():
    user = request.json
    return register_user(user)
