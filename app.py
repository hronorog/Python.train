from flask import Flask, render_template


app = Flask(__name__)


@app.route('/')
def main():
    return render_template('index.html')


@app.route('/about/')
def about():
    return render_template('about.html')


@app.errorhandler(404)
def not_found(e):
    return "Такой страницы нет"


app.run('0.0.0.0', 8000)
