from flask import Blueprint, jsonify, request
from lab7.data import db_session
from lab7.data.tables import User
from datetime import datetime

blueprint = Blueprint('users_api', __name__, template_folder='templates')


@blueprint.get('/api/users')
def get_users():
    db = db_session.create_session()
    users = db.query(User).all()
    return jsonify({
        'users': list(map(lambda x: x.to_dict(only=('id', 'name', 'surname', 'age', 'email')), users))
    })


@blueprint.get('/api/users/<int:user_id>')
def get_user(user_id):
    db = db_session.create_session()
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        return jsonify({'error': 'Not found'})
    return jsonify({
        'user': user.to_dict(only=('id', 'name', 'surname', 'age', 'age', 'position', 'speciality', 'address', 'email',
                                   'modified_date'))
    })


@blueprint.post('/api/users')
def create_user():
    if not request.json:
        return jsonify({'error': 'Empty request'})
    if not all([i in request.json for i in ['name', 'surname', 'age', 'email', 'password']]):
        return jsonify({'error': 'Bad request'})
    db = db_session.create_session()
    if 'id' in request.json and db.query(User).filter(User.id == request.json['id']).first():
        return jsonify({'error': 'Id already exists'})

    user = User()
    if 'id' in request.json:
        user.id = request.json['id']
    user.name = request.json.get('name')
    user.surname = request.json.get('surname')
    user.age = request.json.get('age')
    user.email = request.json.get('email')
    user.position = request.json.get('position')
    user.speciality = request.json.get('speciality')
    user.address = request.json.get('address')
    user.hashed_password = request.json.get('address')
    user.set_password(request.json.get('password'))
    if 'modified_date' in request.json:
        user.modified_date = datetime.strptime(request.json.get('modified_date'), '%Y-%m-%d %H:%M:%S.%f')
    else:
        user.modified_date = datetime.now()
    db.add(user)
    db.commit()

    return jsonify({
        'success': 'Ok',
        'user': user.to_dict(only=('id', 'name', 'surname', 'age', 'position', 'speciality', 'address', 'email',
                                   'modified_date'))
    })


@blueprint.delete('/api/users/<int:user_id>')
def delete_user(user_id):
    db = db_session.create_session()
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        return jsonify({'error': 'Not found'})
    db.delete(user)
    db.commit()
    return jsonify({'success': 'Ok'})


@blueprint.put('/api/users/<int:user_id>')
def update_user(user_id):
    if not request.json:
        return jsonify({'error': 'Empty request'})
    db = db_session.create_session()
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        return jsonify({'error': 'Not found'})

    if 'name' in request.json:
        user.name = request.json['name']
    if 'surname' in request.json:
        user.surname = request.json['surname']
    if 'age' in request.json:
        user.age = request.json['age']
    if 'position' in request.json:
        user.position = request.json['position']
    if 'speciality' in request.json:
        user.speciality = request.json['speciality']
    if 'address' in request.json:
        user.address = request.json['address']
    if 'email' in request.json:
        user.address = request.json['email']
    if 'modified_date' in request.json:
        user.modified_date = datetime.strptime(request.json.get('modified_date'), '%Y-%m-%d %H:%M:%S.%f')
    else:
        user.modified_date = datetime.now()
    if 'password' in request.json:
        user.set_password(request.json['password'])
    db.add(user)
    db.commit()

    return jsonify({
        'success': 'Ok',
        'user': user.to_dict(only=('id', 'name', 'surname', 'age', 'position', 'speciality', 'address', 'email',
                                   'modified_date'))
    })
