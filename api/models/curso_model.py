from api import db
from ..models import formacao_model

class Curso(db.Model):
    __tablename__ = "curso"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    nome = db.Column(db.String(50), nullable=False)
    descricao = db.Column(db.String(100), nullable=False)
    data_publicacao = db.Column(db.Date, nullable=False)
    #Chave estrngeira que relaciona a formação com o curso
    formacao_id = db.Column(db.Integer, db.ForeignKey('formacao.id'))
    formacao = db.relationship(formacao_model.Formacao, backref=db.backref("curso", lazy="dynamic"))