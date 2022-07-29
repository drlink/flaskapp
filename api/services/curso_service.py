from .. models import  curso_model
from api import db

def cadastrar_curso(curso):
    curso_db = curso_model.Curso(nome=curso.nome, descricao=curso.descricao, data_publicacao=curso.data_publicacao)
    db.session.add(curso_db)
    db.session.commit()
    return curso_db