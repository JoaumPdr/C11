# Leitura dos dados
aluno = {}
aluno["nome"] = input("Digite o nome do aluno: ")
aluno["media"] = float(input("Digite a média do aluno: "))

# Situação
aluno["situacao"] = "AP" if aluno["media"] >= 50 else "RP"

# Mostrar dicionário
print("Dados do aluno:", aluno)
