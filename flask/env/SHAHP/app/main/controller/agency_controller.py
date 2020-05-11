from flask import request
from flask_restplus import Resource

from ..util.dto import AgencyDto
from ..service.job_service import get_Agencies,get_drops

api = AgencyDto.api
_agency = AgencyDto.agency
_drops = AgencyDto.drop

@api.route('/search')
@api.param('searchValue', 'searchValue')
@api.param('city', 'city')
@api.param('province', 'province')
@api.param('type', 'type')
@api.param('category', 'category')
@api.param('page', 'Page')
class studentSearch(Resource):
    @api.doc('Search')
    @api.marshal_list_with(_agency, envelope='data')
    def get(self):
        """List all registered users"""
        searchValue = request.args.get('searchValue')
        city = request.args.get('city')
        province = request.args.get('province')
        type = request.args.get('type')
        category = request.args.get('category')
        page = request.args.get('page')
        return get_Agencies(city,province,type,category,searchValue,page)

@api.route('/drops')

class getDropDowns(Resource):
    @api.doc('Search')
    # @api.marshal_with(_drops, envelope='data')
    def get(self):
        """List all registered users"""
        
        return get_drops()