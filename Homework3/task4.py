from flask import Flask, render_template, request
from flask_wtf.csrf import CSRFProtect

from Homework3.forms.forms4 import SingUpForm
from models4 import db, User


app = Flask(__name__)
# Example secret key. REPLACE IT WITH REAL SECRET KEY
app.config['SECRET_KEY'] = 'secretkey'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///4.sqlite'
db.init_app(app)
csrf = CSRFProtect(app)


def add_user(username, email, password):
    user = User(username=username, email=email, password=password)
    db.session.add(user)
    db.session.commit()


@app.route('/', methods=['GET', 'POST'])
def index():
    form = SingUpForm()
    form_errors = []
    if request.method == 'POST' and form.validate():
        username = form.name.data
        email = form.email.data
        if User.query.filter(User.username == username).count() > 0:
            form_errors.append(f'Имя пользователя: {username} уже используется!')
        elif User.query.filter(User.email == email).count() > 0:
            form_errors.append(f'Email {email} уже используется!')
        else:
            print(f'Добавлен пользователь {username}!')
            add_user(username, form.email.data, form.password.data)
            form_notifications = [f'Пользователь {username} успешно зарегистрирован!']
            return render_template(
                'task4.html', form=form, form_notifications=form_notifications
            )
    return render_template('task4.html', form=form, form_errors=form_errors)


@app.cli.command('init-db')
def init_db():
    db.create_all()
    print('База данных успешно создана!')


if __name__ == '__main__':
    app.run(debug=True)