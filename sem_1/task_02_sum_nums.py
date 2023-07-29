"""Написать функцию, которая будет принимать на вход два
числа и выводить на экран их сумму.
"""

from flask import Flask

app = Flask(__name__)


@app.route('/<int:num_a>/<int:num_b>/')
def sum_nums(num_a, num_b):
    return f'{num_a} + {num_b} = {num_a + num_b}'


if __name__ == '__main__':
    app.run(debug=True)