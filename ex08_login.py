import os
os.system('cls')

print('Cadastre um login e senha.')
login_correto = input('Login: ')
senha_correto = input('Senha: ')
os.system('cls')

tentativas = 0

while tentativas < 3:
    login = input('Login: ')
    senha = input('Senha: ')
    if login == login_correto and senha == senha_correto:
        print('!!!Boas vindas!!!')
        break
    else:
        tentativas += 1
        print(f'Você ainda tem {3 - tentativas} chances')

