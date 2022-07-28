from flask_restful import Resource
from api import api

#classe inicial para chamada de dados
class CursoList(Resource):
    def get(self):
        return "Estudando api com flask"

api.add_resource(CursoList, '/cursos') #define a rota de saida dois dados