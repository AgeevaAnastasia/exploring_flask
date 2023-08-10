# WTForms

from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, PasswordField, EmailField, DateField
from wtforms.validators import DataRequired, Length, EqualTo, Regexp
import re


class RegisterForm(FlaskForm):
    first_name = StringField('First_Name', validators=[DataRequired(), Length(min=2, max=20)])
    second_name = StringField('Second_Name', validators=[DataRequired(), Length(min=3, max=30)])
    birth = DateField('Date')
    sex = SelectField('Sex', choices=[('male', 'мужчина'), ('female', 'женщина')])
    email = EmailField('Email', validators=[DataRequired()])
    password = PasswordField('Password',
                             validators=[DataRequired(), Length(min=8),
                                         Regexp('.*\d+.*[a-zа-я]+.*|.*[a-zа-я]+.*\d+.*', flags=re.IGNORECASE,
                                                message='Поле "Password" должно содержать не менее 8 символов, '
                                                        'включая хотя бы одну букву и одну цифру')])
    confirm_pas = PasswordField('Password', validators=[DataRequired(), EqualTo('password')])
