from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextAreaField, HiddenField
from wtforms.validators import DataRequired, EqualTo, ValidationError, Email, Length
from app.models import Candidate, Campaign

class LoginForm(FlaskForm):
  username = StringField('Username', validators=[DataRequired()])
  password = PasswordField('Password', validators=[DataRequired()])
  remember_me = BooleanField('Remember Me', default=False)
  submit = SubmitField('Log In')

class RegistrationForm(FlaskForm):
  username = StringField('Username', validators=[DataRequired()])
  password = PasswordField('Password', validators=[DataRequired()])
  password2 = PasswordField('Repeat Password', validators=[DataRequired(), EqualTo('password')])
  first_name= StringField('First Name', validators=[DataRequired()])
  middle_name = StringField('Middle Name')
  last_name = StringField('Last Name', validators=[DataRequired()])
  email = StringField('Email', validators=[DataRequired(), Email()])
  email2 = StringField('Repeat Email', validators=[DataRequired(), EqualTo('email')])
  submit = SubmitField('Create Account')

  def validate_username(self, username):
    user = Candidate.query.filter_by(username=username.data).first()
    if user is not None:
      raise ValidationError('Please use a different username.')

  def validate_email(self, email):
    user = Candidate.query.filter_by(email=email.data).first()
    if user is not None:
      raise ValidationError('Please use a different email address.')
