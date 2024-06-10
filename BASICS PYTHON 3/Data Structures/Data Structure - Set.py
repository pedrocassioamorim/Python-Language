# CONJUNTOS (set)
# NÃO ACEITAM ELEMENTOS REPETIDOS
usuarios = {"alice", "bob", "carol", "david"} # CRIANDO MANUALMENTE
usuarios2 = set(["pedro", "amorim", "david"]) # CRIANDO SET COM METODO SET
print(usuarios)
usuarios3 = usuarios2.union(usuarios) # UNINDO ~ JUNTANDO CONJUNTOS
usuarios4 = usuarios | usuarios2 # UNINDO ~ JUNTANDO CONJUNTOS

usuarios5 = usuarios3.intersection(usuarios2) #INTERESEÇÃO ENTRE CONJUNTOS
print(usuarios5)

usuarios6 = usuarios3.difference(usuarios2) # DIFERENÇA

eh_igual = usuarios3 == usuarios4 # COMPARANDO CONJUNTOS QUE FORAM UNIDOS
eh_igual2 = usuarios5 == usuarios3 & usuarios2 # COMPARANDO JUNTOS DE INTERSEÇÕES
eh_igual3 = usuarios6 == usuarios3 - usuarios2

usuarios.add("carol") # NÃO ACEITA ELEMENTOS REPETIDOS
print(usuarios)
print(usuarios2)
print(usuarios3)
print(usuarios4)
print(eh_igual)
print(eh_igual2)
print(usuarios5)
print(eh_igual3)
print(usuarios6)