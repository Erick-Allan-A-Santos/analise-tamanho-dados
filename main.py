from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def inicio():
    return "Servidor funcionando!"


@app.route("/teste", methods=["POST"])
def teste():
    dados = request.get_data()

    tamanho = len(dados)

    return f"Tamanho recebido: {tamanho} bytes"

if __name__ == "__main__":
    app.run(debug=True)