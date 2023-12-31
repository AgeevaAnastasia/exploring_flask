"""Flash сообщения

Flash сообщения в Flask являются способом передачи информации между
запросами. Это может быть полезно, например, для вывода сообщений об
успешном выполнении операции или об ошибках ввода данных.

Для работы с flash сообщениями используется функция flash(). Она принимает
сообщение и категорию, к которой это сообщение относится, и сохраняет его во
временном хранилище.

Например, чтобы вывести сообщение об успешной отправке формы, можно
использовать следующий код:"""

from flask import Flask, flash, redirect, render_template, request, url_for

app = Flask(__name__)

app.secret_key = b'5f214cacbd30c2ae4784b520f17912ae0d5d8c16ae98128e3f549546221265e4'


@app.route('/form', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        # Обработка данных формы
        flash('Форма успешно отправлена!', 'success')
        return redirect(url_for('form'))
    return render_template('form.html')


"""В этом примере мы определяем маршрут '/form' для отображения и обработки
формы. Если метод запроса POST, то происходит обработка данных формы и
выводится сообщение об успешной отправке с помощью функции flash() и
категории 'success'. Затем происходит перенаправление на страницу с формой с
помощью функции redirect().


Секретный ключ

Небольшое отступление. Чтобы не получать ошибки вида при работе с сессией
RuntimeError: The session is unavailable because no secret key
was set. Set the secret_key on the application to something
unique and secret.
необходимо добавить в Flask приложение секретный ключ.

Простейший способ генерации такого ключа, выполнить следующие пару строк
кода

>>> import secrets
>>> secrets.token_hex()

Сразу после создания приложения прописываем инициализацию ключа
сгенерированным набором байт. Теперь данные в безопасности, можно продолжать
развивать приложение.



Шаблон для flash сообщений

Чтобы вывести flash сообщения в HTML шаблоне, можно использовать следующий
код шаблона:

{% extends 'base.html' %}
{% block title %}
{{ title }}
{% endblock %}
19
{% block content %}
<form action="/form" method="post">
{% with messages = get_flashed_messages(with_categories=true)
%}
{% if messages %}
{% for category, message in messages %}
<div class="alert alert-{{ category }}">
{{ message }}
</div>
{% endfor %}
{% endif %}
{% endwith %}
<input type="text" name="name" placeholder="Имя">
<input type="submit" value="Отправить">
</form>
{% endblock %}

Этот код использует функцию get_flashed_messages() для получения всех flash
сообщений с категориями (блок with). Далее проверяем передавались ли
сообщения через flash. Если да, в цикле происходит получение категорий и
сообщений, т.к. указан параметр with_categories=true. Далее их вывод в
соответствующих блоках с применением стилей bootstrap.


Категории flash сообщений

Категории сообщений в flash позволяют различать типы сообщений и выводить их
по-разному. Категория по умолчанию message. Но вторым аргументом можно
передавать и другие категории, например warning, success и другие.
Например, чтобы вывести сообщение об ошибке ввода данных, можно
использовать следующую модификацию функции:"""


@app.route('/form', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        # Проверка данных формы
        if not request.form['name']:
            flash('Введите имя!', 'danger')
            return redirect(url_for('form'))
        # Обработка данных формы
        flash('Форма успешно отправлена!', 'success')
        return redirect(url_for('form'))
    return render_template('form.html')


"""Проверяем данные формы на наличие имени. Если имя не указано, то выводится
сообщение об ошибке с категорией danger и происходит перенаправление на
страницу с формой. Сама форма будет работать без изменений.
Flash сообщения являются удобным способом передачи информации между
запросами в Flask. Они позволяют выводить сообщения пользователю и упрощают
обработку ошибок и успешных операций."""

if __name__ == '__main__':
    app.run()
