"""Вывод сложных структур в цикле

Иногда необходимо вывести информацию о нескольких однотипных объектах с
набором свойств. Например, информацию о пользователях из базы данных. Или
если упростить задачу, список словарей с одинаковыми ключами. Для опытных
программистов очевидно, что оба вывода идентичны. Рассмотрим список словарей."""
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/users/')
def users():
    _users = [{'name': 'Никанор',
        'mail': 'nik@mail.ru',
        'phone': '+7-987-654-32-10',
        },
        {'name': 'Феофан',
        'mail': 'feo@mail.ru',
        'phone': '+7-987-444-33-22',
        },
        {'name': 'Оверран',
        'mail': 'forest@mail.ru',
        'phone': '+7-903-333-33-33',
        }, ]
    context = {'users': _users}
    return render_template('users.html', **context)


"""При выводе в шаблоне используем точечную нотацию для доступа к элементам
списка словарей.
...
<body>
<div class="row">
<h1 class="col-12 text-monospace text-center">Список
пользователей из БД</h1>
{% for user in users %}
<div class="col-12 col-md-6 col-lg-4">
<h2>{{ user.name }}</h2>
<p>{{ user.mail }}</p>
<p>{{ user.phone }}</p>
</div>
{% endfor %}
</div>
</body>
..."""

if __name__ == '__main__':
    app.run()