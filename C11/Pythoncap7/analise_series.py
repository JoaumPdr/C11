# -----------------------------------------------------------
#   ANÁLISE E DECOMPOSIÇÃO DAS SÉRIES TEMPORAIS
# -----------------------------------------------------------

import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.seasonal import seasonal_decompose

# ===========================================================
# 1. CARREGAMENTO DOS DATASETS
# ===========================================================

# Caminhos dos arquivos enviados
airtravel_path = "C:/Users/joaop/PycharmProjects/Pythoncap7/datasets/airtravel.csv"
co2_path      = "C:/Users/joaop/PycharmProjects/Pythoncap7/datasets/co2_emissions.csv"

df_air = pd.read_csv(airtravel_path)
df_co2 = pd.read_csv(co2_path)

# ===========================================================
# 2. PREPARAÇÃO DAS SÉRIES
# ===========================================================

# ------------------------------
#   AIRTRAVEL
# ------------------------------
month_column = None
for col in df_air.columns:
    if df_air[col].dtype == object:
        first_value = str(df_air[col].iloc[0]).upper()
        if first_value[:3] in ["JAN", "FEB", "MAR", "APR", "MAY", "JUN",
                               "JUL", "AUG", "SEP", "OCT", "NOV", "DEC"]:
            month_column = col
            break

if month_column is None:
    raise ValueError("Nenhuma coluna contendo nomes de meses foi encontrada no dataset AirTravel.")

print(f"Coluna detectada como meses: {month_column}")

start_year = 1958  # ano base do dataset

df_air[month_column] = pd.to_datetime(df_air[month_column] + f"-{start_year}", format="%b-%Y")
df_air.set_index(month_column, inplace=True)

# ------------------------------
#   CO2 EMISSIONS
# ------------------------------
date_column = None
for col in df_co2.columns:
    try:
        pd.to_datetime(df_co2[col])
        date_column = col
        break
    except:
        pass

if date_column is None:
    raise ValueError("Nenhuma coluna de data encontrada no arquivo co2_emissions.csv.")

print(f"Coluna de data detectada: {date_column}")

df_co2[date_column] = pd.to_datetime(df_co2[date_column])
df_co2.set_index(date_column, inplace=True)

# ===========================================================
# 3. PLOTAGEM DAS SÉRIES TEMPORAIS
# ===========================================================

plt.figure(figsize=(12,4))
plt.plot(df_air.index, df_air[df_air.columns[0]], label="Air Travel Passengers")
plt.title("Série Temporal - Air Travel")
plt.grid(True)
plt.legend()
plt.show()

plt.figure(figsize=(12,4))
plt.plot(df_co2.index, df_co2[df_co2.columns[0]], label="CO2 Emissions")
plt.title("Série Temporal - CO2 Emissions")
plt.grid(True)
plt.legend()
plt.show()

# ===========================================================
# 4. IDENTIFICAÇÃO AUTOMÁTICA DA COLUNA NUMÉRICA
# ===========================================================

# Encontrar a primeira coluna numérica no df_air
air_numeric_col = df_air.select_dtypes(include=['int64', 'float64']).columns[0]
print(f"Coluna numérica detectada no AirTravel: {air_numeric_col}")

# Encontrar a primeira coluna numérica no df_co2
co2_numeric_col = df_co2.select_dtypes(include=['int64', 'float64']).columns[0]
print(f"Coluna numérica detectada no CO2: {co2_numeric_col}")

# ===========================================================
# 5. DECOMPOSIÇÃO
# ===========================================================

decomp_air = seasonal_decompose(df_air[air_numeric_col], model="multiplicative", period=12)
decomp_air.plot()
plt.suptitle("Decomposição - Air Travel", fontsize=14)
plt.show()

decomp_co2 = seasonal_decompose(df_co2[co2_numeric_col], model="multiplicative", period=12)
decomp_co2.plot()
plt.suptitle("Decomposição - CO2 Emissions", fontsize=14)
plt.show()

# ===========================================================
# 6. RESPOSTAS A, B e C (EM COMENTÁRIOS NO PRÓPRIO CÓDIGO)
# ===========================================================

"""
=============================================================
SÉRIE 1 — AIRTRAVEL
=============================================================

a) A série possui Tendência?
   ✔ Sim. Há tendência crescente no número de passageiros.

b) A série possui Sazonalidade?
   ✔ Sim. Sazonalidade anual (12 meses).

c) A série apresenta Ciclo?
   ✔ Pequenas oscilações de longo prazo, mas não há ciclos econômicos claros.

=============================================================
SÉRIE 2 — CO2 EMISSIONS
=============================================================

a) A série possui Tendência?
   ✔ Sim. A tendência é nitidamente crescente.

b) A série possui Sazonalidade?
   ✔ Sim. Também com sazonalidade anual (12 meses).

c) A série apresenta Ciclo?
   ✔ Existem oscilações longas, mas não formam ciclos regulares.

=============================================================
"""

# Fim do código
