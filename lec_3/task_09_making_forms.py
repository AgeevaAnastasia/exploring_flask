"""Создание форм в WTForms

WTForms — это библиотека Python, которая позволяет создавать HTML-формы, а
также проводить их валидацию. Flask-WTF использует WTForms для создания форм.


Определение классов форм

Для создания формы с помощью Flask-WTF необходимо определить класс формы,
который наследуется от класса FlaskForm. Каждое поле формы определяется как
экземпляр класса, который наследуется от класса Field."""


from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
    username = StringField('Username',
    validators=[DataRequired()])
    password = PasswordField('Password',
    validators=[DataRequired()])


"""В данном примере определен класс LoginForm, который наследуется от FlaskForm.
Внутри класса определены два поля: username и password. Поле username является
строковым полем, а поле password — полем для ввода пароля. Оба поля
обязательны для заполнения, так как им передан валидатор DataRequired.


Описание полей форм

WTForms предоставляет множество типов полей для формы. Вот некоторые из них:

● StringField — строковое поле для ввода текста;
● IntegerField — числовое поле для ввода целочисленных значений;
● FloatField — числовое поле для ввода дробных значений;
● BooleanField — чекбокс;
● SelectField — выпадающий список;
● DateField — поле для ввода даты;
● FileField — поле для загрузки файла.


Рассмотрим ещё один пример создания форм:"""

from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SelectField
from wtforms.validators import DataRequired


class RegisterForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    age = IntegerField('Age', validators=[DataRequired()])
    gender = SelectField('Gender', choices=[('male', 'Мужчина'), ('female', 'Женщина')])


"""В данном примере определен класс RegisterForm, который наследуется от
FlaskForm. Внутри класса определены три поля: name, age и gender. Поле name
является строковым полем, поле age — числовым, а поле gender — выпадающим
списком. В списке выбора есть две опции: male и female.
"""