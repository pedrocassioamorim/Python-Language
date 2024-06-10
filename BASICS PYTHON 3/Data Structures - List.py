# LISTAS - estrutura de dados ordenada
notas = []
notas = [9, 10, 8.5]

print(notas[0])
notas.append(40.6)
print(notas)

notas.sort() # ORDENAR CRESCENTEMENTE
print(notas)

notas.reverse() #REVERTENDO A ORDEM DA LISTA
print(notas)

ultimo = notas.pop() #REMOVENDO O ULTIMO ELETEMENTO
print(notas)
print(ultimo)

# INSERINDO EM UMA POSIÇÃO ESPECIFICA
notas.insert(2, 70) # Index 2 , objeto: 70
print(notas)

# REMOVENDO DE UMA POSIÇÃO ESPECIFICA
notas.pop(0) # REMOVE ELEMENTO POSIÇÃO 0
print(notas)

# LISTA SIMPLES
pessoa = ["Gabriel", 27, "(91) 93879-4434"]
print(f'Nome: {pessoa[0]}')
print(f'Idade: {pessoa[1]}')
print(f'Telefone: {pessoa[2]}')

# LISTA DE LISTAS
pessoas = [
    ["Gabriel", 27, "(91) 93879-4434"],
    ["Bruno", 27, "(91) 93879-4434"],
    ["Pedro", 28, "(91) 93879-4434"],
]

notas = [9, 8.4, 8, 5.9, 2, 8.3, 2]
total = sum(notas)
media = total/len(notas)
print(total)
print(media)
for i in range(len(notas)): # LOOP FOR
    print(notas[i])


notas[2] = 100
print(notas)