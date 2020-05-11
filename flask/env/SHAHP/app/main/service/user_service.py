import uuid
import datetime

from app.main import db
from app.main.model.user import User
from app.main.model.models import Student
from app.main.model.models import StudentInterests
from app.main.model.models import StudentSupp
import smtplib, ssl


def save_new_user(data):
    user = User.query.filter_by(email=data['email']).first()
    student = Student.query.filter_by(bannerId=data['bannerId']).first()
    if not user or not student:
        new_user = User(
            public_id=str(uuid.uuid4()),
            email=data['email'],
            username=data['username'],
            password=data['password'],
            registered_on=datetime.datetime.utcnow()
        )
        print(data['interests'])
        save_changes(new_user)
        return add_student(data)
    else:
        response_object = {
            'status': 'fail',
            'message': 'User already exists. Please Log in.',
        }
        return response_object, 409


def get_all_users():
    return Student.query.all()


def get_a_user(public_id):
    return User.query.filter_by(public_id=public_id).first()


def save_changes(data):
    #print(data)
    db.session.add(data)
    db.session.commit()

def generate_token(user):
    try:
        # generate the auth token
        auth_token = user.encode_auth_token(user.id)
        response_object = {
            'status': 'success',
            'message': 'Successfully registered.',
            'Authorization': auth_token.decode()
        }
        return response_object, 201
    except Exception as e:
        response_object = {
            'status': 'fail',
            'message': 'Some error occurred. Please try again.'
        }
        return response_object, 400

def add_student(data):
    try:
        new_student= Student(
            bannerId = data['bannerId'],
            name =  data['username'],
            email =  data['email'],
            program = data['program'],
            year =  data['year']
        )
        save_changes(new_student)
        
        return add_Student_Supp(data)
        # add_interests(data)
        # mail()
        # response_object = {
        #     'status': 'success',
        #     'message': 'Successfully registered.'           
        # }
        # return response_object, 201
    except Exception as e:
        response_object = {
            'status': 'fail',
            'message': 'Some error occurred in add_student. Please try again.' + str(e)
        }
        return response_object, 400

def add_Student_Supp(data):
    try:
        student_Supp = StudentSupp(
             bannerId = data['bannerId'],
             cgpa = None
        )
        
        save_changes(student_Supp)
        return add_interests(data)
        
    except Exception as e:
        response_object = {
            'status': 'fail',
            'message': 'Some error occurred in add_student. Please try again.' + str(e)
        }
        return response_object, 400 
def add_interests(data):
    try:
        for d in data['interests']:
            print(d)
            new_interest = StudentInterests(
                bannerId = data['bannerId'],
                interest  = d
            )
            save_changes(new_interest)
        mail(data['username'])
        response_object = {
            'status': 'success',
            'message': 'Successfully registered.'           
        }
        return response_object, 201
    except Exception as e:
        response_object = {
            'status': 'fail',
            'message': 'Some error occurred. Please try again.'
        }
        return response_object, 400

def mail(name):
    
    port = 465  # For SSL
    smtp_server = "smtp.gmail.com"
    sender_email = "hariarunachalam27@gmail.com"  # Enter your address
    receiver_email = "hariarunachalam27@gmail.com"  # Enter receiver address
    password = "ynwmrwprdnbhihwh"
    message = """\
    Subject: Internship portal verification

    A new student has registered. Please verify and activate """ + name

    context = ssl.create_default_context()
    server = smtplib.SMTP_SSL(smtp_server, port) 
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message)