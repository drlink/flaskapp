from flask import Flask, render_template


app = Flask(__name__) #importa a classe Flask e define o parametro name dentro da variavel
@app.route('/')
# 127.0.0.1:5000
def princ():
    nome = "Sr y"
    idade = 39
    feira = ["Frutas", "verdura" , "legumes", "carnes"]
    frutas = ["Morango", "Uva", "Laranja", "Mamão", "Maça","Melão","Abacaxi","pera"]
    notas = {"Aluno1": 5.0, "Aluno2": 6.0, "Aluno3": 7.0, "Aluno4": 8.5}

    return render_template("index.html", nome=nome, idade=idade, feira=feira, frutas=frutas, notas=notas)

@app.route('/sobre')
def sobre():
    return render_template('sobre.html')
