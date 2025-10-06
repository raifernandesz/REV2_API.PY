
from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def home():
    return { "Calculadora /soma, /subtrair, /multiplicar, /dividir com ?valor1= e valor2="}

@app.route("/soma")
def soma():
    v1 = float(request.args.get("valor1", 0))
    v2 = float(request.args.get("valor2", 0))
    return {"resultado": v1 + v2}

@app.route("/subtrair")
def subtrair():
    v1 = float(request.args.get("valor1", 0))
    v2 = float(request.args.get("valor2", 0))
    return {"resultado": v1 - v2}

@app.route("/multiplicar")
def multiplicar():
    v1 = float(request.args.get("valor1", 0))
    v2 = float(request.args.get("valor2", 0))
    return {"resultado": v1 * v2}

@app.route("/dividir")
def dividir():
    v1 = float(request.args.get("valor1", 0))
    v2 = float(request.args.get("valor2", 1))
    if v2 == 0:
        return {"erro": "Não pode dividir por zero"}
    return {"resultado": v1 / v2}

if __name__ == "__main__":
    # app.run(debug=True)




