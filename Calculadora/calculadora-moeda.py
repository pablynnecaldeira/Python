print("Conversor de Moeda")
valor_real = 100.00

# Taxas
taxa_dolar = 5.20
taxa_euro = 6.15

# Calculo da conversão
valor_em_dolares = valor_real / taxa_dolar
valor_em_euros = valor_real / taxa_euro

# Exibindo os resultados arredondados
print(f"Valor em reais: R$ {valor_real:.2f}")
print(f"Valor em dólares: US$ {valor_em_dolares:.2f}")
print(f"Valor em euros: € {valor_em_euros:.2f}")