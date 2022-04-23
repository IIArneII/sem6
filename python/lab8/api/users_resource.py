from flask import jsonify
from flask_restful import Resource, abort
from lab8.data import db_session
from lab8.data.tables import User
from lab8.api.parsers import user_post_parser, user_put_parser
from datetime import datetime


def get_user_by_id(user_id):
    db = db_session.create_session()
    user = db.query(User).get(user_id)
    if not user:
        abort(404, error='Not found')
    db.close()
    return user


class UsersResource(Resource):
    @staticmethod
    def get(user_id):
        user = get_user_by_id(user_id)
        return jsonify({
            'user': user.to_dict(
                only=('id', 'name', 'surname', 'age', 'age', 'position', 'speciality', 'address', 'email',
                      'modified_date'))
        })

    @staticmethod
    def delete(user_id):
        user = get_user_by_id(user_id)
        db = db_session.create_session()
        db.delete(user)
        db.commit()
        return jsonify({'success': 'Ok'})

    @staticmethod
    def put(user_id):
        user = get_user_by_id(user_id)
        json = user_put_parser.parse_args()
        if json['name']:
            user.name = json['name']
        if json['surname']:
            user.surname = json['surname']
        if json['age']:
            user.age = json['age']
        if json['position']:
            user.position = json['position']
        if json['speciality']:
            user.speciality = json['speciality']
        if json['address']:
            user.address = json['address']
        if json['email']:
            user.address = json['email']
        if json['modified_date']:
            user.modified_date = datetime.strptime(json['modified_date'], '%Y-%m-%d %H:%M:%S.%f')
        else:
            user.modified_date = datetime.now()
        if json['password']:
            user.set_password(json['password'])
        db = db_session.create_session()
        db.add(user)
        db.commit()

        return jsonify({
            'success': 'Ok',
            'user': user.to_dict(only=('id', 'name', 'surname', 'age', 'position', 'speciality', 'address', 'email',
                                       'modified_date'))
        })


class UsersListResource(Resource):
    @staticmethod
    def get():
        db = db_session.create_session()
        users = db.query(User).all()
        return jsonify({
            'users': list(map(lambda x: x.to_dict(only=('id', 'name', 'surname', 'age', 'email')), users))
        })

    @staticmethod
    def post():
        json = user_post_parser.parse_args()
        db = db_session.create_session()
        if 'id' in json and db.query(User).filter(User.id == json['id']).first():
            return jsonify({'error': 'Id already exists'})

        user = User()
        if 'id' in json:
            user.id = json['id']
        user.name = json['name']
        user.surname = json['surname']
        user.age = json['age']
        user.email = json['email']
        user.position = json['position']
        user.speciality = json['speciality']
        user.address = json['address']
        user.set_password(json['password'])
        if json['modified_date']:
            user.modified_date = datetime.strptime(json['modified_date'], '%Y-%m-%d %H:%M:%S.%f')
        else:
            user.modified_date = datetime.now()
        db.add(user)
        db.commit()

        return jsonify({
            'success': 'Ok',
            'user': user.to_dict(only=('id', 'name', 'surname', 'age', 'position', 'speciality', 'address', 'email',
                                       'modified_date'))
        })
