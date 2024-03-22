import streamlit as st
import pandas as pd
import numpy as np

# Carrega o arquivo CSV
dados = 'dados_medicamentos_2014.csv'
df = pd.read_csv(dados, encoding='utf-8')

# Crie um gráfico de barras com os dados do DataFrame
st.bar_chart(df)