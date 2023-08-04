"""➢Разделение проекта на отдельные компоненты

Чтобы Flask проект не превратился один файл гигантского размера, вынесем работу
с БД в отдельный файл models.py.

На текущем этапе в нём будут следующие строки:"""

from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

"""Внутри основного файла проекта оставим следующий код:

from flask import Flask
from flask_lesson_3.models import db
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydatabase.db'
db.init_app(app)



@app.route('/')
def index():
    return 'Hi!'


if __name__ == '__main__':
    app.run(debug=True)


🔥 Важно! Теперь класс не получает приложение Flask app при
инициализации. Для инициализации баз данных необходимо выполнить
строку db.init_app(app)"""