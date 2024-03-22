import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st

# Dados de exemplo (substitua pelos seus dados reais)
dados = {
    'ANO_VENDA': [2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018],
    'MES_VENDA': [10] * 19,  # Definindo o mês como 10 para todas as entradas
    'UNIDADE_MEDIDA_PRINCIPIO_ATIVO': [125, 25, 15, 2, 6, 4, 5, 1, 4, 25, 3, 5, 5, 25, 5, 5, 1, 125, 125]
}

# Crie um DataFrame a partir dos dados
df = pd.DataFrame(dados)

# Agrupe os dados por ANO_VENDA e MES_VENDA
grupo = df.groupby(['ANO_VENDA', 'MES_VENDA'])['UNIDADE_MEDIDA_PRINCIPIO_ATIVO'].sum()

# Crie o gráfico de barras
plt.figure(figsize=(10, 6))
grupo.plot(kind='bar', color='skyblue')
plt.title('Quantidade de Ativos por Unidade Farmacotécnica')
plt.xlabel('Mês de Venda')
plt.ylabel('Quantidade')
plt.xticks(rotation=0)
plt.grid(axis='y')

# Variáveis para controlar a exibição do gráfico
show_ANO_VENDA = st.button("Ano")
show_UNIDADE_MEDIDA_PRINCIPIO_ATIVO = st.button("Quantidade")

# Exiba o gráfico com base na seleção
if show_ANO_VENDA:
    st.dataframe(df['ANO_VENDA'])
elif show_UNIDADE_MEDIDA_PRINCIPIO_ATIVO:
    st.dataframe(df['UNIDADE_MEDIDA_PRINCIPIO_ATIVO'])

# Exiba o gráfico
st.pyplot(plt)