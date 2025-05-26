print("Calculadora de Consumo de Combustível")

# Dados da viagem
distancia_percorrida = 300  # em km
combustivel_gasto = 25      # em litros

# Cálculo do consumo médio
consumo_medio = distancia_percorrida / combustivel_gasto

# Exibindo os resultados
print(f"Distância percorrida: {distancia_percorrida} km")
print(f"Combustível gasto: {combustivel_gasto} litros")
print(f"Consumo médio: {consumo_medio:.2f} km/l")