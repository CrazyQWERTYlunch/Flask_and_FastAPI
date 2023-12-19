from flask import Flask, render_template, request


app = Flask(__name__)

def check_number(number, symbol=''):
    if number.isdigit():
        result = f'Квадрат числа {symbol}{number} = {int(number) ** 2}'
    elif number.replace('.', '').isdigit():
        result = f'Квадрат числа {symbol}{number} = {round(float(number) ** 2, 5)}'
    else:
        result = 'неправильное число'
    return result
@app.get('/')
def index():
    return render_template('square.html')


@app.post('/')
def index_post():
    number = request.form.get('number')
    if number[0] == '-':
        result = check_number(number[1:], '-')
    else:
        result = check_number(number)

    return render_template('square.html', result=result)


if __name__ == '__main__':
    app.run(debug=True)