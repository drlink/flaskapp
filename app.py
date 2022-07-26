from flask import Flask, render_template, request
#

app = Flask(__name__) #importa a classe Flask e define o parametro name dentro da variavel

#Recebimento de dados variavel global
fruta2 = [] #variavel global para que o seu conteu não seja modificado a cada carregamento
registros = []
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

