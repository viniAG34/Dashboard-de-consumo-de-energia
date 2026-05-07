# EnergyAnalytics Dashboard

## Visão Geral

O **EnergyAnalytics Dashboard** é um projeto de análise de dados desenvolvido em Python com foco no monitoramento e análise inteligente do consumo de energia elétrica em ambientes corporativos e industriais.

O sistema foi projetado para automatizar o tratamento de dados energéticos, gerar indicadores estratégicos (KPIs), identificar padrões de consumo e detectar possíveis anomalias operacionais através de visualizações interativas e análises temporais.

O projeto simula um cenário real de monitoramento energético, permitindo transformar dados brutos em informações úteis para apoio à tomada de decisão e otimização de consumo.

---

# Objetivos do Projeto

- Automatizar o tratamento de dados energéticos;
- Identificar padrões e tendências de consumo;
- Detectar consumos fora do comportamento esperado;
- Gerar indicadores de desempenho energético;
- Construir visualizações analíticas para apoio à decisão;
- Demonstrar aplicação prática de análise de dados utilizando Python.

---

# Tecnologias Utilizadas

- Python
- Pandas
- NumPy
- Matplotlib
- Streamlit
- OpenPyXL

---

# Funcionalidades

## Tratamento e Limpeza de Dados

- Remoção de valores inconsistentes;
- Conversão de datas;
- Organização automática da base de dados.

## KPIs Energéticos

- Consumo total;
- Consumo médio;
- Ranking de setores;
- Crescimento de consumo;
- Identificação de maior demanda energética.

## Análise Temporal

- Evolução do consumo ao longo do tempo;
- Média móvel;
- Comparativos entre períodos.

## Detecção de Anomalias

O sistema realiza análise estatística para identificar consumos acima do comportamento esperado, auxiliando na detecção de:

- desperdícios energéticos;
- falhas operacionais;
- possíveis sobrecargas.

## Dashboard Interativo

- Upload de arquivos CSV;
- Filtros por setor;
- Visualização dinâmica;
- Gráficos automáticos.

---

# Estrutura do Projeto

```bash
EnergyAnalytics-Dashboard/
│
├── dados/
│   └── consumo_energia_1000_linhas.csv
│
├── graficos/
│   └── grafico_consumo_setor.png
│
├── src/
│   ├── tratamento.py
│   ├── analise.py
│   ├── dashboard.py
│   └── relatorio.py
│
├── requirements.txt
├── README.md
└── main.py
```

---

# Base de Dados

A base utilizada no projeto contém aproximadamente 1000 registros fictícios de consumo energético distribuídos entre diferentes setores organizacionais, simulando um ambiente corporativo real.

Os dados incluem:

- múltiplos setores;
- variações de consumo;
- tendências de crescimento;
- picos energéticos;
- anomalias simuladas.

---

# Resultados Obtidos

A análise permitiu:

- identificar os setores com maior consumo energético;
- visualizar tendências temporais;
- detectar padrões de comportamento;
- encontrar possíveis anomalias operacionais;
- automatizar o processo de análise de consumo.

---

# Como Executar

## Instalar dependências

```bash
pip install -r requirements.txt
```

## Executar análise

```bash
python main.py
```

## Executar dashboard

```bash
streamlit run src/dashboard.py
```

---

# Aplicações do Projeto

Este projeto pode ser adaptado para:

- monitoramento energético;
- gestão de utilidades;
- análise operacional;
- manutenção industrial;
- PCM;
- automação de relatórios;
- Business Intelligence (BI).

---

# Autor

Vinícius Aguiar

Pofissional com foco em:
- Análise de Dados
- Automação
- Python
- Tecnologia Industrial
