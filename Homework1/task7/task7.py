from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    context = [
        {'heading': 'Первая новость',
         'descr': 'Это была первая новость',
         'date': '01.11.2023'},
        {'heading': 'Вторая новость',
         'descr': 'Это была вторая новость',
         'date': '02.11.2023'},
        {'heading': 'Третья новость',
         'descr': 'Это была третья новость',
         'date': '03.11.2023'}
    ]

    return render_template('table.html', context=context)
