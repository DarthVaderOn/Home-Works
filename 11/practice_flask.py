"""Дополнительная обязательная домашка до понедельника: создать приложение flask с двумя Endpoints."""

# Импортируем Web framework Flask
from flask import Flask

# Экземпляр приложения с переменной Flask
app = Flask(__name__)


# Декоратор главной страницы URL с обработчиком событий (функция представления)
@app.route('/')
def hello_world():
    """При нахождении на главной странице будет выводиться указанная строка"""
    return 'Hello World!'


# Декоратор с дополнительным URL с обработчиком событий (функция представления)
@app.route('/user/<name>')
def user(name):
    """При указании имени после /user будет выведено приветственное сообщение"""
    return '<h>Hi %s!<h>' % name

# Декоратор с дополнительным URL с обработчиком событий (функция представления)
@app.route('/now/year')
def now_year():
    """При нахождении по данной ссылке будет выводиться указанная строка"""
    return '2022!'


# Запуск сервера (для быстрого выбора напишем main + Tab), с режимом отладки debug=True
if __name__ == '__main__':
    app.run(debug=True)