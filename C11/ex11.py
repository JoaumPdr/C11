n = int(input("Quantas pessoas deseja cadastrar? "))
idades = []
mulheres_menos_20 = 0

for _ in range(n):
    nome = input("Nome: ")
    idade = int(input("Idade: "))
    sexo = input("Sexo (M/F): ").strip().upper()
    idades.append(idade)

    if sexo == "F" and idade < 20:
        mulheres_menos_20 += 1

media_idade = sum(idades) / len(idades)

print(f"Média de idade do grupo: {media_idade:.2f}")
print(f"Quantidade de mulheres com menos de 20 anos: {mulheres_menos_20}")
