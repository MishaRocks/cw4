from flask_restx import Resource, Namespace

from app.container import director_service
from app.dao.models.director import DirectorSchema

director_ns = Namespace('directors')


@director_ns.route('/')
class DirectorView(Resource):
    def get(self):
        directors = director_service.get_all()
        result = DirectorSchema(many=True).dump(directors)
        return result, 200


@director_ns.route('/<int:did>')
class DirectorView(Resource):
    def get(self, did):
        director = director_service.get_one(did)
        result = DirectorSchema().dump(director)
        return result, 200
