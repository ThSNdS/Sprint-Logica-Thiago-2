import os
os.system('cls')

pares = 0
impares = 0
soma = 0

for i in range(5):
    numero = int(input(f'Digite o {i+1}ºnúmero: '))
    soma += numero
    if numero % 2 == 0:
        pares += 1
    else:
        impares += 1

print(f'\nExiste {pares} números pares e {impares} ímpares e a soma é {soma}.')