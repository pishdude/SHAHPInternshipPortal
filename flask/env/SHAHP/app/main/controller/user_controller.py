from flask import request
from flask_restplus import Resource

from ..util.dto import UserDto,StudentDto,StudentAdminDto
from ..service.user_service import save_new_user, get_all_users, get_a_user
from ..service.student_service import get_Student
api = StudentDto.api
_user = UserDto.user
_student = StudentDto.student


@api.route('/')
class UserList(Resource):
    @api.response(201, 'User successfully created.')
    @api.doc('create a new user')
    @api.expect(_student, validate=True)
    def post(self):
        """Creates a new User """
        data = request.json
        return save_new_user(data=data)


# @api.route('/<public_id>')
# @api.param('public_id', 'The User identifier')
# @api.response(404, 'User not found.')
# class User(Resource):
#     @api.doc('get a user')
#     @api.marshal_with(_student)
#     def get(self, public_id):
#         """get a user given its identifier"""
#         user = get_a_user(public_id)
#         if not user:
#             api.abort(404)
#         else:
#             return user