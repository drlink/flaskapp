#Opções do servidor
DEBUG = True # Live reload ativado (servidor aplica as modificações sem precisar reiniciar)

#comunicação com o banco de dados
    #dados de login
USERNAME = 'flask'
PASSWORD = 'iddqdidkfa'
SERVER = 'localhost'
DB = 'api_flask'
    #string de conexão
SQLALCHEMY_DATABASE_URI = f'mysql://{USERNAME}:{PASSWORD}@{SERVER}/{DB}'
    #Log de modificações ativado
SQLALCHEMY_TRACK_MODIFICATIONS = True