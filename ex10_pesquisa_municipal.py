import os
os.system('cls')

familias = 0
maior = 0
menor = 0
soma_salario = 0
soma_filhos = 0

while True:
    codigo = int(input('''
Escolha uma opção segundo o codigo abaixo
Código:
1 - Adicionar Família
2 - Sair e exibir resultados
'''))
    match codigo:
        case 1:
            salario = float(input('Digite o salário da família: '))
            soma_salario += salario
            filhos = int(input('Escreva o números de crianças na família: '))
            soma_filhos += filhos
            familias += 1
            if maior == 0 or salario > maior:
                maior = salario
            if menor == 0 or salario < menor:
                menor = salario
        case 2:
            media_salario = soma_salario / familias
            media_filhos = soma_filhos / familias
            print(f'O números de famílias: {familias}')
            print(f'A média de salário: {media_salario}')
            print(f'A média de filhos: {media_filhos}')
            print(f'O maior dos salário: {maior}')
            print(f'O menor dos salário: {menor}')
            break
        case _:
            print('Codigo invalido.')