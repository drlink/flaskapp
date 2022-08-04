from flask_restful import Resource
from api import api
from ..schemas import formacao_schema
from ..entidades import formacao
from .. services import formacao_service
from flask import request, make_response, jsonify

# pesquisa
class FormacaoList(Resource):
    def get(self):
        formacoes = formacao_service.listar_formacoes()
        cs = formacao_schema.FormacaoSchema(many=True)
        return make_response(cs.jsonify(formacoes), 201)

#classe capta dados
    def post(self):
        cs = formacao_schema.FormacaoSchema()
        validate = cs.validate(request.json)
        if validate: #valida os dados
            return make_response(jsonify(validate), 400)
        else: #caso passar grava os dados
            nome = request.json["nome"]
            descricao = request.json["descricao"]

            novo_formacao = formacao.Formacao(nome=nome, descricao=descricao)
            resultado = formacao_service.cadastrar_formacao(novo_formacao)
            x = cs.jsonify(resultado)
            return make_response(x, 201)

#pesquisa formacao por id
class FormacaoDetail(Resource):
    def get(self, id):
        formacao = formacao_service.listar_formacao_id(id)
        if formacao is None:
            return make_response(jsonify("Formacao nao foi encontrado"), 404)
        cs = formacao_schema.FormacaoSchema()
        return make_response(cs.jsonify(formacao), 200)

    def put(self, id):
        formacao_bd = formacao_service.listar_formacao_id(id)
        if formacao_bd is None: #valida dados a serem enviados, caso o id não exista
            return make_response(jsonify("Formacao nao foi encontrado"), 404)
        cs = formacao_schema.FormacaoSchema()
        validate = cs.validate(request.json)
        if validate: #valida dados que são inseridos
            return make_response(jsonify(validate), 400)
        else:  # caso passar grava os dados
            nome = request.json["nome"]
            descricao = request.json["descricao"]

            novo_formacao = formacao.Formacao(nome=nome, descricao=descricao)
            formacao_service.atualiza_formacao(formacao_bd, novo_formacao)
            formacao_atualizado = formacao_service.listar_formacao_id(id)

            return make_response(cs.jsonify(formacao_atualizado), 200)

    def delete(self, id):
        formacao_db = formacao_service.listar_formacao_id(id)
        if formacao_db is None:
            return make_response(jsonify("Formacao nao encontrado"), 404)

        formacao_service.remove_formacao(formacao_db)
        return  make_response(jsonify("Formacao excluido com sucesso"), 204)



api.add_resource(FormacaoList, '/formacoes') #define a rota de saida
api.add_resource(FormacaoDetail, '/formacoes/<int:id>') #define a rota de saida Formacao detatils
