nome = input("Digite seu nome completo: ")

print("\nSeu nome em maiúsculas:", nome.upper())
print("Seu nome em minúsculas:", nome.lower())
print("Quantidade de letras (sem espaços):", len(nome.replace(" ", "")))

partes_nome = nome.split()
if len(partes_nome) > 1:
    partes_nome[-1] = "do Inatel"
    nome_trocado = " ".join(partes_nome)
    print("Nome com o último nome trocado por 'do Inatel':", nome_trocado)
else:
    print("Não foi possível trocar o último nome pois só há um nome.")
