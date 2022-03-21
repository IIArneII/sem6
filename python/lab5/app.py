from flask import Flask, request, render_template
from data import db_session
from data.tables import User, Job, Department
from forms.user import RegisterForm
from insert import add_user
import re

app = Flask(__name__)
app.config['SECRET_KEY'] = 'my_secret_key'


@app.route('/favicon.ico')
def favicon():
    return 'favicon'


@app.route('/')
@app.route('/jobs')
def jobs():
    db = db_session.create_session()
    j = list(db.query(Job).all())
    return render_template('jobs.html', title='Список задач', jobs=j)


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        if form.password.data != form.password_again.data:
            return render_template('register.html', title='Регистрация', form=form, message="Пароли не совпадают")
        if not re.findall('^\d+$', form.age.data):
            return render_template('register.html', title='Регистрация', form=form,
                                   message="Поле возраста должно содержать только цифры")
        add_user(form.surname.data, form.name.data, int(form.age.data), form.email.data, form.password.data,
                 form.position.data, form.speciality.data, form.address.data)
        return 'Успешно'
    return render_template('register.html', title='Регистрация', form=form)


if __name__ == '__main__':
    db_session.global_init("db/mars_explorer.db")
    app.run(port=8080, host='127.0.0.1')
