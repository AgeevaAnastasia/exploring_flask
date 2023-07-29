"""Написать функцию, которая будет выводить на экран HTML
страницу с блоками новостей.
Каждый блок должен содержать заголовок новости,
краткое описание и дату публикации.
Данные о новостях должны быть переданы в шаблон через
контекст.
"""

from flask import Flask, render_template

app = Flask(__name__)


class News:
    def __init__(self, title, description, date):
        self.title = title
        self.description = description
        self.date = date


news1 = [
    {'title': 'Мы открыли сайт!', 'description': 'Торжественное открытие и шампанское', 'date': '2023-06-12'},
    {'title': 'Первое обновление', 'description': 'Первые доработки на основании ваших отзывов', 'date': '2023-07-15'},
    {'title': 'Второе обновление', 'description': 'Существенные исправления', 'date': '2023-07-30'}
]


@app.route('/news/')
def get_news():
    news = [News('Мы открыли сайт!', 'Торжественное открытие и шампанское', '2023-06-12'),
            News('Первое обновление', 'Первые доработки на основании ваших отзывов', '2023-07-15'),
            News('Второе обновление', 'Существенные исправления', '2023-07-30')]
    return render_template('news.html', news=news)


if __name__ == '__main__':
    app.run(debug=True)
