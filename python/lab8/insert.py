from data import db_session
from data.tables import User, Job, Department, Category


def add_user(surname, name, age, email, password, position=None, speciality=None, address=None):
    user = User()

    user.surname = surname
    user.name = name
    user.age = age
    user.email = email
    user.position = position
    user.speciality = speciality
    user.address = address
    user.set_password(password)

    db_sess = db_session.create_session()
    db_sess.add(user)
    db_sess.commit()


def add_job(team_leader=None, description=None, work_size=None, collaborators=None, categories=None, start_date=None, end_date=None,
            is_finished=False):
    job = Job()

    job.team_leader = team_leader
    job.description = description
    job.work_size = work_size
    job.start_date = start_date
    job.end_date = end_date
    job.is_finished = is_finished

    db_sess = db_session.create_session()

    for i in collaborators:
        user = list(db_sess.query(User).filter(User.id == i))[0]
        job.collaborators.append(user)

    for i in categories:
        cat = list(db_sess.query(Category).filter(Category.id == i))[0]
        job.categories.append(cat)

    db_sess.add(job)
    db_sess.commit()


def edit_job(id, team_leader=None, description=None, work_size=None, collaborators=None, categories=None,
             start_date=None, end_date=None, is_finished=False):
    db_sess = db_session.create_session()

    job = db_sess.query(Job).filter(Job.id == id).first()

    job.team_leader = team_leader
    job.description = description
    job.work_size = work_size
    job.start_date = start_date
    job.end_date = end_date
    job.is_finished = is_finished

    job.collaborators[:] = []
    for i in collaborators:
        user = list(db_sess.query(User).filter(User.id == i))[0]
        job.collaborators.append(user)

    job.categories[:] = []
    for i in categories:
        cat = list(db_sess.query(Category).filter(Category.id == i))[0]
        job.categories.append(cat)

    db_sess.commit()


def add_department(title, chief, members, email):
    department = Department()

    department.title = title
    department.chief = chief
    department.email = email

    db_sess = db_session.create_session()

    for i in members:
        user = list(db_sess.query(User).filter(User.id == i))[0]
        department.members.append(user)

    db_sess.add(department)
    db_sess.commit()
