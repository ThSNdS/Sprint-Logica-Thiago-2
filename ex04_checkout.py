import os
os.system('cls')

valor = float(input('Digite o valor combinado: '))
forma = input('Escreva a forma de pagamento [Atenção 1 pra vista e 2 para a prazo]: ')

match forma:
    case '1':
        bonus = 'vista'
        desconto = valor * 0.1
        desconto1 = '10%'
        valor_total = valor - desconto
    case '2':
        bonus = 'prazo'
        parcelas = int(input('Quantas parcelas deseja pagar: '))
        if parcelas < 0:
            print('Numero invalido')
        else:
            valor_total = valor / parcelas
    case _:
        print('Opção invalida.')

if bonus == 'vista':
    print(f'\nO valor: {valor}')
    print(f'\nO forma de pagamento: {bonus}')
    print(f'\nO {bonus} de {desconto1}')
    print(f'\nO valor final: {valor_total}')
elif bonus == 'prazo':
    print(f'\nO valor: {valor}')
    print(f'\nO forma de pagamento: {bonus}')
    print(f'\nO pagemento devido em {parcelas} parcelas.')
    print(f'\nO valor final: {valor_total}')