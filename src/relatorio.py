import matplotlib.pyplot as plt


def gerar_grafico(consumo_setor):
    consumo_setor.plot(kind='bar')
    plt.title('Consumo por Setor')
    plt.xlabel('Setores')
    plt.ylabel('kWh')
    plt.tight_layout()
    plt.savefig('graficos/consumo_setor.png')