"""Создать страницу, на которой будет кнопка "Нажми меня", при
нажатии на которую будет переход на другую страницу с
приветствием пользователя по имени."""

from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/')
def main():
    return render_template('index.html')


@app.route('/hello/')
def hello():
    return 'Привет, мир!'


@app.route('/submit/', methods=['GET', 'POST'])
def submit():
    if request.method == 'POST':
        name = request.form.get('name')
        return f'Hello, {name}!'
    return render_template('index.html')


if __name__ == '__main__':
    app.run()