"""Выводим HTML

Рассмотрим два варианта вывода HTML.

Многостраничный текст с тегами
Python легко может сохранить многостраничный документ в переменной, если
заключить его в три двойные кавычки."""
from flask import Flask

app = Flask(__name__)

html = """
<h1>Привет, меня зовут Алексей</h1>
<p>Уже много лет я создаю сайты на Flask.<br/>Посмотрите на мой сайт.</p>
"""

"""Содержимое переменной можно вернуть, используя функцию представления. При
этом браузер выведет текст с учётом тегов."""


@app.route('/text/')
def text():
    return html


"""Как вы видите, html теги не выводятся в браузере как текст, а преобразуются в теги.
При желании можно сделать страницу динамической. В примере ниже каждая
строчка стихотворения хранится как элемент списка list. Для примера в первой
лекции этого достаточно. Но вы должны понимать, что аналогичным образом можно
использовать данные из БД, внешних источников и т.п."""


@app.route('/poems/')
def poems():
    poem = ['Вот не думал, не гадал,',
            'Программистом взял и стал.',
            'Хитрый знает он язык,',
            'Он к другому не привык.',
            ]

    txt = '<h1>Стихотворение</h1>\n<p>' + '<br/>'.join(poem) + '</p>'
    return txt


"""При желании можно прописать любую логику внутри функции, в зависимости от
задач программиста и того, какую информацию необходимо вывести на странице
сайта.
"""

if __name__ == '__main__':
    app.run()
