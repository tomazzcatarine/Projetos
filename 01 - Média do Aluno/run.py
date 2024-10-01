from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/", methods=['POST'])
def calcular_nota():
    nome_aluno = request.form["nome_aluno"]
    nota_1 = float(request.form["nota_1"])
    nota_2 = float(request.form["nota_2"])
    nota_3 = float(request.form["nota_3"])

    soma = nota_1 + nota_2 + nota_3
    media = round(soma / 3, 1)

    caminho_arquivo = 'models/notas.txt'

    with open(caminho_arquivo, 'a') as arquivo:
        arquivo.write(f"{nome_aluno};{nota_1};{nota_2};{nota_3};{media}\n")

    return redirect("/") # Redireciona de volta para a página inicial

@app.route("/notas")
def ver_nota():
    notas = []  # A lista começa vazia
    caminho_arquivo = 'models/notas.txt'

    with open(caminho_arquivo, 'r') as arquivo:
        for linha in arquivo:  # Usa um nome diferente para a linha
            item = linha.strip().split(';')
            notas.append({
                'nome_aluno': item[0],
                'nota_1': item[1],
                'nota_2': item[2],
                'nota_3': item[3],
                'media': item[4]
            })

    return render_template("notas.html", prod=notas)

app.run(host='127.0.0.1', port=80, debug=True)