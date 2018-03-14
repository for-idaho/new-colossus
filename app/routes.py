from flask import render_template, flash, redirect, url_for, request, jsonify
from app import app, db


@app.route('/')
@app.route('/index')
def index():
    return 'Hello, world!'
