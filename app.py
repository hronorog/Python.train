# -*- coding: utf8 -*-
from flask import Flask, render_template
from data import *
from random import shuffle


app = Flask(__name__)


@app.route('/')
def main():
    # генерируем 6 случайных отелей на главной странице
    lst = [x for x in range(1, 17)]
    shuffle(lst)
    lst = lst[:6]
    spisok = []
    for i in lst:
        spisok.append(tours.get(i))

    return render_template('index.html',
                           check_cards=True,
                           title=title,
                           tours=spisok,
                           subtitle=subtitle,
                           description=description,
                           departures=departures)


@app.route('/from/<direction>')
def direction(direction):

    lst = []
    for k, v in tours.items():
        if v["departure"] == "kazan":
            lst.append(v)

    return render_template('direction.html',
                           check_cards=True,
                           title=title,
                           tours=lst,
                           subtitle=subtitle,
                           description=description,
                           departures=departures
                           )


@app.route('/<id>')
def tour(id):
    return render_template('tour.html', toursid=tours)


@app.errorhandler(404)
def not_found(e):
    return "Такой страницы нет"


app.run('0.0.0.0', 8000)
