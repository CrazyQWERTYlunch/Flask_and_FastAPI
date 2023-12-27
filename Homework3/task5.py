from flask import Flask, redirect, render_template, request, url_for
from flask_wtf.csrf import CSRFProtect

from Homework3.forms.forms5 import RegistrationForm


app = Flask(__name__)

app.config['SECRET_KEY'] = 'secretkey'
csrf = CSRFProtect(app)

EXAMPLE_DB = {}


@app.route('/', methods=['GET', 'POST'])
def index():
    form = RegistrationForm()
    form_notifications = []
    if request.method == 'POST' and form.validate():
        user = form.data.copy()
        if user['name'] not in EXAMPLE_DB:
            EXAMPLE_DB[user['name']] = dict(
                ((key, value) for key, value in user.items() if key != 'name')
            )
        form_notifications.append(
            f'Пользователь {user["name"]} успешно зарегистрирован!'
        )
        return redirect(url_for('main', username=user['name']))
    return render_template(
        'task5.html', form=form, form_notifications=form_notifications
    )


@app.route('/<username>/')
def main(username: str):
    user_data = EXAMPLE_DB.get(username, {})
    return render_template('5_main.html', username=username, **user_data)


if __name__ == '__main__':
    app.run(debug=True)