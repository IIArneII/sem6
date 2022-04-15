from flask import Blueprint, jsonify, request, make_response
from lab7.data import db_session
from lab7.data.tables import Job, User, Category
from datetime import datetime

blueprint = Blueprint('jobs_api', __name__, template_folder='templates')


@blueprint.get('/api/jobs')
def get_jobs():
    db = db_session.create_session()
    jobs = db.query(Job).all()
    return jsonify({
        'jobs': list(
            map(lambda x: x.to_dict(only=('id', 'description', 'team_leader', 'categories.id', 'categories.name')),
                jobs))
    })


@blueprint.get('/api/jobs/<int:job_id>')
def get_job(job_id):
    db = db_session.create_session()
    job = db.query(Job).filter(Job.id == job_id).first()
    if not job:
        return jsonify({'error': 'Not found'})
    return jsonify({
        'job': job.to_dict(only=('id', 'description', 'work_size', 'collaborators.id', 'collaborators.name',
                                 'collaborators.surname', 'collaborators.email', 'team_leader', 'categories.id',
                                 'categories.name', 'start_date', 'end_date', 'is_finished'))
    })


@blueprint.post('/api/jobs')
def create_job():
    if not request.json:
        return jsonify({'error': 'Empty request'})
    if not all([i in request.json for i in ['team_leader', 'description', 'work_size', 'collaborators', 'categories']]):
        return jsonify({'error': 'Bad request'})
    db = db_session.create_session()
    if 'id' in request.json and db.query(Job).filter(Job.id == request.json['id']).first():
        return jsonify({'error': 'Id already exists'})

    job = Job()
    if 'id' in request.json:
        job.id = request.json['id']
    job.team_leader = request.json.get('team_leader')
    job.description = request.json.get('description')
    job.work_size = request.json.get('work_size')
    job.is_finished = request.json.get('is_finished')
    if 'start_date' in request.json:
        job.start_date = datetime.strptime(request.json.get('start_date'), '%Y-%m-%d %H:%M:%S.%f')
    if 'end_date' in request.json:
        job.end_date = datetime.strptime(request.json.get('end_date'), '%Y-%m-%d %H:%M:%S.%f')
    for i in request.json['collaborators']:
        user = db.query(User).filter(User.id == i).first()
        job.collaborators.append(user)
    for i in request.json['categories']:
        cat = db.query(Category).filter(Category.id == i).first()
        job.categories.append(cat)
    db.add(job)
    db.commit()

    return jsonify({
        'success': 'Ok',
        'job': job.to_dict(only=('id', 'description', 'work_size', 'collaborators.id', 'collaborators.name',
                                 'collaborators.surname', 'collaborators.email', 'team_leader', 'categories.id',
                                 'categories.name', 'start_date', 'end_date', 'is_finished'))
    })


@blueprint.delete('/api/jobs/<int:job_id>')
def delete_job(job_id):
    db = db_session.create_session()
    job = db.query(Job).filter(Job.id == job_id).first()
    if not job:
        return jsonify({'error': 'Not found'})
    db.delete(job)
    db.commit()
    return jsonify({'success': 'Ok'})


@blueprint.put('/api/jobs/<int:job_id>')
def update_job(job_id):
    if not request.json:
        return jsonify({'error': 'Empty request'})
    db = db_session.create_session()
    job = db.query(Job).filter(Job.id == job_id).first()
    if not job:
        return jsonify({'error': 'Not found'})

    if 'team_leader' in request.json:
        job.team_leader = request.json['team_leader']
    if 'description' in request.json:
        job.description = request.json['description']
    if 'work_size' in request.json:
        job.work_size = request.json['work_size']
    if 'start_date' in request.json:
        job.start_date = datetime.strptime(request.json.get('start_date'), '%Y-%m-%d %H:%M:%S.%f')
    if 'end_date' in request.json:
        job.end_date = datetime.strptime(request.json.get('end_date'), '%Y-%m-%d %H:%M:%S.%f')
    if 'is_finished' in request.json:
        job.is_finished = request.json['is_finished']
    if 'collaborators' in request.json:
        job.collaborators[:] = []
        for i in request.json['collaborators']:
            user = db.query(User).filter(User.id == i).first()
            job.collaborators.append(user)
    if 'categories' in request.json:
        job.categories[:] = []
        for i in request.json['categories']:
            cat = db.query(Category).filter(Category.id == i).first()
            job.categories.append(cat)
    db.add(job)
    db.commit()

    return jsonify({
        'success': 'Ok',
        'job': job.to_dict(only=('id', 'description', 'work_size', 'collaborators.id', 'collaborators.name',
                                 'collaborators.surname', 'collaborators.email', 'team_leader', 'categories.id',
                                 'categories.name', 'start_date', 'end_date', 'is_finished'))
    })
