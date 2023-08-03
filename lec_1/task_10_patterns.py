"""Наследование шаблонов

Начнём с классической ситуации дублирования кода, который нарушает принцип
DRY. Рассмотрим две html-страницы с большим объёмом одинакового кода.
Шаблон main.html
<!doctype html>
<html lang="ru">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,
initial-scale=1, shrink-to-fit=no">
<link rel="stylesheet" href="/static/css/bootstrap.min.css">
<title>{{ title }}</title>
</head>
<body>
<div class="container-fluid">
<ul class="nav nav-pills justify-content-end align-items-end">
<li class="nav-item"><a href="/main/"
class="nav-link">Основная</a></li>
<li class="nav-item"><a href="/data/"
class="nav-link">Данные</a></li>
</ul>
<div class="row">
<h1 class="col-12 col-md-6 display-2">Привет, меня зовут
Алексей</h1>
<image src="/static/image/foto.jpg" class="col-12 col-md-6
image-fluid rounded-circle" alt="Моё фото">
</div>
<div class="row fixed-bottom modal-footer">
<hr>
<p>Все права защищены &copy;</p>
</div>
</div>
<script src="/static/js/bootstrap.bundle.min.js"></script>
</body>
</html>


Шаблон data.html
<!doctype html>
<html lang="ru">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,
initial-scale=1, shrink-to-fit=no">
<link rel="stylesheet" href="/static/css/bootstrap.min.css">
<title>{{ title }}</title>
</head>
<body>
<div class="container-fluid">
<ul class="nav nav-pills justify-content-end align-items-end">
<li class="nav-item"><a href="/main/"
class="nav-link">Основная</a></li>
<li class="nav-item"><a href="/data/"
class="nav-link">Данные</a></li>
</ul>
<div class="row">
<div class="col-12 col-md-6 col-lg-4">
<p>Lorem ipsum dolor sit amet, consectetur adipisicing
elit. Culpa, fugiat obcaecati? Dignissimos earum facilis incidunt
modi, molestias mollitia nam quis recusandae voluptatum?</p>
</div>
<div class="col-12 col-md-6 col-lg-4">
<p> Dicta id officia quibusdam vel voluptates. Ad
adipisci aliquid animi architecto commodi deleniti dolor
doloremque facilis fugiat hic illo nam odit officia placeat
provident quam quisquam quo reiciendis repudiandae sint suscipit
unde, velit voluptatem! </p>
</div>
<div class="col-12 col-md-6 col-lg-4">
<p>Ab accusamus delectus et expedita id iste,
laboriosam optio quam, recusandae sed veritatis voluptate!
Accusamus blanditiis debitis et tempora. Ab architecto asperiores
aut consequuntur distinctio earum iusto nihil, non odit quidem
soluta veniam.</p>
</div>
</div>
<div class="row fixed-bottom modal-footer">
<hr>
<p>Все права защищены &copy;</p>
</div>
</div>
<script src="/static/js/bootstrap.bundle.min.js"></script>
</body>
</html>


Для того, чтобы выводить эту пару страниц достаточно несколько строк кода на
Flask"""
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/main/')
def main():
    context = {'title': 'Главная'}
    return render_template('main.html', **context)


@app.route('/data/')
def data():
    context = {'title': 'База статей'}
    return render_template('data.html', **context)


if __name__ == '__main__':
    app.run()


"""На каждой странице всего несколько различных строк в середине. Остальной код
дублируется, Представьте, что у вас большой проект на десятки аналогичных
страниц. Сколько же времени вы затратите, чтобы изменить шапку или футер во
всём проекте?



Базовый и дочерние шаблоны
Создадим базовый шаблон base.html, который будет включать весь одинаковый
код.
<!doctype html>
<html lang="ru">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,
initial-scale=1, shrink-to-fit=no">
<link rel="stylesheet" href="/static/css/bootstrap.min.css">
<title>
{% block title %}
Мой сайт
{% endblock %}
</title>
</head>
<body>
<div class="container-fluid">
<ul class="nav nav-pills justify-content-end align-items-end">
<li class="nav-item"><a href="/main/"
class="nav-link">Основная</a></li>
<li class="nav-item"><a href="/data/"
class="nav-link">Данные</a></li>
</ul>
{% block content %}
Страница не заполнена
{% endblock %}
<div class="row fixed-bottom modal-footer">
19
<hr>
<p>Все права защищены &copy;</p>
</div>
</div>
<script src="/static/js/bootstrap.bundle.min.js"></script>
</body>
</html>



Исключённый текст для заголовка сайта был заменён на:

{% block title %} Мой сайт {% endblock %}

Для содержимого страницы код заменён на:

{% block content %}
Страница не заполнена
{% endblock %}


Количество блоков в базовом шаблоне и их названия зависят от задачи, которую
решает разработчик. Содержимое внутри block впоследствии будет заполнено
дочерними шаблонами. Инструкция block принимает один аргумент — название
блока. Внутри шаблона это название должно быть уникальным, иначе возникнет
ошибка.

Если в дочернем шаблоне блок отсутствует, выводится информация из базового
шаблона. В нашем примере, если в дочернем шаблоне не прописать блок title, будет
выведено значение «Мой сайт» из базового шаблона, а вместо содержимого увидим
что “Страница не заполнена”


Теперь из main.html и data.html можно удалить дублирующиеся строки и указать,
что эти шаблоны расширяют базовый.


Шаблон main.html

{% extends 'base.html' %}
{% block title %}
{{ super() }} - {{ title }}
{% endblock %}
{% block content %}
<div class="row">
<h1 class="col-12 col-md-6 display-2">Привет, меня зовут
Алексей</h1>
<image src="/static/image/foto.jpg" class="col-12 col-md-6
20
image-fluid rounded-circle" alt="Моё фото">
</div>
{% endblock %}



Шаблон data.html

{% extends 'base.html' %}
{% block title %}
{{ super() }} - {{ title }}
{% endblock %}
{% block content %}
<div class="row">
<div class="col-12 col-md-6 col-lg-4">
<p>Lorem ipsum dolor sit amet, consectetur adipisicing
elit. Culpa, fugiat obcaecati? Dignissimos earum facilis incidunt
modi, molestias mollitia nam quis recusandae voluptatum?</p>
</div>
<div class="col-12 col-md-6 col-lg-4">
<p> Dicta id officia quibusdam vel voluptates. Ad
adipisci aliquid animi architecto commodi deleniti dolor
doloremque facilis fugiat hic illo nam odit officia placeat
provident quam quisquam quo reiciendis repudiandae sint suscipit
unde, velit voluptatem! </p>
</div>
<div class="col-12 col-md-6 col-lg-4">
<p>Ab accusamus delectus et expedita id iste,
laboriosam optio quam, recusandae sed veritatis voluptate!
Accusamus blanditiis debitis et tempora. Ab architecto asperiores
aut consequuntur distinctio earum iusto nihil, non odit quidem
soluta veniam.</p>
</div>
</div>
{% endblock %}



Содержимое одноимённых блоков в дочерних шаблонах будет подставлено в
соответствующее место базового.

🔥 Внимание! Использование переменной {{ super() }} в дочерних шаблонах
позволяет выводить содержимое родительского блока, а не заменять его!


После такой оптимизации достаточно внести изменение в базовом шаблоне, чтобы
обновить одинаковую информацию на всех страницах сайта.
Дочерние шаблоны компакты и содержат только специфичную для страницы
информацию. А при отрисовке через Jinja в них легко передавать динамически
изменяемую информацию.


🔥 Важно! Сохранять текстовую информацию внутри html файла как в
data.html нелогично. Она должна храниться в базе данных. А шаблон в этом
случае может получать её через контекст и выводить в цикле.
"""