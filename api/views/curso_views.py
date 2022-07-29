from flask_restful import Resource
from api import api
from ..schemas import curso_schema
from ..entidades import curso
from .. services import curso_service
from flask import request, make_response, jsonify

#classe inicial para chamada de dados
class CursoList(Resource):
    def get(self):
        return "Estudando api com flask"

#cadastra os dados
    def post(self):
        cs = curso_schema.CursoSchema()
        validate = cs.validate(request.json)
        if validate: #valida os dados
            return make_response(jsonify(validate), 400)
        else: #caso passar grava os dados
            nome = request.json["nome"]
            descricao = request.json["descricao"]
            data_publicacao = request.json["data_publicacao"]

            novo_curso = curso.Curso(nome=nome, descricao=descricao, data_publicacao=data_publicacao)
            resultado = curso_service.cadastrar_curso(novo_curso)
            x = cs.jsonify(resultado)
            return make_response(x, 201)

api.add_resource(CursoList, '/cursos') #define a rota de saida dois dados