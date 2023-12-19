from flask import Flask, render_template, request


app = Flask(__name__)


@app.get('/')
def index():
    return render_template('age_reg.html')


@app.post('/')
def index_post():
    name = request.form.get('name')
    age = request.form.get('age')

    if age.isdigit() and int(age) > 18:
        result = f'возраст {age}'
    else:
        result = 'неправильный возраст'
    return render_template('age_reg.html', name=name, result=result)


if __name__ == '__main__':
    app.run(debug=True)