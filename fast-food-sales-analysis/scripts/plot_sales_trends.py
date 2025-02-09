import plotly.express as px
from process_data import load_and_process_data

# Carregar os dados
df = load_and_process_data()

df_time_sales = df.groupby("time_of_sale")["transaction_amount"].sum().reset_index()

fig = px.bar(df_time_sales, 
             x="time_of_sale", 
             y="transaction_amount", 
             title="📊 Comparação de Vendas por Período do Dia",
             labels={"time_of_sale": "Período do Dia", "transaction_amount": "Faturamento"},
             text=df_time_sales["transaction_amount"],
             template="plotly_dark",
             color="transaction_amount",
             color_continuous_scale="blues")

fig.update_traces(textposition='outside')
fig.show()
