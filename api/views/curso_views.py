from flask_restful import Resource
from api import api
from ..schemas import curso_schema
from ..entidades import curso
from .. services import curso_service
from flask import request, make_response, jsonify

# pesquisa
class CursoList(Resource):
    def get(self):
        cursos = curso_service.listar_cursos()
        cs = curso_schema.CursoSchema(many=True)
        return make_response(cs.jsonify(cursos), 201)
#
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

#pesquisa curso por id
class CursoDetail(Resource):
    def get(self, id):
        curso = curso_service.listar_curso_id(id)
        if curso is None:
            return make_response(jsonify("Curso nao foi encontrado"), 404)
        cs = curso_schema.CursoSchema()
        return make_response(cs.jsonify(curso), 200)

    def put(self, id):
        curso_bd = curso_service.listar_curso_id(id)
        if curso_bd is None: #valida dados a serem enviados, caso o id não exista
            return make_response(jsonify("Curso nao foi encontrado"), 404)
        cs = curso_schema.CursoSchema()
        validate = cs.validate(request.json)
        if validate: #valida dados que são inseridos
            return make_response(jsonify(validate), 400)
        else:  # caso passar grava os dados
            nome = request.json["nome"]
            descricao = request.json["descricao"]
            data_publicacao = request.json["data_publicacao"]
            novo_curso = curso.Curso(nome=nome, descricao=descricao, data_publicacao=data_publicacao)
            curso_service.atualiza_curso(curso_bd, novo_curso)
            curso_atualizado = curso_service.listar_curso_id(id)

            return make_response(cs.jsonify(curso_atualizado), 200)

    def delete(self, id):
        curso_bd = curso_service.listar_curso_id(id)
        if curso_bd is None:
            return make_response(jsonify("Curso nao encontrado"), 404)

        curso_service.remove_curso(curso_bd)
        return  make_response(jsonify("Curso excluido com sucesso"), 204)



api.add_resource(CursoList, '/cursos') #define a rota de saida
api.add_resource(CursoDetail, '/cursos/<int:id>') #define a rota de saida Curso detatils
