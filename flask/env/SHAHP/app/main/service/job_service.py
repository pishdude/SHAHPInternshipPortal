from app.main import db
from app.main.model.models import Agency,Location,Supervisor,Categories,Applicationprocedure

def get_Agencies(city,province,typ,category,searchValue,page):
    try:
        loc =False
        query = Agency.query
        print (city)
        if city is not None and city !='':
            query = query.join(Location,Location.idAgency==Agency.idAgency).filter(Location.City == city)
            loc = True
        if province is not None and province !='':
            if loc:
                query = query.filter(Location.Province == province)
            else:
                print ("here")
                query = query.join(Location,Location.idAgency==Agency.idAgency).filter(Location.Province == province)
        if typ is not None and typ !='':
            query = query.filter(Agency.type == typ)
        if category is not None and category !='':
            query = query.join(Categories,Categories.idAgency==Agency.idAgency).filter(Categories.category == category)
        if searchValue is not None and searchValue !='':
            query = query.filter(Agency.name.like("%"+searchValue+"%"))

        agencies = query.paginate(page=int(page), error_out=False, max_per_page=1 )
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
        return agencies.items
    except Exception as e:
        print (e)
        response_object = {
            'status': 'fail',
            'message': 'Some error occurred. Please try again.' + str(e)
        }
        return response_object, 400

def get_drops():
    try:
        cities =[]
        provinces =[]
        categories =[]
        types=[]
        for c in  Location.query.with_entities(Location.City).distinct():
            ca = str(c)
            cb = ca[3:len(ca)-3]
            cities.append(cb)
       
        for c in  Location.query.with_entities(Location.Province).distinct():
            ca = str(c)
            cb = ca[3:len(ca)-3]
            provinces.append(cb)
       
        for c in  Categories.query.with_entities(Categories.category).distinct():
            ca = str(c)
            cb = ca[3:len(ca)-3]
            categories.append(cb)
        
        for c in  Agency.query.with_entities(Agency.type).distinct():
            ca = str(c)
            cb = ca[3:len(ca)-3]
            types.append(cb)

       
        result = {
            'cities':cities,
            'provinces': provinces,
            'categories':categories,
            'types':types
        }
        return result
    except Exception as e:
        print (e)
        response_object = {
            'status': 'fail',
            'message': 'Some error occurred. Please try again.' + str(e)
        }
        return response_object, 400