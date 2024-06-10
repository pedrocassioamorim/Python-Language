# Implemente uma calculadora que recebe 3 valores do usuário:
# a. Operando a (pode ser um inteiro ou float).
# b. Operando b (pode ser um inteiro ou float).
# c. Operador op .
# i.
# pode ser uma string representando o operador, por exemplo, "+" ou "-
# ". Outra opção é utilizar números, por exemplo, 1 para soma , 2 para
# subtração , etc.
# op
# O seu programa deve receber esses 3 valores e imprimir o resultado da operação.
# Caso o operador seja de divisão e o segundo operando seja o valor zero, o
# programa deve imprimir uma mensagem: “Não é possível realizar divisão por
# zero!”.

v1 = float(input("Digite o primeiro número: \n"))
v2 = float(input("Digite o segundo número: \n"))
tipo = input("Digite o tipo de operação: \n")
resultado = 0

if (tipo == "/") and (v2 == 0.0):
    print("Não é possível realizar divisão por zero!")
elif (tipo == "*"):
    resultado = v1 * v2
elif (tipo == "+"):
    resultado = v1 + v2
elif (tipo == "-"):
    resultado = v1 - v2
elif (tipo == "/"):
    resultado = v1 / v2
print(f"Resultado: {resultado}")