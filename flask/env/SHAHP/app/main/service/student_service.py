from app.main import db
from app.main.model.user import User
from app.main.model.models import Student
from app.main.model.models import StudentInterests
from app.main.model.models import StudentSupp

def save_changes(data):
    #print(data)
    db.session.add(data)
    db.session.commit()

def get_Student(page):
    try:
        students = Student.query.paginate(page=int(page), error_out=False, max_per_page=1 )
        for s in students.items:
            print s.bannerId
            print StudentInterests.query.filter_by(bannerId=s.bannerId)
            
            s.count = students.total
            
            interests = StudentInterests.query.filter_by(bannerId=s.bannerId).all()
            print(len(interests))
            s.interests = []
            for i in interests:
                print (i)
                s.interests.append(i.interest)
            
            flags  = StudentSupp.query.filter_by(bannerId=s.bannerId).first()
            s.cgpa = flags.cgpa
            s.criminalCheck = flags.criminalCheck
            s.childAbuse = flags.childAbuse
            s.CPR = flags.CPR
            s.immunizations = flags.immunizations
            s.offerReceived = flags.offerReceived
            s.acceptanceForm = flags.acceptanceForm

            user = User.query.filter_by(email = s.email).first()
            s.activated = user.activated

        return students.items
    except Exception as e:
        print (e)
        response_object = {
            'status': 'fail',
            'message': 'Some error occurred. Please try again.' + str(e)
        }
        return response_object, 400

def update_student_supp(data):
    try:
        stud = StudentSupp.query.get(data['bannerId'])
        stud.cgpa = data['cgpa']
        stud.criminalCheck = data['criminalCheck']
        stud.childAbuse = data['childAbuse']
        stud.CPR = data['CPR']
        stud.immunizations = data['immunizations']
        stud.offerReceived = data['offerReceived']
        stud.acceptanceForm = data['acceptanceForm']
        db.session.commit()
        response_object = {
            'status': 'success',
            'message': 'Successfully updated.'
            
        }
        return response_object, 200

    except Exception as e:
        response_object = {
            'status': 'fail',
            'message': 'Some error occurred. Please try again.' +str (e)
        }
        return response_object, 401

def act_stud(data):
    try:
        stud = User.query.filter_by(email=data['email']).first()
        stud.activated = not(stud.activated)
        db.session.commit()
        response_object = {
            'status': 'success',
            'message': 'Successfully updated.'
            
        }
        return response_object, 200
    except Exception as e:
        response_object = {
            'status': 'fail',
            'message': 'Some error occurred. Please try again.'+ str (e)
        }
        return response_object, 401

def search_Student(searchValue,searchType,page):
    try:
        print(searchType)
        if(searchValue is None):
            searchValue =''
        searchValue = str(searchValue).lower()
        
        #searchValue = 'b00832133'
        if(searchType=='false'):
            students = Student.query.filter(Student.bannerId.like("%"+searchValue+"%")).paginate(page=int(page), error_out=False, max_per_page=1 )
        else:
            students = Student.query.filter(Student.name.like("%"+searchValue+"%")).paginate(page=int(page), error_out=False, max_per_page=1 )
        for s in students.items:
            print s.bannerId
            print StudentInterests.query.filter_by(bannerId=s.bannerId)
            
            s.count = students.total
            
            interests = StudentInterests.query.filter_by(bannerId=s.bannerId).all()
            print(len(interests))
            s.interests = []
            for i in interests:
                print (i)
                s.interests.append(i.interest)
            
            flags  = StudentSupp.query.filter_by(bannerId=s.bannerId).first()
            s.cgpa = flags.cgpa
            s.criminalCheck = flags.criminalCheck
            s.childAbuse = flags.childAbuse
            s.CPR = flags.CPR
            s.immunizations = flags.immunizations
            s.offerReceived = flags.offerReceived
            s.acceptanceForm = flags.acceptanceForm

            user = User.query.filter_by(email = s.email).first()
            s.activated = user.activated

        return students.items
    except Exception as e:
        print (e)
        response_object = {
            'status': 'fail',
            'message': 'Some error occurred. Please try again.' + str(e)
        }
        return response_object, 400
