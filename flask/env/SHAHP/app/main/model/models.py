# coding: utf-8
from sqlalchemy import Column, ForeignKey, Integer, String, Table
from sqlalchemy.orm import relationship
from flask_sqlalchemy import SQLAlchemy

from .. import db



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
    interests = []
    cgpa = ''
    criminalCheck = ''
    childAbuse = ''
    CPR = ''
    immunizations = ''
    offerReceived = ''
    acceptanceForm = ''
    count =''
    activated = False

class StudentInterests(db.Model):
    __tablename__ = 'studentinterests'
    __bind_key__ = 'users'
    bannerId = db.Column(db.String(9))
    interest = db.Column(db.String(45), primary_key=True)

class StudentSupp(db.Model):
    __tablename__ = 'studentsupp'
    __bind_key__ = 'users'
    bannerId = db.Column(db.String(9), primary_key=True)
    cgpa = db.Column(db.String(45),nullable = True)
    criminalCheck = db.Column(db.String(5), nullable=False, default="false")
    childAbuse = db.Column(db.String(5), nullable=False, default="false")
    CPR = db.Column(db.String(5), nullable=False, default="false")
    immunizations = db.Column(db.String(5), nullable=False, default="false")
    offerReceived = db.Column(db.String(5), nullable=False, default="false")
    acceptanceForm = db.Column(db.String(5), nullable=False, default="false")



class Agency(db.Model):
    managed=False
    __tablename__ = 'agency'
    __bind_key__ = 'users'
    idAgency = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(45))
    type = db.Column(db.String(45))
    description = db.Column(db.String(45))
    count =''
    locations =[]
    supervisors = ''
    catgories =[]
    applicationprocedure =''

# class Job(db.Model):
#     __tablename__ = 'job'
#     __bind_key__ = 'users'
#     idJob = db.Column(db.Integer, primary_key=True)
#     idAgency = db.Column(db.Integer, nullable=False, index=True)
#     name = db.Column(db.String(45))
    # description = db.Column(db.String(45))

class Location(db.Model):
    __tablename__ = 'location'
    __bind_key__ = 'users'
    City = db.Column(db.String(45), nullable=False,primary_key=True)
    Province = db.Column(db.String(45), nullable=False)
    Address = db.Column(db.String(45), nullable=False)
    idAgency = db.Column(db.Integer, nullable=False, index=True,primary_key=True)
 
class Supervisor(db.Model):
    __tablename__ = 'supervisor'
    __bind_key__ = 'users'
    idSupervisor = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(45))
    idAgency = db.Column(db.Integer, nullable=False)
    email = db.Column(db.String(45))

class Categories(db.Model):
    __tablename__ = 'categories'
    __bind_key__ = 'users'
    idAgency = db.Column(db.Integer, nullable=False, index=True,primary_key=True)
    category = db.Column(db.String(45), nullable=False,primary_key=True)

class Applicationprocedure(db.Model):
    __tablename__ = 'applicationprocedure'
    __bind_key__ = 'users'
    idAgency = db.Column(db.Integer, nullable=False, index=True,primary_key=True)
    website = db.Column(db.String(45))
    contactDirect = db.Column(db.String(1))