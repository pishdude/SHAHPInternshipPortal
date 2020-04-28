from app.main import db
from app.main.model.models import Agency,Location,Supervisor,Categories,Applicationprocedure

def get_Agencies(page):
    try:
        agencies = Agency.query.paginate(page=int(page), error_out=False, max_per_page=10 )
        for a in agencies.items:
            print a.idAgency
            a.count = agencies.total
            locations = Location.query.filter_by(idAgency=a.idAgency).all()
            print(len(locations))
            a.locations = []
            for l in locations:
                print (l)
                a.locations.append(l)
            supervisor = Supervisor.query.filter_by(idAgency=a.idAgency).first()
            a.supervisor = supervisor
            categories = Categories.query.filter_by(idAgency=a.idAgency).all()
            a.categories = []
            for c in categories:
                print (c)
                a.categories.append(c)
            applicationprocedure = Applicationprocedure.query.filter_by(idAgency=a.idAgency).first()
            a.applicationprocedure = applicationprocedure
        #     flags  = StudentSupp.query.filter_by(bannerId=s.bannerId).first()
        #     s.cgpa = flags.cgpa
        #     s.criminalCheck = flags.criminalCheck
        #     s.childAbuse = flags.childAbuse
        #     s.CPR = flags.CPR
        #     s.immunizations = flags.immunizations
        #     s.offerReceived = flags.offerReceived
        #     s.acceptanceForm = flags.acceptanceForm

        #     user = User.query.filter_by(email = s.email).first()
        #     s.activated = user.activated

        return agencies.items
    except Exception as e:
        print (e)
        response_object = {
            'status': 'fail',
            'message': 'Some error occurred. Please try again.' + str(e)
        }
        return response_object, 400