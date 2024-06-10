# Operação Relacional
# COMPARAÇÃO ==
resultado = 2 == 2
print(resultado)
print(type(resultado))

# DIFERENÇA
resultado2 = 2 != 2
print(resultado2)
print(type(resultado2))

# MAIOR ou igual
resultado3 = 2 >= 2
print(resultado3)
print(type(resultado3))


# MENOR ou igual
resultado3 = 2 <= 2
print(resultado3)
print(type(resultado3))

# NOT
idade = 16
maior_de_idade = idade >= 18
menor_de_idade = not maior_de_idade # NEGA UM VALOR - INVERTE
print(f'Idade da pessoa: {idade}')
print(f'Maior de idade: {maior_de_idade}')
print(f'Menor de idade: {menor_de_idade}')

# AND
usuario_correto = True
senha_correta = True
sucesso = usuario_correto and senha_correta
print(f'Login bem sucedido: {sucesso}')

# OR
idade_pessoa = 14
idade_minima = 16
acompanhada = True
pode_assistir = idade_pessoa > idade_minima or acompanhada
print(f'Pode assistir ao filme: {pode_assistir}')

