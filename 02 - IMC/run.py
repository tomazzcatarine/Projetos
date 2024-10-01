from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/calcular_imc", methods=['POST'])  # Alterado para uma rota diferente
def calcular_imc():
    nome = request.form["nome"]
    peso = request.form["peso"]
    altura = request.form["altura"]

    imc_valor = round(float(peso) / (float(altura)** 2), 2)

    # Determinar o resultado com base no IMC
    if imc_valor < 18.5:
        resultado = "Abaixo do peso"
    elif 18.5 <= imc_valor < 24.9:
        resultado = "Peso normal"
    elif 25 <= imc_valor < 29.9:
        resultado = "Sobrepeso"
    else:
        resultado = "Obesidade"

    caminho_arquivo = 'models/imc.txt'

    with open(caminho_arquivo, 'a') as arquivo:
        arquivo.write(f"{nome};{peso};{altura};{imc_valor};{resultado};\n")

    return redirect("/")  # Redireciona para a página inicial após o cálculo

@app.route("/consultar")
def consultar_imc():
    imc_list = []
    caminho_arquivo = 'models/imc.txt'

    with open(caminho_arquivo, 'r') as arquivo:
        for linha in arquivo:
            item = linha.strip().split(';')
            imc_list.append({
                'nome': item[0],
                'peso': item[1],
                'altura': item[2],
                'imc': item[3],
                'resultado': item[4]
            })

    return render_template("consultar.html", prod=imc_list)

app.run(host='127.0.0.1', port=80, debug=True)
