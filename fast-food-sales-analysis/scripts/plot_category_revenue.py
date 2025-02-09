import plotly.express as px
from process_data import load_and_process_data

# Carregar os dados
df = load_and_process_data()

# Agrupar faturamento por categoria
df_category = df.groupby("item_type")["transaction_amount"].sum().reset_index()

# Criar gráfico
fig = px.bar(df_category, 
             x="item_type", 
             y="transaction_amount", 
             title="🍽 Faturamento por Categoria de Produto",
             labels={"item_type": "Categoria", "transaction_amount": "Faturamento"},
             template="plotly_dark",
             text=df_category["transaction_amount"],
             color="transaction_amount",
             color_continuous_scale="reds")

fig.update_traces(textposition="outside")
fig.show()
