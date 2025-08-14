pessoas = []
for i in range(3):
    nome = input(f"Digite o nome da {i+1}ª pessoa: ")
    peso = float(input(f"Digite o peso de {nome}: "))
    pessoas.append((nome, peso))

mais_pesado = max(pessoas, key=lambda x: x[1])
mais_leve = min(pessoas, key=lambda x: x[1])

print("Mais pesado:", mais_pesado[0])
print("Mais leve:", mais_leve[0])
