"""Написать функцию, которая будет принимать на вход строку и
выводить на экран ее длину.
"""


from flask import Flask

app = Flask(__name__)


@app.route('/<text>/')
def len_text(text):
    return f'Длина строки "{text}" - {len(text)} символов'


if __name__ == '__main__':
    app.run(debug=True)