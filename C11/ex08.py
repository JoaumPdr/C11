# Conjuntos de modelos
loja1 = {"iPhone 14", "Galaxy S23", "Xiaomi 12", "Motorola Edge"}
loja2 = {"Galaxy S23", "Xiaomi 12", "OnePlus 10", "Pixel 7"}

# Modelos disponíveis no total (união)
todos_modelos = loja1.union(loja2)
print("Modelos disponíveis no total:", todos_modelos)

# Modelos disponíveis em ambas (interseção)
modelos_comuns = loja1.intersection(loja2)
print("Modelos disponíveis em ambas as lojas:", modelos_comuns)
