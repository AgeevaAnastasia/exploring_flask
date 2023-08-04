"""➢Получение данных из базы данных

Для получения данных из базы данных необходимо использовать метод query()
модели. Этот метод возвращает объект запроса, который можно дополнить
фильтрами и другими параметрами.

...
@app.route('/users/')
def all_users():
    users = User.query.all()
    context = {'users': users}
    return render_template('users.html', **context)
...

В этом примере получаем все объекты модели User из базы данных с помощью
метода all(). Пробросим их в шаблон, где выводим имена пользователей и
электронные адреса.

{% extends 'base.html' %}
{% block title %}
{{ super() }} - {{ title }}
{% endblock %}
{% block content %}
<div class="row">
{% for user in users %}
<p class="col-12 col-md-6">Имя пользователя: {{
user.username }}<br>
Email пользователя: {{ user.email }}</p>
{% endfor %}
</div>
{% endblock %}


➢Фильтрация данных

Для фильтрации данных можно использовать метод filter() объекта запроса. Этот
метод принимает условия фильтрации в виде аргументов или объектов-атрибутов
модели.

...
@app.route('/users/<username>/')
def users_by_username(username):
    users = User.query.filter(User.username == username).all()
    context = {'users': users}
    return render_template('users.html', **context)
...

В этом примере получаем все объекты модели User из базы данных, у которых имя
пользователя равно username из строки запроса, с помощью метода filter() и
выводим их имена пользователей и электронные адреса используя прежний
шаблон.


Рассмотрим ещё один вариант фильтрации данных

@app.route('/posts/author/<int:user_id>/')
def get_posts_by_author(user_id):
    posts = Post.query.filter_by(author_id=user_id).all()
    if posts:
        return jsonify([{'id': post.id, 'title': post.title, 'content': post.content, 'created_at': post.created_at} for post in posts])
    else:
        return jsonify({'error': 'Posts not found'})

Мы создаем маршрут /posts/author/<int:user_id>, который принимает ID
пользователя в качестве параметра. Внутри маршрута мы используем метод
filter_by для фильтрации постов по ID автора и метод all для получения всех
найденных постов. Если посты найдены, мы возвращаем их данные в формате
JSON, иначе возвращаем ошибку.


🔥 Внимание! Для того, чтобы вернуть JSON объект используется функция
jsonify. Её необходимо импортировать из модуля Flask перед
использованием.


Финальный пример фильтрации данных

@app.route('/posts/last-week/')
def get_posts_last_week():
    date = datetime.utcnow() - timedelta(days=7)
    posts = Post.query.filter(Post.created_at >= date).all()
    if posts:
        return jsonify([{'id': post.id, 'title': post.title, 'content': post.content, 'created_at': post.created_at} for post in posts])
    else:
        return jsonify({'error': 'Posts not found'})


Создаем маршрут /posts/last-week, который возвращает все посты, созданные за
последнюю неделю. Внутри маршрута мы используем модуль datetime для
вычисления даты, которая была неделю назад, и метод filter для фильтрации постов
по дате создания. Если посты найдены, мы возвращаем их данные в формате JSON,
иначе возвращаем ошибку.


🔥 Важно! Для работы без ошибок, добавьте строку импорта в начале файла:

from datetime import datetime, timedelta


Заключение по работе с Flask-SQLAlchemy

Flask-SQLAlchemy — это мощный инструмент для работы с базами данных в
приложениях Flask. Он предоставляет простой и удобный интерфейс для создания
моделей, выполнения запросов и управления данными.
Мы рассмотрели основные функции Flask-SQLAlchemy, такие как создание моделей,
работу с данными, получение и фильтрацию данных. Мы также рассмотрели
создание запросов к базе данных с помощью SQLAlchemy ORM.
Flask-SQLAlchemy позволяет разработчикам быстро и легко создавать и
поддерживать базы данных в своих приложениях Flask. Он также обеспечивает
безопасность и надежность работы с данными.
"""