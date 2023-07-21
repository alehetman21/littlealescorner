from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import Length, DataRequired, Email, EqualTo, ValidationError
from market.models import User

class RegisterForm(FlaskForm):

    """Important aclaration about name of this method:
        Flask automaticly searches for validation methods
        and validates fields that names are equal to method name after the _
        eg. this method will validate username because after validate_ its called
        username"""
    
    def validate_username(self, user_to_check):
        user = User.query.filter_by(username=user_to_check.data).first()
        if user:
            raise ValidationError('This username is already in use')
        
    def validate_email(self, email_to_check):
        email = User.query.filter_by(email=email_to_check.data).first()
        if email:
            raise ValidationError('This email is already in use')

    username = StringField(label='Username:', validators=[DataRequired(), Length(min=3, max=30)])
    email = StringField(label='Email:', validators=[DataRequired(), Email()])
    password = PasswordField(label='Password:', validators=[DataRequired(), Length(min=8)])
    confirm_password = PasswordField(label='Confirm Password:', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField(label='Sign Up')