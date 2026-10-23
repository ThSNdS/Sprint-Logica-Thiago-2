numero1 = float(input("Digite o primeiro numero: "))
numero2 = float(input("Digite o segundo numero: "))

operador = input("Digite o operador (+, -, * ou /")

match operador:
    case "+":
        Resultado = numero1 + numero2
        print("Resultado:", Resultado)
    
    case "-":
        Resultado = numero1 - numero2
        print("Resultado:", Resultado)
        
    case "*":
        Resultado = numero1 * numero2
        print("Resultado:", Resultado)

    case "/":
        if numero2 != 0:
            Resultado = numero1 / numero2
            print("Resultado:", Resultado)
        else:
            print("Não pode dividir por zero! ")
    case _:
        print("Operador invalido!")