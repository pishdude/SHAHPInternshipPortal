from flask_restplus import Namespace, fields


class UserDto:
    api = Namespace('user', description='user related operations')
    user = api.model('user', {
        'email': fields.String(required=True, description='user email address'),
        'username': fields.String(required=True, description='user username'),
        'password': fields.String(required=True, description='user password'),
        'public_id': fields.String(description='user Identifier')
    })

class AuthDto:
    api = Namespace('Auth', description='authentication related operations')
    user_auth = api.model('auth_details', {
        'email': fields.String(required=True, description='The email address'),
        'password': fields.String(required=True, description='The user password '),
    })


class StudentDto:
    api = Namespace('Student', description='Student related operations')
    student = api.model('student', {
        'email': fields.String(required=True, description='user email address'),
        'username': fields.String(required=True, description='user username'),
        'name': fields.String(required=True, description='user name'),
        'password': fields.String(required=True, description='user password'),
        'bannerId': fields.String(description='user Identifier'),
        'program': fields.String(description='user Identifier'),
        'year': fields.String(description='user Identifier'),
        'interests': fields.List(fields.String,description='user Identifier')
    })

class StudentAdminDto:
    api = Namespace('Admin', description='Admin related operations')
    student = api.model('student', {
        'email': fields.String(required=True, description='user email address'),
        'name': fields.String(required=True, description='user name'),
        'bannerId': fields.String(description='user Identifier'),
        'program': fields.String(description='user Identifier'),
        'year': fields.String(description='user Identifier'),
        'interests': fields.List(fields.String,description='user Identifier'),
        'cgpa' : fields.String(description='user Identifier'),
        'criminalCheck' : fields.String(description="criminalCheck"),
        'childAbuse' : fields.String(description="criminalCheck"),
        'CPR' : fields.String(description="criminalCheck"),
        'immunizations' : fields.String(description="criminalCheck"),
        'offerReceived' : fields.String(description="criminalCheck"),
        'acceptanceForm' : fields.String(description="criminalCheck"),
        'count' : fields.String(description="criminalCheck"),
        'activated' : fields.Boolean(description="criminalCheck")
    })

    update = api.model('student_support',{
        'bannerId': fields.String(description='user Identifier'),
        'cgpa' : fields.String(description='user Identifier'),
        'criminalCheck' : fields.String(description="criminalCheck"),
        'childAbuse' : fields.String(description="criminalCheck"),
        'CPR' : fields.String(description="criminalCheck"),
        'immunizations' : fields.String(description="criminalCheck"),
        'offerReceived' : fields.String(description="criminalCheck"),
        'acceptanceForm' : fields.String(description="criminalCheck")
    })

    activate = api.model('activate',{
        'email': fields.String(description='user Identifier')
    })

class AgencyDto:
    api = Namespace('Agency', description='Agency related operations')
    location = api.model('location',{
        'idAgency': fields.Integer(required=True, description='user email address'),
        'City': fields.String(required=True, description='user username'),
        'Province': fields.String(required=True, description='user name'),
        'Address': fields.String(required=True, description='user password'),
        
    })

    supervisor = api.model('supervisor',{
        'idSupervisor': fields.Integer(required=True, description='user email address'),
        'idAgency': fields.Integer(required=True, description='user email address'),
        'email': fields.String(required=True, description='user username'),
        'name': fields.String(required=True, description='user name'),
        
    })

    applicationprocedure = api.model('applicationprocedure',{
        'idAgency': fields.Integer(required=True, description='user email address'),
        'website': fields.String(required=True, description='user username'),
        'contactDirect': fields.String(required=True, description='user name'),
        
    })
    categories = api.model('categories',{
        'idAgency': fields.Integer(required=True, description='user email address'),
        'category': fields.String(required=True, description='user username'),
        
    })

    agency = api.model('agency', {
        'idAgency': fields.Integer(required=True, description='user email address'),
        'name': fields.String(required=True, description='user username'),
        'type': fields.String(required=True, description='user name'),
        'description': fields.String(required=True, description='user password'),
        'locations': fields.List(fields.Nested(location),description='user Identifier'),
        'supervisor':fields.Nested(supervisor),
        'categories': fields.List(fields.Nested(categories),description='user Identifier'),
        'applicationprocedure':fields.Nested(applicationprocedure),
         'count' : fields.String(description="criminalCheck"),
        # 'bannerId': fields.String(description='user Identifier'),
        # 'program': fields.String(description='user Identifier'),
        # 'year': fields.String(description='user Identifier'),
        # 'interests': fields.List(fields.String,description='user Identifier')
    
    })

    drop = api.model('drop',{
        # 'cities':fields.List(fields.String)
        'cities':fields.String()
    })
    
