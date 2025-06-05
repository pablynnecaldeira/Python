import csv

def escrever_csv(nome_arquivo, dados):
    colunas = ["Nome", "Idade", "Cidade"]
    with open(nome_arquivo, mode="w", newline= '', encoding='utf-8') as arquivo:
        escritor = csv.DictWriter(arquivo, fieldnames=colunas)
        escritor.writeheader()
        escritor.writerows(dados)

    print(f"Arquivo '{nome_arquivo}' criado com sucesso!")

dados_pessoas = [
    {"Nome": "Pablynne", "Idade": 23, "Cidade": "Brasília/DF"},
    {"Nome": "Brian", "Idade": 23, "Cidade": "RJ"},
    {"Nome": "Luciana", "Idade": 23, "Cidade": "São José dos Campos"},
]

escrever_csv("pessoas.csv", dados_pessoas)