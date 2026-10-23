renda = float(input("Digite sua renda mensal: "))
emprestimo = float(input("Digite o valor do emprestimo: "))
prestacoes = float(input("Digite o numero das prestacoes: "))

valor_das_prestacoes = emprestimo / prestacoes

if emprestimo <= renda * 0.30:
    print("Credito aprovado! ")
else:
    print("Credito negado! ")
    
print("Valor das prestacoes: R$", valor_das_prestacoes)