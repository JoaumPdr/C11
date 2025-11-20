import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.seasonal import seasonal_decompose
import numpy as np

# Configuração para melhor visualização dos gráficos
plt.style.use('seaborn-v0_8-whitegrid')


def analisar_serie(caminho_arquivo, nome_serie, freq, col_data, col_valor, modelo_decomposicao='additive'):
    """
    Realiza a análise de série temporal: leitura, plotagem, decomposição e
    salva o gráfico da decomposição.
    """
    print(f"\n--- Análise da Série Temporal: {nome_serie} ---")

    # 1. Leitura e Preparação dos Dados
    # Lendo o arquivo com cabeçalho (header=0)
    df = pd.read_csv(caminho_arquivo, header=0)

    # Renomear colunas para facilitar e tratar as datas
    if 'airtravel' in caminho_arquivo:
        # airtravel.csv: Colunas originais: Date, Month, Year, Passengers
        df.columns = ['Data', 'Mes', 'Ano', 'Valor']
        # Converter a coluna de data para o formato datetime e definir como índice
        df['Data'] = pd.to_datetime(df['Data'])
    else:  # co2_emissions.csv
        # co2_emissions.csv: Colunas originais: Year, CO2_Emissions
        df.columns = ['Data', 'Valor']
        # A coluna 'Data' é o ano, vamos criar uma data de início do ano
        df['Data'] = pd.to_datetime(df['Data'].astype(str) + '-01-01')

    df = df.set_index('Data')

    # Selecionar apenas a coluna de valor e garantir que é float
    serie = df['Valor'].astype(float)

    # Ajustar a frequência da série
    serie = serie.asfreq(freq)

    # 2. Plotagem da Série Temporal Original
    plt.figure(figsize=(12, 6))
    serie.plot(title=f'Série Temporal Original: {nome_serie}')
    plt.savefig(f'{nome_serie}_original.png')
    plt.close()
    print(f"Gráfico da série original salvo como {nome_serie}_original.png")

    # 3. Decomposição da Série Temporal
    try:
        # A decomposição é feita para separar Tendência, Sazonalidade e Resíduo
        decomposicao = seasonal_decompose(serie, model=modelo_decomposicao)

        # 4. Plotagem da Decomposição
        fig, axes = plt.subplots(4, 1, figsize=(12, 10), sharex=True)

        decomposicao.observed.plot(ax=axes[0], title='Observado')
        decomposicao.trend.plot(ax=axes[1], title='Tendência')
        decomposicao.seasonal.plot(ax=axes[2], title='Sazonalidade')
        decomposicao.resid.plot(ax=axes[3], title='Resíduo')

        plt.tight_layout()
        plt.savefig(f'{nome_serie}_decomposicao.png')
        plt.close()
        print(f"Gráfico da decomposição salvo como {nome_serie}_decomposicao.png")
        print(f"Análise de {nome_serie} concluída. Verifique os gráficos e o código para as respostas detalhadas.")

    except Exception as e:
        print(f"Erro ao decompor a série {nome_serie}: {e}")
        print("Verifique se a frequência (freq) e o modelo de decomposição (modelo_decomposicao) estão corretos.")


# --- Execução da Análise ---

# 1. airtravel.csv (Passageiros de Companhias Aéreas)
# Dados mensais, a frequência é 'MS' (Month Start) e o período sazonal é 12.
# O crescimento da amplitude da sazonalidade sugere um modelo multiplicativo,
# mas vamos começar com o aditivo para a decomposição clássica e ajustar se necessário.
# Para fins de plotagem e decomposição, a frequência deve ser definida.
analisar_serie(
    caminho_arquivo="C:/Users/joaop/PycharmProjects/Pythoncap7/datasets/airtravel.csv",
    nome_serie='airtravel',
    freq='MS',
    col_data='Data',
    col_valor='Valor',
    modelo_decomposicao='multiplicative'  # Usando multiplicativo devido ao aumento da amplitude sazonal
)

# 2. co2_emissions.csv (Emissões de CO2)
# Dados anuais, a frequência é 'AS' (Annual Start).
# Séries anuais geralmente não possuem sazonalidade (período < 1 ano).
# O modelo aditivo é o padrão.
analisar_serie(
    caminho_arquivo="C:/Users/joaop/PycharmProjects/Pythoncap7/datasets/co2_emissions.csv",
    nome_serie='co2_emissions',
    freq='AS',
    col_data='Data',
    col_valor='Valor',
    modelo_decomposicao='additive'
)

      # 5. Respostas às Perguntas (em comentários no código)

        # --- co2_emissions.csv ---

# a. A série possui Tendência? Se sim, que tipo?
# Resposta: Sim, a série possui uma **Tendência de Crescimento** (ascendente).
# Isso indica que as emissões de CO2 têm aumentado consistentemente ao longo dos anos.

# b. A série possui Sazonalidade? Se sim, qual o período que ela acontece?
# Resposta: **Não**, a série não possui Sazonalidade.
# Como os dados são anuais, a sazonalidade (que é um padrão que se repete em períodos
# menores que um ano, como mensal ou trimestral) não pode ser observada ou calculada.

# c. A série apresenta um Ciclo? Se sim, por qual razão?
# Resposta: Sim, é possível que a série apresente **Ciclos** relacionados a **ciclos econômicos**
# globais (ex: recessões e expansões). Estes ciclos se manifestam como flutuações
# na tendência de longo prazo (ex: períodos de crescimento mais lento ou até queda
# seguidos por períodos de crescimento mais rápido). A razão é a correlação
# entre a atividade econômica (produção industrial, transporte) e as emissões de CO2.
# A decomposição simples pode não isolar o ciclo perfeitamente, mas a interpretação
# do domínio sugere sua presença.

   # --- co2_emissions.csv ---

# a. A série possui Tendência? Se sim, que tipo?
# Resposta: Sim, a série possui uma **Tendência de Crescimento** (ascendente).
# Isso indica que as emissões de CO2 têm aumentado consistentemente ao longo dos anos.

# b. A série possui Sazonalidade? Se sim, qual o período que ela acontece?
# Resposta: **Não**, a série não possui Sazonalidade.
# Como os dados são anuais, a sazonalidade (que é um padrão que se repete em períodos
# menores que um ano, como mensal ou trimestral) não pode ser observada ou calculada.

# c. A série apresenta um Ciclo? Se sim, por qual razão?
# Resposta: Sim, é possível que a série apresente **Ciclos** relacionados a **ciclos econômicos**
# globais (ex: recessões e expansões). Estes ciclos se manifestam como flutuações
# na tendência de longo prazo (ex: períodos de crescimento mais lento ou até queda
# seguidos por períodos de crescimento mais rápido). A razão é a correlação
# entre a atividade econômica (produção industrial, transporte) e as emissões de CO2.
# A decomposição simples pode não isolar o ciclo perfeitamente, mas a interpretação
# do domínio sugere sua presença.

