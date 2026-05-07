import streamlit as st
import pandas as pd
from tratamento import carregar_dados, tratar_dados
from analise import (
    consumo_total,
    consumo_medio,
    consumo_por_setor,
    detectar_anomalias,
    crescimento_consumo
)

st.set_page_config(page_title='Energy Analytics', layout='wide')

st.title('Sistema Inteligente de Monitoramento Energético')

arquivo = st.file_uploader('Envie uma planilha CSV', type=['csv'])

if arquivo:
    df = pd.read_csv(arquivo)
else:
    df = carregar_dados('dados/consumo_energia.csv')


df = tratar_dados(df)

st.sidebar.header('Filtros')

setores = st.sidebar.multiselect(
    'Selecione os setores',
    df['Setor'].unique(),
    default=df['Setor'].unique()
)


df = df[df['Setor'].isin(setores)]

col1, col2, col3 = st.columns(3)

col1.metric('Consumo Total', f"{consumo_total(df)} kWh")
col2.metric('Consumo Médio', f"{consumo_medio(df)} kWh")
col3.metric('Crescimento', f"{crescimento_consumo(df)}%")

st.subheader('Ranking de Consumo por Setor')
st.bar_chart(consumo_por_setor(df))

st.subheader('Consumo ao Longo do Tempo')
st.line_chart(df.groupby('Data')['Consumo_kWh'].sum())

anomalias = detectar_anomalias(df)

st.subheader('Possíveis Anomalias Detectadas')
st.dataframe(anomalias)