# Estudo de Python flask com CI/CD

---

<p>Este repositorio tem por caracteristica estudar e simular um aplicativo<br>
web desenvolvido em python para ser utilizado em criação de esteira CI/CD de qual quer tipo.</p>

---

### 1 - Dados da aplicação<br>
**linguagem** = _python_ 3.8.10<br>
**banco de dados** = _mariadb_:10-focal<br>
**SGBD** = _adminer_:latest<br>

---

### 2 - bibliotecas e dependencias<br>  
**flask** == 2.1.2<br>
**flask-Migrate** == 2.5.2<br>
**flask-RESTful** == 0.39<br>
**SQLAlchemy** == 1.4.38<br>
**flask-SQLAlchemy** == 2.5.1<br>
**marshmallow** == 3.15.0<br>
**flask-marshmallow** == 0.14.0<br>
**mysqlclient** == 2.1.1<br>
**PyMySQL** == 1.0.2<br>

---

### 3 - Estrutura da aplicação<br>
Esta aplicação esta estruturada com base no edesign patner MVC porem com modificações <br>

Estrutura:
- **/api** _-> Contem os principais arquivos da aplicação_ 
    - **/entidades** _-> Contem os metodos gets, sets_ 
    -  **/models** _-> Contem os modelos base das estruturas de banco de dados (ORM)_
    -  **/schemas** _-> Contem as validações de dados_
    - **/services** _-> Contem os C.R.U.D.S da aplicação (ORM)_
    - **/views** _-> Contem as regras de negocio e as rotas das paginas_
    - **__ init __.py** _-> Arquivo de declaração principal da api_
    - **run.py** _-> Arquivo contem os codigos para a execução do aplicativo_
- **/migrations** _-> Contem os scripts de criaçao e versionamento da estrutura de banco de dados (ORM)_
    - **/versions** _-> Contem o script de montagen e desmontagem da estrutura de banco de dados_
- **config.py** _-> config.py => Contem as configuraçoes de variaveis da aplicaçao_

---
### 4 - Comandos para construir a aplicação
 **...**

