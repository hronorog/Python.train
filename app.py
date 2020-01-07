from flask import Flask, request


app = Flask(__name__)


@app.route('/')
def main():
    return '''  Привет, это Stepik ***,  портал по видео про ****.
                <br>Перейдите на /about чтобы посмотреть инфрмацию
                <br>Перейдите на /playlists чтобы посмотреть плейлисты 
                <br>Перейдите на /videos/1 чтобы посмотреть видео
                <br>
                <br>Теги: concrete, table ,wood, furniture, accessorizes, metal
                <br>Плейлисты: Поделки из бетона (4 видео), Работа по дереву (8 видео), Изготовление мебели (6 видео)'''


@app.route('/about/')
def about():
    return 'Информация о проекте'


@app.route('/videos/<id>')
def videos(id):
    return '''Название: Concrete Candle Holder How To Make
            <br>Теги: concrete, accessorizes
            <br>Видео: youtu.be/Z_8Ss94fgZc'''


@app.route('/playlists/<id>')
def playlists(id):
    return '''Плейлист: Поделки из бетона:
            <br>
            <br>1. How To Make a Concrete Fire Bowl
            <br>http://youtu.be/DwJpy48GZF0
            <br>
            <br>2. Making a table top FIRE PIT
            <br>http://youtu.be/DwJpy48GZF0
            <br>
            <br>3. MODERN Outdoor Concrete and Wood
            <br>http://youtu.be/zD-lSfDSKn0
            <br>
            <br>4. Diy LED Desk Lamp With Concrete Base
            <br>http://youtu.be/a5yiMhJaGCo
            <br>
            <br>Приятного просмотра!'''


@app.route('/tags/<tag>')
def thetag(tag):
    return '''У нас есть 3 видео по тегу: concrete
            <br>
            <br>1. How To Make a Concrete Fire Bowl
            <br>http://youtu.be/DwJpy48GZF0
            <br>
            <br>2. Making a table top FIRE PIT
            <br>http://youtu.be/DwJpy48GZF0
            <br>
            <br>3. MODERN Outdoor Concrete and Wood
            <br>http://youtu.be/zD-lSfDSKn0'''


@app.errorhandler(404)
def not_found(e):
    return "Такой страницы нет"


app.run('0.0.0.0', 8000)
