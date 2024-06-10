# 01. Escreva um programa que receba um número inteiro do usuário e imprima True
# caso o número seja par e False, caso o número seja ímpar.
numero = int(input("Digite um número: \n"))
if numero % 2 == 0:
    print("Número Par!")
else:
    print("Número Impar!")

# 02. Alice é responsável por escrever um programa que verifica se um cupom de
# desconto pode ser utilizado. O programa recebe 3 valores e retorna True caso o
# cupom possa ser utilizado, ou False , caso contrário.
# Os três valores que o programa recebe são:
# 1. Valor de compra (float)
# 2. Valor do frete (float)
# 3. Cliente é cadastrado no programa de fidelidade (string “s” (sim) ou “n” (não))
# O cupom tem a seguinte regra:
# Caso o valor da compra somado ao frete seja superior a R$
# 100, ou o cliente seja cadastrado no programa de fidelidade, o
# cupom de desconto pode ser utilizado. Caso contrário, o cupom
# não pode ser utilizado.
# Seu objetivo é implementar o programa que atenda a especificação acima.

valor_de_compra = float(input("Digite o valor a ser comprado: \n"))
valor_do_frete = float(input("Digite o valor do frete: \n"))
cliente_cadastro = input("Cliente é cadastrado no Programa fidelidade? \n")
if cliente_cadastro == "s":
    fidelidade = True
else:
    fidelidade = False

if ((valor_do_frete + valor_de_compra >= 100) or (fidelidade)):
    print("O CUPOM de desconto pode ser utilizado: TOME AQUI ABC20")
else:
    print("CUPOM Inativo")

