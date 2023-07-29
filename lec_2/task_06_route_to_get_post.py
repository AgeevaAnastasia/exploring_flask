"""Замена route на get и post

Рассмотренный выше пример функции submit можно записать иначе."""

from flask import Flask, render_template, url_for, request

app = Flask(__name__)


@app.get('/submit')
def submit_get():
    return render_template('form.html')


@app.post('/submit')
def submit_post():
    name = request.form.get('name')
    return f'Hello {name}!'


if __name__ == '__main__':
    app.run()


"""Вместо одной функции, которая обрабатывает и get и post запросы были созданы
две. В первой использован декоратор get и она отвечает за отрисовки формы.
Вторая функция имеет декоратор post с тем же самым аргументом, что и у get.
Внутри читаем данные формы без лишних проверок метода запроса.
"""