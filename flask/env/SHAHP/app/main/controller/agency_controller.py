from flask import request
from flask_restplus import Resource

from ..util.dto import AgencyDto
from ..service.job_service import get_Agencies

api = AgencyDto.api
_agency = AgencyDto.agency


@api.route('/search')
@api.param('searchValue', 'searchValue')
@api.param('searchType', 'searchType')
@api.param('page', 'Page')
class studentSearch(Resource):
    @api.doc('Search')
    @api.marshal_list_with(_agency, envelope='data')
    def get(self):
        """List all registered users"""
        searchValue = request.args.get('searchValue')
        searchType = request.args.get('searchType')
        page = request.args.get('page')
        return get_Agencies(page)