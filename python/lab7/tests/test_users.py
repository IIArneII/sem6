from requests import delete, post, get, put
from datetime import datetime


def add_users():
    users = get('http://localhost:8080/api/users').json()
    next_id = max(([0] + [i['id'] for i in users['users']])) + 1
    user1 = post('http://localhost:8080/api/users', json={
        'name': 'Арсений',
        'surname': 'Шванев',
        'age': 20,
        'email': f'shwanev.gzed@gmail.com{next_id}',
        'password': '123',
        'modified_date': str(datetime.now())
    }).json()
    assert 'error' not in user1

    user2 = post('http://localhost:8080/api/users', json={
        'name': 'Анна',
        'surname': 'Илина',
        'age': 21,
        'email': f'ann@gmail.com{next_id + 1}',
        'password': '123',
        'modified_date': str(datetime.now())
    }).json()
    assert 'error' not in user2

    return user1, user2


def del_users(*args):
    for i in args:
        response = delete(f'http://localhost:8080/api/users/{i["user"]["id"]}')
        assert 'error' not in response


def test_get_users():
    # Добавление пользователей
    users = add_users()

    response = get('http://localhost:8080/api/users').json()
    assert 'error' not in response
    ids = [i['id'] for i in response['users']]
    for user in users:
        assert user['user']['id'] in ids
        for i, v in enumerate(ids):
            if v != user['user']['id']:
                continue
            assert user['user']['name'] == response['users'][i]['name']
            assert user['user']['surname'] == response['users'][i]['surname']
            assert user['user']['age'] == response['users'][i]['age']
            assert user['user']['email'] == response['users'][i]['email']

    # Удаление пользователей
    del_users(*users)


def test_get_user():
    # Добавление пользователей
    users = add_users()

    # Тестирование полученных по id пользователей
    for user in users:
        response = get(f'http://localhost:8080/api/users/{user["user"]["id"]}').json()
        assert 'error' not in response
        assert user['user']['name'] == response['user']['name']
        assert user['user']['surname'] == response['user']['surname']
        assert user['user']['age'] == response['user']['age']
        assert user['user']['email'] == response['user']['email']
        assert user['user']['modified_date'] == response['user']['modified_date']

    # Тестирование получение пользователя по неверному id
    response = get('http://localhost:8080/api/users/0').json()
    assert 'error' in response
    assert response['error'] == 'Not found'

    # Тестирование получение пользователя по строчному id
    response = get('http://localhost:8080/api/users/a').json()
    assert 'error' in response
    assert response['error'] == 'Not found'

    # Удаление пользователей
    del_users(*users)


def test_create_user():
    # Добавление пользователей
    users = get('http://localhost:8080/api/users').json()
    next_id = max(([0] + [i['id'] for i in users['users']])) + 1
    user = post('http://localhost:8080/api/users', json={
        'name': 'Арсений',
        'surname': 'Шванев',
        'age': 20,
        'email': f'shwanev.gzed@gmail.com{next_id}',
        'password': '123',
        'modified_date': str(datetime.now())
    }).json()
    assert 'error' not in user

    # Добавление пользователя с пустым json
    response = post('http://localhost:8080/api/users').json()
    assert 'error' in response
    assert response['error'] == 'Empty request'

    # Добавление пользователя с недостающими параметрами в json
    response = post('http://localhost:8080/api/users', json={
        'name': 'Арсений'
    }).json()
    assert 'error' in response
    assert response['error'] == 'Bad request'

    # Добавление пользователя с уже существующим id
    response = post('http://localhost:8080/api/users', json={
        'id': user['user']['id'],
        'name': 'Анна',
        'surname': 'Илина',
        'age': 21,
        'email': 'ann@gmail.com',
        'password': '123',
        'modified_date': str(datetime.now())
    }).json()
    assert 'error' in response
    assert response['error'] == 'Id already exists'

    # Удаление пользователей
    del_users(user)


def test_del_user():
    # Добавление пользователей
    users = add_users()

    # Удаление пользователя
    response = delete(f'http://localhost:8080/api/users/{users[0]["user"]["id"]}').json()
    assert 'error' not in response
    users_after_del = get('http://localhost:8080/api/users').json()
    assert users[0]["user"]["id"] not in [i['id'] for i in users_after_del['users']]

    # Удаление пользователя с несуществующим id
    response = delete('http://localhost:8080/api/jobs/0').json()
    assert 'error' in response
    assert response['error'] == 'Not found'

    # Удаление пользователя по строчному id
    response = delete('http://localhost:8080/api/jobs/a').json()
    assert 'error' in response
    assert response['error'] == 'Not found'

    # Удаление пользователей
    users = list(users)
    del users[0]
    del_users(*users)


def test_update_user():
    # Добавление пользователей
    users = add_users()

    # Обновление пользователя
    update_user = put(f'http://localhost:8080/api/users/{users[0]["user"]["id"]}', json={
        'name': 'Обновленное имя'
    }).json()
    assert 'error' not in update_user
    assert update_user['user']['name'] == 'Обновленное имя'
    user = get(f'http://localhost:8080/api/users/{users[0]["user"]["id"]}').json()
    assert user['user']['name'] == 'Обновленное имя'

    # Обновление пользователя с несуществующим id
    update_user = put('http://localhost:8080/api/users/0', json={
        'name': 'Обновленное имя'
    }).json()
    assert 'error' in update_user
    assert update_user['error'] == 'Not found'

    # Обновление пользователя со строчным id
    update_user = put('http://localhost:8080/api/users/a', json={
        'name': 'Обновленное имя'
    }).json()
    assert 'error' in update_user
    assert update_user['error'] == 'Not found'

    # Обновление пользователя с пустым json
    update_user = put(f'http://localhost:8080/api/users/{users[0]["user"]["id"]}').json()
    assert 'error' in update_user
    assert update_user['error'] == 'Empty request'

    # Удаление пользователей
    del_users(*users)
