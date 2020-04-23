from app.main import db
from app.main.model.user import User
from app.main.model.models import Student
from app.main.model.models import StudentInterests

def save_changes(data):
    #print(data)
    db.session.add(data)
    db.session.commit()

def get_Student():
    students = Student.query.all()
    for s in students:
        print s.bannerId
        print StudentInterests.query.filter_by(bannerId=s.bannerId)
        interests = StudentInterests.query.filter_by(bannerId=s.bannerId).all()
        print(len(interests))
        s.interests = []
        for i in interests:
            print (i)
            s.interests.append(i.interest)
    return students