
from flask_restplus import Api
from flask import Blueprint

from .main.controller.user_controller import api as user_ns
from .main.controller.auth_controller import api as auth_ns
from .main.controller.admin_controller import api as admin_ns
from .main.controller.agency_controller import api as agency_ns

blueprint = Blueprint('api', __name__)

api = Api(blueprint,
          title='FLASK RESTPLUS API BOILER-PLATE WITH JWT',
          version='1.0',
          description='a boilerplate for flask restplus web service'
          )

api.add_namespace(user_ns, path='/student')
api.add_namespace(auth_ns)
api.add_namespace(admin_ns, path='/admin')
api.add_namespace(agency_ns, path='/agency')