# 4. Matriz de tamanho qualquer
matriz = np.random.randint(1, 10, (3, 5))  # exemplo 3x5
linhas, colunas = matriz.shape
produto = linhas * colunas

print("Matriz:\n", matriz)
print("Linhas:", linhas, "Colunas:", colunas, "Produto:", produto)
print("Número de elementos é par" if produto % 2 == 0 else "Número de elementos é ímpar")
