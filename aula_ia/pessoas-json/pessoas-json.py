import json
arquivo_json = 'pessoa.json'

# Dados a serem escritos
dados_pessoa = {
    "nome": "João",
    "idade": 35,
    "cidade": "Belo Horizonte"
}

# Dados no arquivo JSON
with open(arquivo_json, 'w', encoding='utf-8') as arquivo:
    json.dump(dados_pessoa, arquivo, ensure_ascii=False, indent=4)
    print("✅ Dados salvos no arquivo JSON com sucesso!")

# Ler os dados do arquivo JSON
try:
    with open(arquivo_json, 'r', encoding='utf-8') as arquivo:
        dados_lidos = json.load(arquivo)
        print("\n📄 Dados lidos do arquivo JSON:")
        print(f"Nome: {dados_lidos['nome']}")
        print(f"Idade: {dados_lidos['idade']}")
        print(f"Cidade: {dados_lidos['cidade']}")
except FileNotFoundError:
    print(f"❌ Arquivo '{arquivo_json}' não encontrado.")
except json.JSONDecodeError:
    print("❌ Erro ao decodificar o arquivo JSON.")
