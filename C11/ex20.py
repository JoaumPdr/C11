import pandas as pd

# 1. Carregar o dataset
df = pd.read_csv("paises.csv")

print("\n=== EXERCÍCIO 1 ===")
# a) Países da Oceania
paises_oceania = df[df['Region'].str.contains("OCEANIA", case=False, na=False)]['Country']
print("Países da Oceania:")
print(paises_oceania.to_string(index=False))

# b) Quantidade de países da Oceania
quantidade_oceania = paises_oceania.count()
print("\nQuantidade de países da Oceania:", quantidade_oceania)


print("\n=== EXERCÍCIO 2 ===")
# País com maior população
pais_max_pop = df.loc[df['Population'].idxmax(), ['Country', 'Region', 'Population']]
print("País com maior população:")
print(pais_max_pop)


print("\n=== EXERCÍCIO 3 ===")
# Média de alfabetização por região
media_literacy = df.groupby('Region')['Literacy (%)'].mean()
print("Média de alfabetização por região:")
print(media_literacy)


print("\n=== EXERCÍCIO 4 ===")
# Países sem costa marítima
no_coast = df[df['Coastline (coast/area ratio)'] == 0][['Country']]
print("Países sem costa marítima:")
print(no_coast.to_string(index=False))

# Salvar em arquivo
no_coast.to_csv("noCoast.csv", index=False)
print("\nArquivo 'noCoast.csv' salvo com sucesso!")


print("\n=== EXERCÍCIO 5 ===")
# Função para classificar taxa de mortalidade
def help_status(deathrate):
    return "Balanced" if deathrate < 9 else "Urgent"

# Criar coluna Humanitarian Help
df['Humanitarian Help'] = df['Deathrate'].apply(help_status)

print("Dataset atualizado com coluna 'Humanitarian Help':")
print(df[['Country', 'Deathrate', 'Humanitarian Help']].head())
