from api import ma
from .. models import curso_model
from marshmallow import fields

class CursoSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        # estrutura base para trabalhar com schema
        model = curso_model.Curso
        load_instance = True
        fields = ("id", "nome", "descricao", "data_publicacao")

    nome = fields.String(required=True)
    decricao = fields.String(requerid=True)
    data_publicacao = fields.Date(required=True)