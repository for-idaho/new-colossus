from flask import render_template, flash, redirect, url_for, request, jsonify
from app import app, db
from flask_login import current_user, login_user, logout_user, login_required
import uuid
from .forms import LoginForm, RegistrationForm
from werkzeug.urls import url_parse
from app.models import Candidate, Campaign


@app.route('/')
@app.route('/index')
@login_required
def index():
  return render_template('index.html',
                         title='Home',
                         user=current_user)


@app.route('/login', methods=['GET','POST'])
def login():
  if current_user.is_authenticated:
    return redirect(url_for('index'))
  form = LoginForm()
  if form.validate_on_submit():
    user = Candidate.query.filter_by(username=form.username.data).first()
    if user is None or not user.check_password(form.password.data):
      flash('Invalid username or password')
      return redirect(url_for('login'))
    login_user(user, remember=form.remember_me.data)
    next_page = request.args.get('next')
    if not next_page or url_parse(next_page).netloc != '':
      next_page = url_for('index')
    return redirect(next_page)
  return render_template('login.html',
                        title='Sign In',
                        form=form)

@app.route('/logout')
def logout():
  logout_user()
  return redirect(url_for('index'))

@app.route('/register', methods=['GET', 'POST'])
def register():
  if current_user.is_authenticated:
    return redirect(url_for('index'))
  form = RegistrationForm()
  if form.validate_on_submit():
    candidate = Candidate(candidate_id=uuid.uuid4().hex,
                     username=form.username.data,
                     email=form.email.data,
                     first_name=form.first_name.data,
                     middle_name=form.middle_name.data,
                     last_name=form.last_name.data)
    candidate.set_password(form.password.data)
    db.session.add(candidate)
    db.session.commit()
    flash('Congratulations! You are now a registered user!')
    return redirect(url_for('login'))
  return render_template('register.html', title='Register', form=form)

@app.route('/campaigns/<username>')
@login_required
def campaigns(username):
  return "Campaigns!"