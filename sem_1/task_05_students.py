"""Написать функцию, которая будет выводить на экран HTML
страницу с таблицей, содержащей информацию о студентах.
Таблица должна содержать следующие поля: "Имя",
"Фамилия", "Возраст", "Средний балл".
Данные о студентах должны быть переданы в шаблон через
контекст.
"""


from flask import Flask, render_template

app = Flask(__name__)

students = [
    {'firstname': 'Иван', 'lastname': 'Иванов', 'age': 21, 'rate': 4.8},
    {'firstname': 'Денис', 'lastname': 'Сидоров', 'age': 19, 'rate': 4.2},
    {'firstname': 'Анна', 'lastname': 'Герасимова', 'age': 20, 'rate': 4.6},
    {'firstname': 'Игорь', 'lastname': 'Петров', 'age': 22, 'rate': 3.9},
    {'firstname': 'Жанна', 'lastname': 'Азарова', 'age': 19, 'rate': 5.0}
]

@app.route('/students/')
def get_students():
    return render_template('students.html', students=students)


if __name__ == '__main__':
    app.run(debug=True)
