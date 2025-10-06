
# from flask import Flask

# app = Flask(__name__)

# @app.route("/")
# def numbers():
#     return "Seja bem vindo"

# @app.route("/calculator/somar/<int:num1>/<int:num2>")
# def somar(num1, num2):
#     resultado = num1 + num2
#     return f"A soma de {num1} + {num2} = {resultado}"

# @app.route("/calculator/subtração/<int:num1>/<int:num2>")
# def subtrair(num1, num2):
#     resultado = num1 - num2
#     return f"A subtração de {num1} - {num2} = {resultado}"

# @app.route("/calculator/multiplicação/<int:num1>/<int:num2>")
# def multiplicar(num1, num2):
#     resultado = num1 * num2
#     return f"A multiplicação de {num1} * {num2} = {resultado}"

# @app.route("/calculadora/divisao/<int:n1>/<int:n2>")
# def divisao(n1,n2):
#     # resultado = n1 + n2
#     if n2 == 0:
#         return f'Esta invalido'
#     else:
#         return f'Somando os valores {n1} e {n2} = {n1 / n2}'

# if __name__ == "__main__":
#     app.run(debug=True)











# from flask import Flask, request

# app = Flask(__name__)

# @app.route("/")
# def home():
#     return {"msg": "Calculadora /soma, /subtrair, /multiplicar, /dividir com ?valor1= e valor2="}

# @app.route("/soma")
# def soma():
#     v1 = float(request.args.get("valor1", 0))
#     v2 = float(request.args.get("valor2", 0))
#     return {"resultado": v1 + v2}

# @app.route("/subtrair")
# def subtrair():
#     v1 = float(request.args.get("valor1", 0))
#     v2 = float(request.args.get("valor2", 0))
#     return {"resultado": v1 - v2}

# @app.route("/multiplicar")
# def multiplicar():
#     v1 = float(request.args.get("valor1", 0))
#     v2 = float(request.args.get("valor2", 0))
#     return {"resultado": v1 * v2}

# @app.route("/dividir")
# def dividir():
#     v1 = float(request.args.get("valor1", 0))
#     v2 = float(request.args.get("valor2", 1))
#     if v2 == 0:
#         return {"erro": "Não pode dividir por zero"}
#     return {"resultado": v1 / v2}

# if __name__ == "__main__":
#     # app.run(debug=True)



