import pandas as pd


def consumo_total(df):
    return df['Consumo_kWh'].sum()


def consumo_medio(df):
    return round(df['Consumo_kWh'].mean(), 2)


def consumo_por_setor(df):
    return df.groupby('Setor')['Consumo_kWh'].sum().sort_values(ascending=False)


def maior_consumo(df):
    return df.loc[df['Consumo_kWh'].idxmax()]


def media_movel(df):
    df = df.sort_values('Data')
    df['Media_Movel'] = df['Consumo_kWh'].rolling(window=7).mean()
    return df


def detectar_anomalias(df):
    media = df['Consumo_kWh'].mean()
    desvio = df['Consumo_kWh'].std()

    limite = media + (2 * desvio)

    anomalias = df[df['Consumo_kWh'] > limite]

    return anomalias


def crescimento_consumo(df):
    consumo_inicial = df.iloc[0]['Consumo_kWh']
    consumo_final = df.iloc[-1]['Consumo_kWh']

    crescimento = ((consumo_final - consumo_inicial) / consumo_inicial) * 100

    return round(crescimento, 2)