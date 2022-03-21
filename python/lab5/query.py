from data import db_session
from data.tables import User, Job, Department

if __name__ == '__main__':
    db_session.global_init("db/mars_explorer.db")

    db = db_session.create_session()

    print('\nВывести всех колонистов, проживающих в первом модуле, каждого с новой строки:')
    for i in db.query(User).filter(User.address == 'module_1'):
        print(i)

    print('\nВывести id колонистов из 1 модуля и ни speciality, ни position которых не содержат подстроку "Инженер":')
    for i in db.query(User).filter(User.address == 'module_1',
                                   User.speciality.notilike('%Инженер%'),
                                   User.position.notilike('%Инженер%')):
        print(i.id)

    print('\nВывести всех, у кого возраст меньше 21 с указанием возраста в годах, каждого с новой строки:')
    for i in db.query(User).filter(User.age < 21):
        print(i.id, i.name, i.surname, i.age)

    print('\nВывести всех, у кого в названии должности есть "Капитан" или "Пилот", каждого с новой строки:')
    for i in db.query(User).filter(User.position.ilike('%Капитан%') | User.position.ilike('%Пилот%')):
        print(i, i.position)

    print('\nВыводести работы, выполнение которых требует меньше 20 часов и которые еще не закончены:')
    for i in db.query(Job).filter(Job.work_size < 20, Job.is_finished == False):
        print(i)

    print('\nВыводит имена тимлидов работ, которые выполняются наибольшими командами:')
    for i in [i for i in db.query(Job).all() if
              len(i.collaborators) == max([len(i.collaborators) for i in db.query(Job).all()])]:
        print(i.user)

    print('\nВывести имена работников департамента 1, которые имеют суммарное количество отработанных часов больше 20:')
    members = db.query(Department).filter(Department.id == 1).first().members
    jobs = db.query(Job).filter(Job.is_finished == True)
    for i in members:
        i.time = 0
        for j in jobs:
            if i in j.collaborators:
                i.time += j.work_size
        if i.time > 20:
            print(i.name, i.surname, i.time)
