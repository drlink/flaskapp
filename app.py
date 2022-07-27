from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
import urllib.request, json, os



app = Flask(__name__) #importa a classe Flask e define o parametro name dentro da variavel
#inicializa o banco de dados
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cursos.sqlite3'
app.config['SECRET_KEY'] = "random string"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

#instancia a classe
db = SQLAlchemy(app)

#Recebimento de dados variavel global
fruta2 = [] #variavel global para que o seu conteu não seja modificado a cada carregamento
registros = []

class cursos(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(50))
    descricao = db.Column(db.String(100))
    ch = db.Column(db.Integer)

    def __init__(self, nome, descricao, ch): #metodo construtor da classe
        self.nome = nome
        self.descricao = descricao
        self.ch = ch



@app.route('/', methods=["GET", "POST"])
# 127.0.0.1:5000
def princ():
    #Envio de dados
    nome = "Sr y"
    idade = 39
    feira = ["Frutas", "verdura" , "legumes", "carnes"]
    frutas = ["Morango", "Uva", "Laranja", "Mamão", "Maça","Melão","Abacaxi","pera"]
    notas = {"Aluno1": 5.0, "Aluno2": 6.0, "Aluno3": 7.0, "Aluno4": 8.5}
    #Recebendo dados - prestar atenção o nome do que se refcebe e o nome do input e não da variavel
    if request.method == "POST":
        if request.form.get("input_form"):
            fruta2.append(request.form.get("input_form"))
    return render_template("index.html", nome=nome, idade=idade, feira=feira, frutas=frutas, notas=notas, fruta2=fruta2)


@app.route('/sobre', methods=["GET", "POST"])
def sobre():
    # Recebendo dados - prestar atenção o nome do que se recebe e o nome do input e não da variavel
    if request.method == "POST":
        if request.form.get("aluno") and request.form.get("nota"):
            registros.append({"aluno": request.form.get("aluno"), "nota": request.form.get("nota")})
    return render_template("sobre.html", registros=registros)

@app.route('/filmes/<propriedade>')
def filmes(propriedade):
    if propriedade == 'populares':
        url = "https://api.themoviedb.org/3/discover/movie?sort_by=popularity.desc&api_key=eb674176aa071860cd64f69cad582750"
    elif propriedade == 'kids':
        url = "https://api.themoviedb.org/3/discover/movie?certification_country=US&certification.lte=G&sort_by=popularity.desc&api_key=eb674176aa071860cd64f69cad582750"
    elif propriedade == '2010':
        url = "https://api.themoviedb.org/3/discover/movie?primary_release_year=2010&sort_by=vote_average.desc&api_key=eb674176aa071860cd64f69cad582750"
    elif propriedade == 'drama':
        url = "https://api.themoviedb.org/3/discover/movie?with_genres=18&sort_by=vote_average.desc&vote_count.gte=10&api_key=eb674176aa071860cd64f69cad582750"
    elif propriedade == 'tom_cruise':
        url = "https://api.themoviedb.org/3/discover/movie?with_genres=878&with_cast=500&sort_by=vote_average.desc&api_key=eb674176aa071860cd64f69cad582750"

    resp = urllib.request.urlopen(url)
    dados = resp.read()
    jsondata = json.loads(dados)
    return render_template("filmes.html", filmes=jsondata['results'])

@app.route('/cursos')
def lista_cursos():
    return render_template("cursos.html", cursos=cursos.query.all())

@app.route('/cria_curso', methods=['GET','POST'])
def cria_curso():
    nome = request.form.get('nome')
    descricao = request.form.get('descricao')
    ch = request.form.get('ch')

    if request.method == 'POST':
        if not nome or not descricao or not ch:
            flash("Preencha todos os campos do formulario","error")
            pass
        else:
            print("PASSOU NAO SEI COMO ?")
            #curso = cursos(nome, descricao, ch)
            #db.session.add(curso)
            #db.session.commit()
            return redirect(url_for('lista_cursos'))

    return render_template("novo_curso.html")

@app.route('/<int:id>/atualiza_curso', methods=['GET','POST'])
def atualiza_curso(id):
    curso = cursos.query.filter_by(id=id).first()
    if request.method == 'POST':
        nome = request.form["nome"]
        descricao = request.form["descricao"]
        ch = request.form["ch"]
        cursos.query.filter_by(id=id).update({"nome":nome, "descricao":descricao, "ch":ch})
        db.session.commit()
        return redirect(url_for('lista_cursos'))

    return render_template("atualiza_curso.html", curso=curso)


#=======================================================================================================================
if __name__ =="__main__":
    app.run(debug=True)
    if os.path.isfile('cursos.sqlite3'):
        print('Banco de dados presente OK')
    else:
        db.create_all()
        print('Criando banco de dados')