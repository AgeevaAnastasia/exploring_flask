"""Написать функцию, которая будет выводить на экран HTML
страницу с заголовком "Моя первая HTML страница" и
абзацем "Привет, мир!".
"""

from flask import Flask

app = Flask(__name__)

html = """<h1> Моя первая страница </h1> <br><br>
Привет, Мир"""


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/hello/')
def about():
    return html


if __name__ == '__main__':
    app.run(debug=True)
