import pandas as pd
import numpy as np

# Criando o DataFrame igual ao do exemplo 5.3
np.random.seed(10)
data = np.random.randint(1, 50, [5, 4])
df = pd.DataFrame(data, index=['A', 'B', 'C', 'D', 'E'], columns=['W', 'X', 'Y', 'Z'])

print(df)
print()

# fazendo a média dos elementos da coluna X que são menores do que 30
media = df[df['X'] < 30]['X'].mean()
print(f"média coluna x <30: {media:.2f}")

# fazendo a média dos elementos da linha D
media_linha_d = df.loc['D'].mean()
print(f"linha D: {media_linha_d:.2f}")

# fazendo a soma dos elementos da linha E
soma_linha = df.iloc[4].sum()
print(f"linha E: {soma_linha}")

# fazendo o slicing das linhas A, C, E e colunas X e Y
df_com_slicing = df.loc[['A', 'C', 'E'], ['X', 'Y']]
print("dataframe com slicing:")
print(df_com_slicing)
print()

# fazendfdo a soma dos elementos de cada linha
soma_linhas = sliced_df.sum(axis=1)
print("soma linhas:")
print(soma_linhas)
print()

# fazendo a soma dos elementos de cada coluna
soma_colunas = sliced_df.sum(axis=0)
print("soma colunas:")
print(soma_colunas)
