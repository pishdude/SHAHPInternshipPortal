# coding: utf-8
from sqlalchemy import Column, ForeignKey, Integer, String, Table
from sqlalchemy.orm import relationship
from flask_sqlalchemy import SQLAlchemy

from .. import db



class Agency(db.Model):
    managed=False
    __tablename__ = 'agency'
    __bind_key__ = 'users'
    idAgency = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(45))
    type = db.Column(db.String(45))
    description = db.Column(db.String(45))



"""class Authtable(db.Model):
    __tablename__ = 'authtable'
    __bind_key__ = 'users'
    bannerId = db.Column(db.String(9), primary_key=True)
    password = db.Column(db.String(45), nullable=False)


class Admin(db.Model):
    __tablename__ = 'admin'
    __bind_key__ = 'users'
    adminId = db.Column(db.String(9), primary_key=True)
    name = db.Column(db.String(45), nullable=False)
    email = db.Column(db.String(45), nullable=False)
    type = db.Column(db.String(45), nullable=False)"""


class Student(db.Model):
    __tablename__ = 'student'
    __bind_key__ = 'users'
    bannerId = db.Column(db.String(9), primary_key=True)
    name = db.Column(db.String(45), nullable=False)
    email = db.Column(db.String(45), nullable=False)
    program = db.Column(db.String(45), nullable=False)
    year = db.Column(db.String(45), nullable=False)


"""class Studentsupp(Student):
    __tablename__ = 'studentsupp'

    bannerId = db.Column(db.ForeignKey(u'student.bannerId'), primary_key=True)
    cgpa = db.Column(db.String(45))
    criminalCheck = db.Column(db.String(45))



t_categories = db.Table(
    'categories',
    db.Column('idAgency', db.ForeignKey(u'agency.idAgency'), nullable=False, index=True),
    db.Column('category', db.String(45), nullable=False)
)



class Job(db.Model):
    __tablename__ = 'job'

    idJob = db.Column(db.Integer, primary_key=True)
    idAgency = db.Column(db.ForeignKey(u'agency.idAgency'), nullable=False, index=True)
    name = db.Column(db.String(45))
    description = db.Column(db.String(45))

    agency = db.relationship(u'Agency', primaryjoin='Job.idAgency == Agency.idAgency', backref=u'jobs')


class Applicationprocedure(Job):
    __tablename__ = 'applicationprocedure'

    idJob = db.Column(db.ForeignKey(u'job.idJob'), primary_key=True)
    website = db.Column(db.String(45))
    contactDirect = db.Column(db.String(1))



t_location = db.Table(
    'location',
    db.Column('City', db.String(45), nullable=False),
    db.Column('Province', db.String(45), nullable=False),
    db.Column('Address', db.String(45), nullable=False),
    db.Column('idAgency', db.ForeignKey(u'agency.idAgency'), nullable=False, index=True)
)



t_studentinterests = db.Table(
    'studentinterests',
    db.Column('bannerId', db.ForeignKey(u'student.bannerId'), nullable=False, index=True),
    db.Column('interest', db.String(45), nullable=False)
)



class Supervisor(db.Model):
    __tablename__ = 'supervisor'

    idSupervisor = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(45))
    idJob = db.Column(db.ForeignKey(u'job.idJob'), nullable=False, index=True)
    email = db.Column(db.String(45))

    job = db.relationship(u'Job', primaryjoin='Supervisor.idJob == Job.idJob', backref=u'supervisors')"""