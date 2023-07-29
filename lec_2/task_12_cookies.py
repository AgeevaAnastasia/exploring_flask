"""Хранение данных

В финале лекции рассмотрим возможность сохранения данных между запросами.
Работа с cookie файлами в Flask


Cookie файлы — это небольшие текстовые файлы, которые хранятся в браузере
пользователя и используются для хранения информации о пользователе и его
предпочтениях на сайте. В Flask, работа с cookie файлами очень проста и может
быть выполнена с помощью самого фреймворка, без установки дополнительных
модулей.

Для работы с cookie файлами, необходимо импортировать модуль Flask и объект
request, который позволяет получить доступ к cookie файлам. Подобное мы
проделывали несколько раз за лекцию. Разберем куки на примере"""

from flask import Flask, request, make_response

app = Flask(__name__)


@app.route('/')
def index():
    # устанавливаем cookie
    response = make_response("Cookie установлен")
    response.set_cookie('username', 'admin')
    return response


@app.route('/getcookie/')
def get_cookies():
    # получаем значение cookie
    name = request.cookies.get('username')
    return f"Значение cookie: {name}"


"""Мы устанавливаем значение cookie файла с ключом "username" и значением
"admin" в функции index(). Затем мы получаем значение cookie файла с ключом
"username" в функции get_cookies() и выводим его на экран.


Создание ответа

Несколько слов о функции make_response(). Во всех прошлых примерах мы
возвращали из view функций обычный текст, текст форматированный как HTML,
динамически сгенерированные страницы через render_template и даже запросы
переадресации благодаря функциям redirect и url_for. Каждый раз Flask неявно
формировал объект ответа - response. Если же мы хотим внести изменения в ответ,
можно воспользоваться функцией make_response.
Изменим прошлый пример. Для начала создадим шаблон main.html

{% extends 'base.html' %}
{% block title %}
{{ super() }} - {{ title }}
{% endblock %}
{% block content %}
<div class="row">
<h1 class="col-12 col-md-6 display-2">Привет, меня зовут
{{ name }}</h1>
<img src="/static/image/foto.jpg" class="col-12 col-md-6
img-fluid rounded-circle" alt="Моё фото">
</div>
{% endblock %}

Шаблон принимает заголовок и имя пользователя. Для отрисовки он расширяет
базовый шаблон. Ничего нового и никаких упоминаний “печенек”.
А теперь модифицируем представление"""

@app.route('/')
def index():
    context = {
        'title': 'Главная',
        'name': 'Харитон'
    }
    response = make_response(render_template('main.html', **context))
    response.headers['new_head'] = 'New value'
    response.set_cookie('username', context['name'])
    return response


"""Используя render_template пробрасываем контекст в шаблон, но не возвращаем его,
а передаём результат в функцию make_response. Ответ сформирован, но мы можем
внести в него изменения перед возвратом. В нашем примере добавили в заголовки
пару ключ-значение и установили куки для имени пользователя.


🔥 Важно! Не путайте заголовки ответа и содержимое блок head в теле ответа.

"""


if __name__ == '__main__':
    app.run()
