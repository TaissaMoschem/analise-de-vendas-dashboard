import streamlit as st
import pandas as pd
from sqlalchemy import create_engine
import plotly.express as px

# Configuração da página
st.set_page_config(page_title="Dashboard de Vendas", page_icon="📊", layout="wide")

# Conectar ao banco de dados SQLite
engine = create_engine('sqlite:///data/vendas.db')
df = pd.read_sql('SELECT * FROM vendas', con=engine)

# Criando KPIs
total_vendas = df["total"].sum()
produto_mais_vendido = df.groupby("produto")["quantidade"].sum().idxmax()
categoria_mais_lucrativa = df.groupby("categoria")["total"].sum().idxmax()

# Layout do dashboard
st.title("📊 Dashboard de Vendas")

# Criar colunas para KPIs
col1, col2, col3 = st.columns(3)
col1.metric("💰 Total de Vendas", f"R$ {total_vendas:,.2f}")
col2.metric("🏆 Produto Mais Vendido", produto_mais_vendido)
col3.metric("🔥 Categoria Mais Lucrativa", categoria_mais_lucrativa)

st.divider()  # Linha separadora

# Criar um filtro por categoria
categorias = df["categoria"].unique()
categoria_selecionada = st.selectbox("🔍 Filtrar por Categoria", ["Todas"] + list(categorias))

# Aplicar filtro
if categoria_selecionada != "Todas":
    df_filtrado = df[df["categoria"] == categoria_selecionada]
else:
    df_filtrado = df

# Criar gráficos interativos
col1, col2 = st.columns(2)

# Gráfico de vendas por categoria
fig1 = px.bar(df_filtrado, x="categoria", y="total", color="categoria",
              title="💵 Total de Vendas por Categoria", text_auto=True)
col1.plotly_chart(fig1, use_container_width=True)

# Gráfico de quantidade de produtos vendidos por categoria
fig2 = px.bar(df_filtrado, x="categoria", y="quantidade", color="categoria",
              title="📦 Quantidade Vendida por Categoria", text_auto=True)
col2.plotly_chart(fig2, use_container_width=True)

# Exibir tabela com os dados filtrados
st.subheader("📋 Dados de Vendas")
st.dataframe(df_filtrado)

# Mensagem final
st.markdown("💡 *Dica: Utilize os filtros para visualizar os dados com mais detalhes!*")