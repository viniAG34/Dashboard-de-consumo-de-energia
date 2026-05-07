from src.tratamento import carregar_dados, tratar_dados
from src.analise import consumo_total, consumo_por_setor, maior_consumo
from src.relatorio import gerar_grafico


df = carregar_dados('dados/consumo_energia.csv')
df = tratar_dados(df)

print('Consumo Total:', consumo_total(df))
print('\nConsumo por Setor:')
print(consumo_por_setor(df))

print('\nMaior Consumo Registrado:')
print(maior_consumo(df))

gerar_grafico(consumo_por_setor(df))