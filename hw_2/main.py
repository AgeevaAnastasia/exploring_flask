"""Создать страницу, на которой будет форма для ввода имени и электронной почты,
при отправке которой будет создан cookie-файл с данными пользователя,
а также будет произведено перенаправление на страницу приветствия,
где будет отображаться имя пользователя.

На странице приветствия должна быть кнопка «Выйти»,
при нажатии на которую будет удалён cookie-файл с данными пользователя
и произведено перенаправление на страницу ввода имени и электронной почты."""

from flask import Flask, request, make_response, render_template, redirect, url_for

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        email = request.form.get('email')
        response = make_response(redirect(url_for('welcome', username=username)))
        response.headers['new_head'] = 'New value'
        # создаём cookie
        response.set_cookie('username', 'email')
        return response
    return render_template('index.html')


@app.route('/getcookie/')
def get_cookies():
    # получаем значение cookie
    name = request.cookies.get('username')
    email = request.cookies.get('email')
    return f"Значение cookie: {name}, {email}"


@app.route('/welcome/')
def welcome():
    return render_template('welcome.html', username=request.args.get('username'))


@app.route('/logout/')
def logout():
    response = make_response(render_template('index.html'))
    # удаляем cookie
    response.delete_cookie('username')
    response.delete_cookie('email')
    return response


if __name__ == '__main__':
    app.run(debug=True)
