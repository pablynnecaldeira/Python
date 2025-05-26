# Programa: Calculadora de IMC

# Solicita os dados do usuário
peso = float(input("Digite seu peso em kg: "))
altura = float(input("Digite sua altura em metros: "))

# Verifica se os valores são válidos
if peso <= 0 or altura <= 0:
    print("Peso e altura devem ser valores positivos.")
else:
    imc = peso / (altura ** 2)

    # Classifica o IMC
    if imc < 18.5:
        classificacao = "Abaixo do peso"
    elif imc < 25:
        classificacao = "Peso normal"
    elif imc < 30:
        classificacao = "Sobrepeso"
    else:
        classificacao = "Obeso"

    # Exibe o resultado
    print(f"Seu IMC é: {imc:.2f}")
    print(f"Classificação: {classificacao}")
