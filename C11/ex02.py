numero = int(input("Digite um número para ver a tabuada: "))
inicio = int(input("Digite o início do intervalo: "))
fim = int(input("Digite o fim do intervalo: "))

print(f"\nTabuada de {numero} de {inicio} a {fim}:")
for i in range(inicio, fim + 1):
    print(f"{numero} x {i} = {numero * i}")
