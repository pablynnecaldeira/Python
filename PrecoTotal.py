print("Insira os dados para calcular o preço total: ")

nome_produto = input("Digite o nome do produto: ")
preco_unitario = float(input("Digite o preço unitário do produto (em R$): "))
quantidade = int(input("Digite a quantidade comprada: "))

preco_total = preco_unitario * quantidade

print("\n--- Detalhes da Compra ---")
print(f"Produto: {nome_produto}")
print(f"Preço Unitário: R$ {preco_unitario:.2f}")
print(f"Quantidade: {quantidade}")
print(f"Preço Total: R$ {preco_total:.2f}")