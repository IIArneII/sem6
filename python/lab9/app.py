from flask import Flask, request, render_template, redirect, abort, make_response, jsonify
from flask_login import LoginManager, login_user, login_required, logout_user, current_user
from flask_restful import Api
from lab9.data import db_session
from data.tables import User, Job, Category
from forms.forms import RegisterForm, LoginForm, JobForm
from insert import add_user, add_job
from insert import edit_job as ed_job
from lab9.api import jobs_api, users_api
from lab9.api import users_resource


app = Flask(__name__)
api = Api(app)
app.config['SECRET_KEY'] = 'my_secret_key'
login_manager = LoginManager()
login_manager.init_app(app)


@login_manager.user_loader
def load_user(user_id):
    db = db_session.create_session()
    return db.query(User).get(user_id)


@app.route('/')
def home():
    db = db_session.create_session()
    j = list(db.query(Job).all())
    return render_template('jobs.html', title='Главная', jobs=j)


@app.route('/new_job', methods=['GET', 'POST'])
@login_required
def new_job():
    form = JobForm()
    form.validate_on_submit()
    if request.method == 'POST':
        db = db_session.create_session()
        collaborators = []
        for email in form.collaborators.data.replace(" ", "").split(','):
            user = db.query(User).filter(User.email == email).first()
            if not user:
                return render_template('new_job.html', title='Новая задача', form=form,
                                       message=f'Указан неверный пользователь: {email}')
            if current_user.id == user.id:
                return render_template('new_job.html', title='Новая задача', form=form,
                                       message=f'Вы уже являетесь участником')
            collaborators.append(user.id)
        categories = []
        for cat in form.categories.data.replace(" ", "").split(','):
            category = db.query(Category).filter(Category.name == cat).first()
            if not category:
                return render_template('new_job.html', title='Новая задача', form=form,
                                       message=f'Указано неверное название категории: {cat}')
            categories.append(category.id)
        add_job(current_user.id, form.description.data, form.work_size.data, collaborators, categories,
                form.start_date.data,
                form.start_date.data, form.is_finished.data)
        return redirect('/')
    else:
        return render_template('new_job.html', title='Новая задача', form=form)


@app.route('/edit_job/<int:id>', methods=['GET', 'POST'])
@login_required
def edit_job(id):
    form = JobForm()
    if request.method == 'POST':
        db = db_session.create_session()
        collaborators = []
        for email in form.collaborators.data.replace(" ", "").split(','):
            user = db.query(User).filter(User.email == email).first()
            if not user:
                return render_template('new_job.html', title='Новая задача', form=form,
                                       message=f'Указан неверный пользователь: {email}')
            if current_user.id == user.id and current_user.id != 1:
                return render_template('new_job.html', title='Новая задача', form=form,
                                       message=f'Вы уже являетесь участником')
            collaborators.append(user.id)
        categories = []
        for cat in form.categories.data.replace(" ", "").split(','):
            category = db.query(Category).filter(Category.name == cat).first()
            if not category:
                return render_template('new_job.html', title='Новая задача', form=form,
                                       message=f'Указано неверное название категории: {cat}')
            categories.append(category.id)
        team_leader = db.query(Job).filter(Job.id == id).first().team_leader
        ed_job(id, team_leader, form.description.data, form.work_size.data, collaborators, categories,
               form.start_date.data, form.start_date.data, form.is_finished.data)
        return redirect('/')
    else:
        db = db_session.create_session()
        job = db.query(Job).filter(Job.id == id).first()
        if job and (job.team_leader == current_user.id or current_user.id == 1):
            form.description.data = job.description
            form.work_size.data = job.work_size
            form.collaborators.data = ', '.join([i.email for i in job.collaborators])
            form.categories.data = ', '.join([i.name for i in job.categories])
            form.start_date.data = job.start_date
            form.end_date.data = job.end_date
            form.is_finished.data = job.is_finished
            return render_template('new_job.html', title='Редактировать задачу', form=form)
        else:
            abort(404)


@app.route('/del_job/<int:id>', methods=['GET', 'POST'])
@login_required
def del_job(id):
    db = db_session.create_session()
    job = db.query(Job).filter(Job.id == id).first()
    if job and (Job.team_leader == current_user.id or current_user.id == 1):
        db.delete(job)
        db.commit()
    else:
        abort(404)
    return redirect('/')


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        db = db_session.create_session()
        user = db.query(User).filter(User.email == form.email.data).first()
        if user and user.check_password(form.password.data):
            login_user(user, remember=form.remember.data)
            return redirect("/")
        return render_template('login.html', title='Авторизация', form=form, message='Неправильный логин или пароль')
    return render_template('login.html', title='Авторизация', form=form)


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        if form.password.data != form.password_again.data:
            return render_template('register.html', title='Регистрация', form=form, message="Пароли не совпадают")
        db = db_session.create_session()
        if db.query(User).filter(User.email == form.email.data).first():
            return render_template('register.html', title='Регистрация', form=form, message="Почта уже используется")
        add_user(form.surname.data, form.name.data, int(form.age.data), form.email.data, form.password.data,
                 form.position.data, form.speciality.data, form.address.data)
        return redirect('/login')
    return render_template('register.html', title='Регистрация', form=form)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect('/')


@app.errorhandler(404)
def not_found(error):
    print('ауауауа')
    return make_response(jsonify({'error': 'Not found'}), 404)


if __name__ == '__main__':
    db_session.global_init("db/mars_explorer.db")
    app.register_blueprint(jobs_api.blueprint)
    app.register_blueprint(users_api.blueprint)
    api.add_resource(users_resource.UsersResource, '/api/v2/users/<int:user_id>')
    api.add_resource(users_resource.UsersListResource, '/api/v2/users')
    app.run(port=8080, host='127.0.0.1')
