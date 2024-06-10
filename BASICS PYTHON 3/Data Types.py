# STRING
name = str("Mr. Skywalker")
name = "Mr. Skywalker"
print(name)

# INTEGER
age = 29
age = int(29)
print(age)

# FLOAT
height = 1.70
weight = float(80.2)
print("Height: " + str(height) + ", Weight: " + str(weight))  # String manipulation

# BOOLEAN
open = True
close = False
print(f" It's your name, {name}?")
print(f" And is it true that you are {age} years old?")
print(f" Yes, it's True, is the Party open?: {open}")

# SHOWING THE DATA TYPE
print(type(name))
print(type(age))
print(type(height))
print(type(weight))
print(type(open))
print(type(close))

# INPUTs
nome = input("Enter your name: ")
print(type(nome))
idade = int(input("Enter your age: "))
print(type(idade))
idade_minima = 16
if (idade >= idade_minima):
    print("Você pode assistir o filme!")
else:
    print("Você não pode assistir o filme!")