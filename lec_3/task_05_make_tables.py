"""➢Создание таблиц в базе данных

Остался финальный этап. Напишим функцию, которая создаст таблицы через
консольную команду. Заполняем основной файл проекта"""

...
from flask_lesson_3.models import db, User, Post, Comment

from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()


@app.cli.command("init-db")
def init_db():
db.create_all()
print('OK')
...


"""Из models импортировали все созданные классы таблиц. Без этого импорта
функция create_all может не увидеть какие таблицу необходимо создать.
Далее создали функцию, которая будет вызвана командой в консоли:
flask init-db

🔥 Внимание! Если команда в консоли выдает ошибку, проверьте что у вас
есть wsgi.py файл в корневой директории проекта и он верно работает.
Например его код может быть таким:

from flask_lesson_3.app_01 import app

if __name__ == '__main__':
    app.run(debug=True)
    
    
Мы рассмотрели основные аспекты создания моделей в Flask-SQLAlchemy. Были
описаны классы моделей, поля моделей и создание связей между моделями.



Работа с данными

После определения моделей в Flask-SQLAlchemy можно начать работу с данными в
базе данных. Давайте рассмотрим основные методы для создания, изменения и
удаления записей, а также получения данных из базы данных и их фильтрацию.


➢Создание записей

Для создания новой записи в базе данных необходимо создать объект модели и
добавить его в сессию базы данных. После этого нужно вызвать метод commit() для
сохранения изменений.
..."""


@app.cli.command("add-john")
def add_user():
    user = User(username='john', email='john@example.com')
    db.session.add(user)
    db.session.commit()
    print('John add in DB!')


"""...

В этом примере создается новый объект модели User с именем пользователя "john"
и электронной почтой "john@example.com". Затем объект добавляется в сессию
базы данных и сохраняется с помощью метода commit().

Как вы уже догадались для выполнения функции необходимо выполнить в консоли
команду flask add-john


➢Изменение записей

Для изменения существующей записи нужно получить ее из базы данных, изменить
нужные поля и вызвать метод commit().

..."""


@app.cli.command("edit-john")
def edit_user():
    user = User.query.filter_by(username='john').first()
    user.email = 'new_email@example.com'
    db.session.commit()
    print('Edit John mail in DB!')

"""
...
В этом примере получаем объект модели User по имени пользователя "john",
изменяем его электронную почту на "new_email@example.com" и сохраняем
изменения с помощью метода commit().

🔥 Внимание! Если бы база данных позволяла хранить несколько
пользователей с одинаковыми username, в переменную user попал бы один
пользователь благодаря методу first().


➢Удаление записей

Для удаления записи нужно получить ее из базы данных, вызвать метод delete() и
затем вызвать метод commit().
..."""


@app.cli.command("del-john")
def del_user():
    user = User.query.filter_by(username='john').first()
    db.session.delete(user)
    db.session.commit()
    print('Delete John from DB!')


"""...

В этом примере получаем объект модели User по имени пользователя "john",
удаляем его из базы данных с помощью метода delete() и сохраняем изменения с
помощью метода commit().
"""