import pandas as pd

# Carregar dataset (ajustar caminho para o arquivo correto)
df = pd.read_csv("dataset.csv")

# 1. Porcentagem de missões que deram certo
sucesso = (df['MissionStatus'] == "Success").mean() * 100
print("Porcentagem de sucesso:", sucesso, "%")

# 2. Média de gastos > 0
media_gastos = df[df['Cost'] > 0]['Cost'].mean()
print("Média de gastos:", media_gastos)

# 3. Missões dos EUA
missoes_eua = (df['Country'] == "USA").sum()
print("Missões dos EUA:", missoes_eua)

# 4. Missão mais cara da SpaceX
spacex_cara = df[df['Company'] == "SpaceX"].sort_values("Cost", ascending=False).head(1)
print("Missão mais cara da SpaceX:\n", spacex_cara)

# 5. Empresas e quantidade de missões
empresas = df['Company'].value_counts()
print("Missões por empresa:\n", empresas)
