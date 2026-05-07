import pandas as pd


def carregar_dados(caminho):
    df = pd.read_csv(caminho)
    return df


def tratar_dados(df):
    df = df.dropna()
    df['Data'] = pd.to_datetime(df['Data'])
    return df