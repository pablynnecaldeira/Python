import csv
arquivo_csv = 'pessoas.csv'

try:
    with open(arquivo_csv, newline='', encoding='utf-8') as arquivo:
        leitor = csv.DictReader(arquivo)
        print("Dados do arquivo CSV:")
        print("-" * 30)
        for linha in leitor:
            nome = linha['Nome']
            idade = linha['Idade']
            cidade = linha['Cidade']
            print(f"Nome: {nome}, Idade: {idade}, Cidade: {cidade}")
except FileNotFoundError:
    print(f"Arquivo '{arquivo_csv}' não encontrado.")
except Exception as e:
    print(f"Ocorreu um erro: {e}")
