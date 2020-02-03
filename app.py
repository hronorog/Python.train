# -*- coding: utf8 -*-
from flask import Flask, render_template, abort
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
                           title=title,
                           tours=spisok,
                           subtitle=subtitle,
                           description=description,
                           departures=departures)


@app.route('/from/<direction>')
def direction(direction):
    # фильтруем туры по выбранному направлению
    lst = []
    city = ''
    for k, v in tours.items():
        if v["departure"] == direction:
            lst.append(v)
            city = departures[direction]
    # направление
    try:
        city = city[:1].lower()+city[1:]
    except:
        pass
    return render_template('direction.html',
                           city=city,
                           title=title,
                           tours=lst,
                           subtitle=subtitle,
                           description=description,
                           departures=departures
                           )


@app.route('/tour/<ids>')
def tour(ids):
    try:
        tourset = tours[int(ids)]
    except KeyError:
        tourset = None
    if tourset is None:
        abort(404, description='Uuuuuups, WTF?')
    return render_template('tour.html',
                           title=title,
                           tour=tourset,
                           departures=departures
                           )


@app.errorhandler(404)
@app.errorhandler(500)
def not_found(e):
    return "Такой страницы нет"


app.run('0.0.0.0', 8000)
