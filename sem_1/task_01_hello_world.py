"""Напишите простое веб-приложение на Flask, которое будет
выводить на экран текст "Hello, World!".


Добавьте две дополнительные страницы в ваше вебприложение:
○ страницу "about"
○ страницу "contact".
"""

from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/about/')
def about():
    return 'About us'


@app.route('/contact/')
def contact():
    return 'Contact us'


if __name__ == '__main__':
    app.run(debug=True)
