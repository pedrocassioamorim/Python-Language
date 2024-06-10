# “FizzBuzz” é um problema clássico de programação. O programa recebe um
# número inteiro e imprime:
# a. “Fizz", caso o número seja múltiplo de 3.
# b. “Buzz", caso o número seja múltiplo de 5.
# c. “FizzBuzz", caso o número seja múltiplo de 3 e de 5.
# Por exemplo:
# 3 -> "Fizz" (múltiplo de 3)
# 8 -> ... (não imprime nada)
# 10 -> "Buzz" (múltiplo de 5)
# 15 -> "FizzBuzz" (múltiplo de 3 e 5)
# 21 -> "Fizz"
# Implemente o programa FizzBuzz.

valor = int(input("Digite um número inteiro: \n"))
i = 1
while i <= valor:
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
        i = i + 1
    if i % 3 == 0:
        print("Fizz")
        i = i + 1
    if i % 5 == 0:
        print("Buzz")
        i = i + 1
    else:
        print(i)
        i = i + 1
