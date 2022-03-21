from data import db_session
from data.tables import User, Job
from datetime import datetime

if __name__ == '__main__':
    db_session.global_init("db/mars_explorer.db")

    db = db_session.create_session()

    print('Изменить всем, проживающим в модуле 1 и имеющим возраст менее 21 года, адрес на module_3')

    for i in db.query(User).filter(User.age < 21, User.address == 'module_1'):
        i.address = 'module_3'
        i.created_date = datetime.now()

    db.commit()
