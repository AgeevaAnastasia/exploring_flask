"""Генерация пути к статике

Один из распространённых способов использования url_for является указание пути
к файлам статики внутри шаблонов.

Рассмотрим следующее представление"""

from flask import Flask, render_template, url_for

app = Flask(__name__)


@app.route('/about/')
def about():
    context = {
        'title': 'Обо мне',
        'name': 'Харитон',
    }
    return render_template('about.html', **context)


if __name__ == '__main__':
    app.run()

"""На прошлом занятии мы выводили примерно такой шаблон
<!doctype html>
<html lang="ru">
<head>
<meta charset="utf-8">
<link rel="stylesheet" href="/static/css/bootstrap.min.css">
<title>{{ title }}</title>
</head>
<body>
<h1 class="text-monospace">Привет, меня зовут {{ name }}</h1>
5
<img src="/static/image/foto.jpg" alt="Моё фото" width="300">
<p class="text-body text-justify">Lorem ipsum dolor sit amet, consectetur adipisicing
elit. Ad cupiditate doloribus ducimus nam provident quo similique! Accusantium
aperiam fugit magnam quas reprehenderit sapiente temporibus voluptatum!</p>
<p class="alert-dark">Все права защищены &copy;</p>
<script src="/static/js/bootstrap.bundle.min.js"></script>
</body>
</html>
В качестве статики тут прописаны стили и скрипты bootstrap, а также изображение
из каталога image. Исправим эти три строки шаблона используя url_for
...
<link rel="stylesheet" href="{{ url_for('static', filename='css/bootstrap.min.css') }}">
...
<img src="{{ url_for('static', filename='image/foto.jpg') }}" alt="Моё фото"
width="300">
...
<script src="{{ url_for('static', filename='js/bootstrap.bundle.min.js') }}"></script>
...


Чтобы сгенерировать URL-адреса для статических файлов, необходимо
использовать специальное имя “static” в качестве первого параметра, а по ключу
filename передать путь до файла внутри каталога static.


💡 Внимание! Не стоит создавать view функцию с именем static.

🔥 Важно! Во время разработки приложения за раздачу статики отвечает
Flask. При запуске рабочего проекта статику раздаёт веб-сервер, а не Flask.

Для этого надо настроит сервер. Изменять шаблоны Flask не нужно, url_for
сгенерировала необходимые пути.
"""
