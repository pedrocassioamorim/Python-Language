# CONDICIONAIS
valor = int(input('Digite um valor: '))

# IF
if valor > 10:
    print('Valor maior que 10')
elif valor == 10:
    print('Valor igual a 10')
elif valor >= 5 and valor < 10:
    print('Valor maior que 5 e menor que 10')
else:
    print('Valor menor que 5')

# TRUTHY
print(bool(1))
print(bool("0"))

# FALSY
print(bool(0))
print(bool(""))