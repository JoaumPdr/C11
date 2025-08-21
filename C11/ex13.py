# 2. Arrays pares
arr_par_0_51 = np.arange(0, 52, 2)
arr_par_100_50 = np.arange(100, 49, -2)

resultado = np.concatenate([arr_par_0_51, arr_par_100_50])
resultado_ordenado = np.sort(resultado)

print("Resultado concatenado ordenado:\n", resultado_ordenado)


