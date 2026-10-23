import os
os.system('cls')

produto = input('Escreva o nome do produto: ')
quantidade = int(input('Digite a quantidade: '))
preco = float(input('Qual é o preço: '))

total = preco * quantidade
if quantidade <= 5:
    desconto = 0.02
    desconto1 = '2%'
elif quantidade <= 10:
    desconto = 0.03
    desconto1 = '3%'
else:
    desconto = 0.05
    desconto1 = '5%'

total1 = total * desconto
total2 = total - total1
print(f'\n O produto escolhido foi {produto} por {total} com desconto de {desconto1} dá {total2}')