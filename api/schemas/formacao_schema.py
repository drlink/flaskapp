from api import ma
from .. models import formacao_model
from marshmallow import fields

class FormacaoSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        # estrutura base para trabalhar com schema
        model = formacao_model.Formacao
        load_instance = True
        fields = ("id", "nome", "descricao")

    nome = fields.String(required=True)
    decricao = fields.String(requerid=True)
    