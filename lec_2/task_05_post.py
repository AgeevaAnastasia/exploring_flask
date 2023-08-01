"""Обработка POST запросов

POST запросы используются для отправки данных на сервер. Они отличаются от GET
запросов тем, что данные, передаваемые в POST запросах, не видны в URL. Также
POST запросы могут содержать большее количество данных, чем GET.

Для того, чтобы передать данные в POST запросе, обычно используют HTML форму.

У формы нужно указать атрибут method="post" для правильной обработки
сервером.

Ниже приведен пример HTML формы:

<!DOCTYPE html>
<html lang="ru">
<head>
<meta charset="UTF-8">
<title>Форма для POST запроса</title>
</head>
<body>
<form action="/submit" method="post">
<input type="text" name="name" placeholder="Имя">
<input type="submit" value="Отправить">
</form>
</body>
</html>


В данном примере мы создаем HTML-форму с полем "name" и кнопкой "submit". При
нажатии на кнопку страница отправляет POST-запрос на указанный URL, в данном
случае "/submit".

В Python-коде функция, ассоциированная с URL "/submit", использует функцию
request.form.get() для получения данных, переданных через форму."""


from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/submit', methods=['GET', 'POST'])
def submit():
    if request.method == 'POST':
        name = request.form.get('name')
        return f'Hello {name}!'
    return render_template('form.html')


if __name__ == '__main__':
    app.run()


"""В декораторе передаём список ['GET', 'POST'] по ключу methods. Теперь view готова
обрабатывать как get, так и post запросы. Внутри делаем проверку метода. Если
была отправлена форма, функция request.form.get() извлекает данные, переданные
через форму, и сохраняет их в переменную name. Последняя строка сработает в
случае get запроса и выводит шаблон с формой для заполнения.


🔥 Важно! Используйте метод get для поиска значения внутри request.form.
Так вы избежите ошибок обращения к несуществующему ключу. Нет
гарантий, что клиент отправит все ключи, которые разработчик передаёт в
HTML форме. Альтернатива - блок try с обработкой KeyError.

GET и POST запросы нужны, чтобы отправлять данные на сервер. GET запросы
используются, чтобы получать данные, а POST — чтобы отправлять."""