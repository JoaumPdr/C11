import numpy as np

# 1. Dois arrays de tamanho 8
arr1 = np.ones(8, dtype=int)
arr2 = np.random.randint(0, 10, 8)
arr3 = arr1 + arr2

print("Array 1:", arr1)
print("Array 2:", arr2)
print("Array Soma:", arr3)

# Condição
if arr3.sum() >= 40:
    arr3 = arr3.reshape(4, 2)  # mais linhas que colunas
else:
    arr3 = arr3.reshape(2, 4)  # mais colunas que linhas

print("Array remodelado:\n", arr3)
