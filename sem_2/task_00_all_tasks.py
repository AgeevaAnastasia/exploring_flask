from pathlib import PurePath, Path
from flask import Flask, request, render_template, abort, redirect, url_for, flash
from markupsafe import escape
from werkzeug.utils import secure_filename

app = Flask(__name__)

app.secret_key = b'ddb4b937bfc272f7139dea217630a099cd148cc1bacec6e324d9beb0b952775a'


# task_01_pushme_button
@app.route('/')
def index():
    return render_template('index.html')


@app.route('/hello/')
def hello1():
    return 'Привет, незнакомец!'


@app.route('/uploads', methods=['GET', 'POST'])
def uploads():
    if request.method == 'POST':
        file = request.files.get('file')
        file_name = secure_filename(file.filename)
        file.save(PurePath.joinpath(Path.cwd(), 'static/image', file_name))
        return render_template('image.html', file_name=file_name)
    return render_template('uploads.html')


users = {'admin': '000', 'user1': '111', 'user2': '222', 'user3': '333'}


@app.route('/login/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        if (username, password) in users.items():
            return f'Вы вошли! Привет, {escape(username)}'
        return f'Неверный логин {escape(username)} или пароль'
    return render_template('login.html')


@app.route('/text/', methods=['GET', 'POST'])
def text():
    if request.method == 'POST':
        text = request.form.get('text').split()
        words = len(text)
        return f'Слов в вашем тексте: {words}'
    return render_template('text.html')


@app.route('/calk/', methods=['GET', 'POST'])
def calk():
    if request.method == 'POST':
        num1 = int(request.form.get('num1'))
        num2 = int(request.form.get('num2'))
        op = request.form.get('operation')
        if op == 'add':
            return f'{num1} + {num2} = {num1 + num2}'
        elif op == 'subtract':
            return f'{num1} - {num2} = {num1 - num2}'
        elif op == 'multiply':
            return f'{num1} * {num2} = {num1 * num2}'
        else:
            return f'{num1} / {num2} = {num1 / num2}'
    return render_template('calk.html')


@app.route('/age/', methods=['GET', 'POST'])
def age():
    if request.method == 'POST':
        name = request.form.get('username')
        user_age = int(request.form.get('age'))
        if user_age < 18:
            return abort(403)
        return f'Вы вошли. Добро пожаловать, {escape(name)}!'
    return render_template('age.html')


@app.errorhandler(403)
def forbidden(e):
    print(e)
    context = {
        'title': 'Доступ запрещен',
        'url': request.base_url
    }
    return render_template('403.html', **context), 403


@app.route('/square/', methods=['GET', 'POST'])
def square():
    if request.method == 'POST':
        num = int(request.form.get('num'))
        return redirect(url_for('res_square', num=num))
    return render_template('square.html')


@app.route('/square/result/')
def res_square():
    result = int(request.args.get('num'))
    return f'{result} в квадрате равно {result ** 2}'


@app.route('/form/', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        name = request.form.get('name')
        flash(f'Привет, {name}!', 'success')
        return redirect(url_for('form'))
    return render_template('hello_flash.html')


if __name__ == '__main__':
    app.run(debug=True)
