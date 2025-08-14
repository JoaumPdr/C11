# Lista inicial
times = ["Real Madrid", "Barcelona", "Atlético de Madrid", "Sevilla", "Valencia"]

# a) Apenas os 3 primeiros colocados
print("3 primeiros colocados:", times[:3])

# b) Os últimos 2 colocados
print("Últimos 2 colocados:", times[-2:])

# c) Times em ordem alfabética
print("Ordem alfabética:", sorted(times))

# d) Posição do Barcelona
posicao_barcelona = times.index("Barcelona") + 1
print("Posição do Barcelona:", posicao_barcelona)
