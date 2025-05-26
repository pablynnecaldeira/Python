# Conversor de Temperatura Simples

# Entrada dos dados
temp = float(input("Digite a temperatura: "))
origem = input("Unidade de origem (C, F ou K): ").upper()
destino = input("Unidade para conversão (C, F ou K): ").upper()

# Conversão
if origem == destino:
    resultado = temp
elif origem == "C" and destino == "F":
    resultado = (temp * 9/5) + 32
elif origem == "C" and destino == "K":
    resultado = temp + 273.15
elif origem == "F" and destino == "C":
    resultado = (temp - 32) * 5/9
elif origem == "F" and destino == "K":
    resultado = (temp - 32) * 5/9 + 273.15
elif origem == "K" and destino == "C":
    resultado = temp - 273.15
elif origem == "K" and destino == "F":
    resultado = (temp - 273.15) * 9/5 + 32
else:
    resultado = None

# Saída
if resultado is not None:
    print(f"{temp}°{origem} = {resultado:.2f}°{destino}")
else:
    print("Unidade inválida. Use apenas C, F ou K.")
