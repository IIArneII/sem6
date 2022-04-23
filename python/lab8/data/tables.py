from sqlalchemy import Column, Integer, String, DateTime, Boolean, ForeignKey, Table
from sqlalchemy import orm
from sqlalchemy_serializer import SerializerMixin
from flask_login import UserMixin
import datetime
from .db_session import SqlAlchemyBase
from werkzeug.security import generate_password_hash, check_password_hash


collaborations_table = Table('collaborations_list', SqlAlchemyBase.metadata,
                             Column('job_id', ForeignKey('job.id')),
                             Column('user_id', ForeignKey('user.id')))

members_table = Table('members_list', SqlAlchemyBase.metadata,
                      Column('department_id', ForeignKey('department.id')),
                      Column('user_id', ForeignKey('user.id')))

job_to_category = Table('job_to_category', SqlAlchemyBase.metadata,
                        Column('job_id', ForeignKey('job.id')),
                        Column('category_id', ForeignKey('category.id')))


class Job(SqlAlchemyBase, SerializerMixin):
    __tablename__ = 'job'

    id = Column(Integer, primary_key=True, autoincrement=True, unique=True)
    team_leader = Column(Integer, ForeignKey('user.id'))
    description = Column(String)
    work_size = Column(Integer)

    collaborators = orm.relationship('User', secondary=collaborations_table, back_populates="job")
    categories = orm.relationship('Category', secondary=job_to_category, back_populates="jobs")

    start_date = Column(DateTime)
    end_date = Column(DateTime)
    is_finished = Column(Boolean)
    user = orm.relation('User')

    def __repr__(self):
        return f'<Job> { {self.id} } { {self.description} }'


class User(SqlAlchemyBase, UserMixin, SerializerMixin):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True, autoincrement=True, unique=True)
    surname = Column(String, nullable=False)
    name = Column(String, nullable=False)
    age = Column(Integer, nullable=False)
    position = Column(String)
    speciality = Column(String)
    address = Column(String)
    email = Column(String, nullable=False, unique=True)
    hashed_password = Column(String, nullable=False)
    modified_date = Column(DateTime, nullable=False, default=datetime.datetime.now())

    collaborators = orm.relationship('Job', secondary=collaborations_table, back_populates="user",
                                     overlaps="collaborators")

    job = orm.relation('Job', overlaps="user")
    department = orm.relation('Department', overlaps="user")

    def __repr__(self):
        return f'<Colonist> { {self.id} } { {self.surname} } { {self.name} }'

    def set_password(self, password):
        self.hashed_password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.hashed_password, password)


class Department(SqlAlchemyBase, SerializerMixin):
    __tablename__ = 'department'

    id = Column(Integer, primary_key=True, autoincrement=True, unique=True)
    title = Column(String, nullable=False)
    chief = Column(Integer, ForeignKey('user.id'))
    members = orm.relationship('User', secondary=members_table, back_populates="department")
    email = Column(String, nullable=False)
    user = orm.relation('User')


class Category(SqlAlchemyBase, SerializerMixin):
    __tablename__ = 'category'

    id = Column(Integer, primary_key=True, autoincrement=True, unique=True)
    name = Column(String)
    jobs = orm.relationship('Job', secondary=job_to_category, back_populates="categories",  overlaps="jobs")
