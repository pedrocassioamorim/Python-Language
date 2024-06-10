# WHILE
i = 1
while i <=  100:
    print(i)
    i = i + 1
print("Done")
print(i)
continuar = "S"
total = 0
while True or continuar == "S":
    valor = float(input("Digite um valor: \n"))
    total = total + valor

    cont = input("Quer continuar? [S/N] ")
    if cont != "S":
        break
print(f"Valor total: {total}")