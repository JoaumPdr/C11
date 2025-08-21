# 5. Matriz 4x4 com seed
np.random.seed(10)
matriz = np.random.randint(1, 51, (4, 4))
print("Matriz:\n", matriz)

# a) Média linhas e colunas
media_linhas = matriz.mean(axis=1)
media_colunas = matriz.mean(axis=0)
print("Média das linhas:", media_linhas)
print("Média das colunas:", media_colunas)

# b) Maior valor das médias
print("Maior média das linhas:", media_linhas.max())
print("Maior média das colunas:", media_colunas.max())

# c) Contagem aparições
valores, contagem = np.unique(matriz, return_counts=True)
print("Contagem dos números:\n", dict(zip(valores, contagem)))
print("Números que aparecem 2 vezes:", valores[contagem == 2])