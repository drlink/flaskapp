from flask_restful import Resource
from api import api
from ..schemas import curso_schema
from ..entidades import curso
from .. services import curso_service
from flask import request, make_response, jsonify

#classe retorna os dados
class CursoList(Resource):
    def get(self):
        cursos = curso_service.listar_cursos()
        cs = curso_schema.CursoSchema(many=True)
        return make_response(cs.jsonify(cursos), 201)

#classe capta dados
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