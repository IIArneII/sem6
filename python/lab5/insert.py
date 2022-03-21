from data import db_session
from data.tables import User, Job, Department
from datetime import datetime


def add_user(surname, name, age, email, hashed_password, position=None, speciality=None, address=None):
    user = User()

    user.surname = surname
    user.name = name
    user.age = age
    user.email = email
    user.hashed_password = hashed_password
    user.position = position
    user.speciality = speciality
    user.address = address

    db_sess = db_session.create_session()
    db_sess.add(user)
    db_sess.commit()


def add_job(team_leader=None, description=None, work_size=None, collaborators=None, start_date=None, is_finished=False):
    job = Job()

    job.team_leader = team_leader
    job.description = description
    job.work_size = work_size
    job.start_date = start_date
    job.is_finished = is_finished

    db_sess = db_session.create_session()

    for i in collaborators:
        user = list(db_sess.query(User).filter(User.id == i))[0]
        job.collaborators.append(user)

    db_sess.add(job)
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


if __name__ == '__main__':
    db_session.global_init("db/mars_explorer.db")

    add_user('Скотт', 'Ридли', 21, 'scott_chief@mars.org', '123456', position='Капитан',
             speciality='Инженер-исследователь', address='module_1')
    add_user('Кривоносова', 'София', 21, 'sofa@mars.org', '985471', position='Пилот', speciality='Астрогеолог',
             address='module_2')
    add_user('Бауэр', 'Рудольф', 20, 'ba@mars.org', '985461571', position='Исследователь', speciality='Киберинженер',
             address='module_2')
    add_user('Калинько', 'Арсений', 20, 'arsenii@mars.org', '91', position='Исследователь', speciality='Врач',
             address='module_1')
    add_user('Сулиман', 'Роман', 21, 'sul@mars.org', '9816181', position='Пилот', speciality='Оператор марсохода',
             address='module_3')
    add_user('Шванев', 'Арсений', 21, 'arne@mars.org', '98181286181', position='Исследователь', speciality='Экзобиолог',
             address='module_3')

    add_job(1, 'Развертывание жилых модулей 1 и 2', 15, [2, 3], datetime.now(), False)
    add_job(2, 'Развертывание жилых модулей 3 и 4', 17, [4, 5, 6], datetime.now(), True)
    add_job(5, 'Исследование почвы', 25, [3, 4, 6], datetime.now(), False)
    add_job(1, 'Разветка территории', 12, [4, 5], datetime.now(), False)
    add_job(2, 'Технический осмотр корабля', 21, [3, 5], datetime.now(), True)

    add_department('Исследования', 6, [3, 4, 6], 'research@mars.org')
    add_department('Пилотирование', 2, [2, 5], 'piloting@mars.org')
    add_department('Руководство', 1, [1], 'management@mars.org')
