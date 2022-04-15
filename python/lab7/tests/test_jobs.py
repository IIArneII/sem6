from requests import delete, post, get, put


def add_jobs_and_users():
    users = get('http://localhost:8080/api/users').json()
    next_id = max(([0] + [i['id'] for i in users['users']])) + 1
    user1 = post('http://localhost:8080/api/users', json={
        'name': 'Арсений',
        'surname': 'Шванев',
        'age': 20,
        'email': f'shwanev.gzed@gmail.com{next_id}',
        'password': '123',
    }).json()
    assert 'error' not in user1

    user2 = post('http://localhost:8080/api/users', json={
        'name': 'Анна',
        'surname': 'Илина',
        'age': 21,
        'email': f'ann@gmail.com{next_id + 1}',
        'password': '123',
    }).json()
    assert 'error' not in user2

    job1 = post('http://localhost:8080/api/jobs', json={
        'team_leader': user1['user']['id'],
        'description': 'Новое описание1',
        'work_size': 10,
        'collaborators': [user2['user']['id']],
        'categories': [1, 2]
    }).json()
    assert 'error' not in job1

    job2 = post('http://localhost:8080/api/jobs', json={
        'team_leader': user2['user']['id'],
        'description': 'Новое описание2',
        'work_size': 12,
        'collaborators': [user1['user']['id']],
        'categories': [1]
    }).json()
    assert 'error' not in job2

    return (job1, job2), (user1, user2)


def del_jobs(*args):
    for i in args:
        response = delete(f'http://localhost:8080/api/jobs/{i["job"]["id"]}')
        assert 'error' not in response


def del_users(*args):
    for i in args:
        response = delete(f'http://localhost:8080/api/users/{i["user"]["id"]}')
        assert 'error' not in response


def test_get_jobs():
    # Добавление работ и пользователей
    jobs, users = add_jobs_and_users()

    # Тестирование получения списка работ
    response = get('http://localhost:8080/api/jobs').json()
    assert 'error' not in response
    ids = [i['id'] for i in response['jobs']]
    for job in jobs:
        assert job['job']['id'] in ids
        for i, v in enumerate(ids):
            if v != job['job']['id']:
                continue
            assert job['job']['team_leader'] == response['jobs'][i]['team_leader']
            assert job['job']['description'] == response['jobs'][i]['description']
            assert len(job['job']['categories']) == len(response['jobs'][i]['categories'])
            for j, cat in enumerate(job['job']['categories']):
                assert cat['id'] == response['jobs'][i]['categories'][j]['id']

    # Удаление работ и пользователей
    del_jobs(*jobs)
    del_users(*users)


def test_get_job():
    # Добавление работ и пользователей
    jobs, users = add_jobs_and_users()

    # Тестирование получения работы по id
    for job in jobs:
        response = get(f'http://localhost:8080/api/jobs/{job["job"]["id"]}').json()
        assert 'error' not in response
        assert job['job']['id'] == response['job']['id']
        assert job['job']['team_leader'] == response['job']['team_leader']
        assert job['job']['description'] == response['job']['description']
        assert job['job']['work_size'] == response['job']['work_size']
        assert len(job['job']['collaborators']) == len(response['job']['collaborators'])
        for j, col in enumerate(job['job']['collaborators']):
            assert col['id'] == response['job']['collaborators'][j]['id']
        assert len(job['job']['categories']) == len(response['job']['categories'])
        for j, cat in enumerate(job['job']['categories']):
            assert cat['id'] == response['job']['categories'][j]['id']

    # Тестирование получения работы по неверному id
    response = get(f'http://localhost:8080/api/jobs/0').json()
    assert 'error' in response

    # Тестирование получения работы по строчному id
    response = get(f'http://localhost:8080/api/jobs/a').json()
    assert 'error' in response

    # Удаление работ и пользователей
    del_jobs(*jobs)
    del_users(*users)


def test_create_job():
    # Добавление работ и пользователей
    users = get('http://localhost:8080/api/users').json()
    next_id = max(([0] + [i['id'] for i in users['users']])) + 1
    user1 = post('http://localhost:8080/api/users', json={
        'name': 'Арсений',
        'surname': 'Шванев',
        'age': 20,
        'email': f'shwanev.gzed@gmail.com{next_id}',
        'password': '123',
    }).json()
    assert 'error' not in user1

    user2 = post('http://localhost:8080/api/users', json={
        'name': 'Анна',
        'surname': 'Илина',
        'age': 21,
        'email': f'ann@gmail.com{next_id + 1}',
        'password': '123',
    }).json()
    assert 'error' not in user2

    job = post('http://localhost:8080/api/jobs', json={
        'team_leader': user1['user']['id'],
        'description': 'Новое описание1',
        'work_size': 10,
        'collaborators': [user2['user']['id']],
        'categories': [1, 2]
    }).json()
    assert 'error' not in job

    # Добавление работы с пустым json
    response = post('http://localhost:8080/api/jobs').json()
    assert 'error' in response
    assert response['error'] == 'Empty request'

    # Некорректный запрос: недостаточно параметов в json
    response = post('http://localhost:8080/api/jobs', json={
        'team_leader': 1,
        'description': 'Новое описание2',
    }).json()
    assert 'error' in response
    assert response['error'] == 'Bad request'

    # Добавление работы с уже существующим id
    response = post('http://localhost:8080/api/jobs', json={
        'id': job['job']['id'],
        'team_leader': 2,
        'description': 'Новое описание2',
        'work_size': 12,
        'collaborators': [1],
        'categories': [1]
    }).json()
    assert 'error' in response
    assert response['error'] == 'Id already exists'

    # Удаление работ и пользователей
    del_jobs(job)
    del_users(user1, user2)


def test_del_job():
    # Добавление работ и пользователей
    jobs, users = add_jobs_and_users()

    # Удаление работы
    response = delete(f'http://localhost:8080/api/jobs/{jobs[0]["job"]["id"]}')
    assert 'error' not in response
    jobs_after_del = get('http://localhost:8080/api/jobs').json()
    assert jobs[0]["job"]["id"] not in [i['id'] for i in jobs_after_del['jobs']]

    # Удаление работы с несуществующим id
    response = delete('http://localhost:8080/api/jobs/0').json()
    assert 'error' in response
    assert response['error'] == 'Not found'

    # Удаление работы по строчному id
    response = delete('http://localhost:8080/api/jobs/a').json()
    assert 'error' in response
    assert response['error'] == 'Not found'

    # Удаление работ
    jobs = list(jobs)
    del jobs[0]
    del_jobs(*jobs)
    del_users(*users)


def test_update_job():
    # Добавление работ и пользователей
    jobs, users = add_jobs_and_users()

    # Обновление работы
    update_job = put(f'http://localhost:8080/api/jobs/{jobs[0]["job"]["id"]}', json={
        'description': 'Обновленное описание'
    }).json()
    assert 'error' not in update_job
    assert update_job['job']['description'] == 'Обновленное описание'
    job = get(f'http://localhost:8080/api/jobs/{jobs[0]["job"]["id"]}').json()
    assert job['job']['description'] == 'Обновленное описание'

    # Обновление работы с несуществующим id
    update_job = put('http://localhost:8080/api/jobs/0', json={
        'description': 'Обновленное описание'
    }).json()
    assert 'error' in update_job
    assert update_job['error'] == 'Not found'

    # Обновление работы со строчным id
    update_job = put('http://localhost:8080/api/jobs/a', json={
        'description': 'Обновленное описание'
    }).json()
    assert 'error' in update_job
    assert update_job['error'] == 'Not found'

    # Обновление работы с пустым json
    update_job = put(f'http://localhost:8080/api/jobs/{jobs[0]["job"]["id"]}').json()
    assert 'error' in update_job
    assert update_job['error'] == 'Empty request'

    # Удаление работ и пользователей
    del_jobs(*jobs)
    del_users(*users)
