import pandas as pd

seriesAno1 = pd.Series({'Java': 16.25, 'C': 16.04, 'Python': 9.85})
seriesAno2 = pd.Series({'C': 16.21, 'Python': 12.12, 'Java': 11.68})

#porcentagem total
total1 = seriesAno1.sum()
total2 = seriesAno2.sum()
print(f"Porcent. ano 1: {total1:.2f}%")
print(f"Porcent. ano 2: {total2:.2f}%")

#crescimento/declinio
crescimento = seriesAno2 - seriesAno1
print("crescimento / declinio")
print(crescimento)

#crescimento de verdade (positivo)
crescimentoreal = crescimento[crescimento > 0]
print("linguagens que cresceram")
print(crescimentoreal)

#fazendo uma projeção dos 2 anos
ano3 = seriesAno2 + crescimento
ano4 = ano3 + crescimento

ling_popular = proj_ano4.nlargest(1)
print("linguagem mais popular depois dos 2 anos:")
print(ling_popular)
