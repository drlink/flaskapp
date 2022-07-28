from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import pymysql #correção do erro das migration sem isso as migrations não rodam
pymysql.install_as_MySQLdb()

# Configurações iniciais
app = Flask(__name__) #configuração do app
app.config.from_object('config')#chama arquivo de configuração
db =SQLAlchemy(app) #configura o banco de dados
migrate = Migrate(app, db) #configura as migrates
api = Api(app) # configuração da api
###

#importando as views para o arquivo de inicialização
from.views import curso_views
from.models import curso_model