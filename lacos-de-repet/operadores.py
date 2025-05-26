# Calculadora Básica com Tratamento de Erros

while True:
    try:
        # Solicita os dois números
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
        
        # Solicita a operação
        operacao = input("Digite a operação (+, -, *, /): ")

        # Verifica e executa a operação
        if operacao == "+":
            resultado = num1 + num2
        elif operacao == "-":
            resultado = num1 - num2
        elif operacao == "*":
            resultado = num1 * num2
        elif operacao == "/":
            if num2 == 0:
                print("Erro: divisão por zero não é permitida.")
                continue
            resultado = num1 / num2
        else:
            print("Operação inválida. Tente novamente.")
            continue

        # Mostra o resultado e encerra o loop
        print(f"Resultado: {num1} {operacao} {num2} = {resultado}")
        break

    except ValueError:
        print("Erro: entrada não numérica. Tente novamente.")