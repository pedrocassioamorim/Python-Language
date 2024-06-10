# TUPLES
# SÃO IMUTÁVEIS, NÃO PODEM SER ALTERADAS
x = (5, 10)
print(x[1])
print(type(x))

# Pessoa - Tupla
pessoa = ("Gabriel", 27, True)
pessoas = (
    (pessoa),
    ("Pedro", 29, False))

# DESEMPACOTAMENTO
nome, idade, admin = pessoa
print(nome, idade, admin)

