
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
