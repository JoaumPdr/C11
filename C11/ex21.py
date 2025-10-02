# ============================
# RESOLUÇÃO DOS 3 EXERCÍCIOS
# ============================

import pandas as pd
import matplotlib.pyplot as plt

# ---------- Exercício 1 ----------
# Já carregamos paises.csv anteriormente
americas_norte = paises[paises["Region"].str.contains("NORTHERN AMERICA", case=False)]

plt.figure(figsize=(12,6))
plt.plot(americas_norte["Country"], americas_norte["Deathrate"], label="Taxa de Mortalidade (Deathrate)", marker="o")
plt.plot(americas_norte["Country"], americas_norte["Birthrate"], label="Taxa de Natalidade (Birthrate)", marker="o")

plt.title("Exercício 1 - Taxa de Mortalidade vs Natalidade - América do Norte")
plt.xlabel("País")
plt.ylabel("Taxa")
plt.xticks(rotation=45)
plt.legend()
plt.grid(True)
plt.show()


# ---------- Exercício 2 ----------
# Carregar space.csv com delimitador correto
space = pd.read_csv("/mnt/data/space.csv", delimiter=";")

# Extrair país da coluna Location (última palavra)
space["Country"] = space["Location"].apply(lambda x: x.split()[-1])

# Contar quantas empresas espaciais diferentes EUA e China possuem
empresas_eua = space[space["Country"] == "USA"]["Company Name"].unique()
empresas_china = space[space["Country"] == "China"]["Company Name"].unique()

dados_empresas = {
    "EUA": len(empresas_eua),
    "China": len(empresas_china)
}

plt.figure(figsize=(6,5))
plt.bar(dados_empresas.keys(), dados_empresas.values(), color=["blue", "red"])
plt.title("Exercício 2 - Empresas Espaciais Diferentes (EUA vs China)")
plt.ylabel("Quantidade de Empresas")
plt.show()


# ---------- Exercício 3 ----------
# Filtrar apenas a empresa Roscosmos
roscosmos = space[space["Company Name"].str.contains("Roscosmos", case=False)]

# Contar sucessos e falhas
status_missoes = roscosmos["Status Mission"].value_counts()

plt.figure(figsize=(6,6))
plt.pie(status_missoes, labels=status_missoes.index, autopct="%1.1f%%", startangle=90, colors=["green", "red"])
plt.title("Exercício 3 - Sucesso vs Falha das Missões Roscosmos")
plt.show()
