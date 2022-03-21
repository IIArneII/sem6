from sqlalchemy import Column, Integer, String, DateTime, Boolean, ForeignKey, Table
from sqlalchemy import orm
import datetime
from .db_session import SqlAlchemyBase


collaborations_table = Table('collaborations_list', SqlAlchemyBase.metadata,
                             Column('job_id', ForeignKey('job.id')),
                             Column('user_id', ForeignKey('user.id')))


members_table = Table('members_list', SqlAlchemyBase.metadata,
                      Column('department_id', ForeignKey('department.id')),
                      Column('user_id', ForeignKey('user.id')))


class Job(SqlAlchemyBase):
    __tablename__ = 'job'

    id = Column(Integer, primary_key=True, autoincrement=True, unique=True)
    team_leader = Column(Integer, ForeignKey('user.id'))
    description = Column(String)
    work_size = Column(Integer)
    collaborators = orm.relationship('User', secondary=collaborations_table, back_populates="job")
    start_date = Column(DateTime)
    end_date = Column(DateTime)
    is_finished = Column(Boolean)
    user = orm.relation('User')

    def __repr__(self):
        return f'<Job> { {self.id} } { {self.description} }'


class User(SqlAlchemyBase):
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


class Department(SqlAlchemyBase):
    __tablename__ = 'department'

    id = Column(Integer, primary_key=True, autoincrement=True, unique=True)
    title = Column(String, nullable=False)
    chief = Column(Integer, ForeignKey('user.id'))
    members = orm.relationship('User', secondary=members_table, back_populates="department")
    email = Column(String, nullable=False)
    user = orm.relation('User')
