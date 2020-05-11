from flask import request
from flask_restplus import Resource

from ..util.dto import StudentAdminDto
from ..service.student_service import update_student_supp,get_Student,act_stud,search_Student
from ..util.decorator import token_required
api = StudentAdminDto.api
_update = StudentAdminDto.update


@api.route('/<page>')
@api.param('page', 'Page')
class studentList(Resource):
    @api.doc('list_of_registered_students')
    @api.marshal_list_with(StudentAdminDto.student, envelope='data')
    @token_required
    def get(self,page):
        """List all registered users"""
        return get_Student(page)

@api.route('/search')
@api.param('searchValue', 'searchValue')
@api.param('searchType', 'searchType')
@api.param('page', 'Page')
class studentSearch(Resource):
    @api.doc('Search')
    @api.marshal_list_with(StudentAdminDto.student, envelope='data')
    def get(self):
        """List all registered users"""
        searchValue = request.args.get('searchValue')
        searchType = request.args.get('searchType')
        page = request.args.get('page')
        return search_Student(searchValue,searchType,page)

@api.route('/updateSupp')
@api.expect(_update, validate=True)
class LogoutAPI(Resource):
    """
    Update Student Details
    """
    @api.doc('Update Student Details')
    def post(self):
        # get auth token
        #auth_header = request.headers.get('Authorization')
        post_data = request.json
        return update_student_supp(data=post_data)

@api.route('/activateStud')
@api.expect(StudentAdminDto.activate, validate=True)
class LogoutAPI(Resource):
    """
    Update Student Details
    """
    @api.doc('Update Student Details')
    def post(self):
        # get auth token
        #auth_header = request.headers.get('Authorization')
        post_data = request.json
        return act_stud(data=post_data)