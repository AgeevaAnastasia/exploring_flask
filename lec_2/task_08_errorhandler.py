"""Обработка ошибок

Что будет, если пользователь перешёл на несуществующую страницу? Если ничего
не предпринимать, получим следующий вывод:

Not Found
The requested URL was not found on the server. If you entered the URL manually
please check your spelling and try again.


Декоратор errorhandler

Flask предоставляет возможности для обработки ошибок и способен заменить
стандартный текст на симпатичную страницу в стиле вашего сайта.

Обработка ошибок в Flask происходит с помощью декоратора errorhandler(). Этот
декоратор позволяет определить функцию-обработчик ошибок, которая будет
вызываться в случае возникновения ошибки в приложении.

Например, чтобы обработать ошибку 404 (страница не найдена), необходимо
определить функцию, которая будет вызываться при возникновении этой ошибки:"""


import logging
from flask import Flask, render_template, request

app = Flask(__name__)

logger = logging.getLogger(__name__)


@app.route('/')
def index():
    return '<h1>Hello world!</h1>'


@app.errorhandler(404)
def page_not_found(e):
    logger.warning(e)
    context = {
        'title': 'Страница не найдена',
        'url': request.base_url,
    }
    return render_template('404.html', **context), 404


"""В этом примере мы определяем функцию page_not_found(), которая будет
вызываться при ошибке 404. Функция возвращает шаблон HTML страницы 404 и
код ошибки 404. Обратите внимание, что в переменную e попадает текст той самой
ошибки о “Not Found…”. Её мы выводим в логи как предупреждение.
В качестве контекста пробрасываем в шаблон заголовок страницы и адрес, по
которому пытался перейти пользователь. Свойство base_url у объекта request
возвращает тот адрес, который видит пользователь в адресной строке браузера.
Что касается шаблона, возьмём базовый из прошлой лекции.


Шаблон base.html

<!doctype html>
<html lang="ru">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,
initial-scale=1, shrink-to-fit=no">
<link rel="stylesheet" href="/static/css/bootstrap.min.css">
<title>
{% block title %}
Мой сайт
{% endblock %}
</title>
</head>
<body>
<div class="container-fluid">
<ul class="nav nav-pills justify-content-end
align-items-end">
<li class="nav-item"><a href="/main/"
class="nav-link">Основная</a></li>
<li class="nav-item"><a href="/data/"
class="nav-link">Данные</a></li>
</ul>
{% block content %}
Страница не заполнена
{% endblock %}
<div class="row fixed-bottom modal-footer">
<hr>
<p>Все права защищены &copy;</p>
</div>
</div>
<script src="/static/js/bootstrap.bundle.min.js"></script>
</body>
</html>


В этом случае шаблон для ошибки 404 может выглядеть например так:
{% extends 'base.html' %}
{% block title %}
{{ title }}
{% endblock %}

{% block content %}
<div class="row">
<p class="col-12">Мы не нашли страницу: &laquo;{{ url
}}&raquo;.<br>
<a href="{{ url_for('index') }}">Попробуйте вернуться на
главную</a>
</p>
</div>
{% endblock %}


Обратите внимание, что адрес главной страницы указан не явно, а генерируется
через url_for. Подобная практика должна использоваться во всех шаблонах проекта
для удобства масштабирования.
"""


if __name__ == '__main__':
    app.run()
