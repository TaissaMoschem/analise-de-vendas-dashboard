import streamlit as st
import pandas as pd
from sqlalchemy import create_engine
import plotly.express as px

# Conecta ao banco de dados
engine = create_engine('sqlite:///data/vendas.db')
df = pd.read_sql('SELECT * FROM vendas', con=engine)

# Cria um dashboard
st.title("📊 Dashboard de Vendas")

# Exibe o dataframe
st.dataframe(df)

# Gráfico de vendas por categoria
fig = px.bar(df, x='categoria', y='total', color='categoria', title="Vendas por Categoria")
st.plotly_chart(fig)

# Exibe o total de vendas
st.metric("Total de Vendas", f"R$ {df['total'].sum():,.2f}")
