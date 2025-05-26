# Registro de Alunos e Notas

alunos = []  # Lista para armazenar tuplas (nome, nota)

while True:
    nome = input("Digite o nome do aluno (ou 'fim' para encerrar): ").strip()

    if nome.lower() == 'fim':
        break

    nota_input = input(f"Digite a nota de {nome} (0 a 10): ").strip()

    try:
        nota = float(nota_input)
        if 0 <= nota <= 10:
            alunos.append((nome, nota))  # Adiciona tupla (nome, nota)
        else:
            print("Nota inválida. Digite um valor entre 0 e 10.")
    except ValueError:
        print("Entrada inválida. Digite uma nota numérica.")

# Exibição dos resultados
if alunos:
    print("\n📋 Notas da turma:")
    for nome, nota in alunos:
        print(f"- {nome}: {nota}")

    # Calcula a média
    media = sum(nota for _, nota in alunos) / len(alunos)
    print(f"\nMédia da turma: {media:.2f}")
else:
    print("Nenhum aluno foi registrado.")
