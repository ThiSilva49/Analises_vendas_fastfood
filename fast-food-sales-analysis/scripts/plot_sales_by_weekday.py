import plotly.express as px
from process_data import load_and_process_data

# Carregar os dados
df = load_and_process_data()

df_sales_by_weekday = df.groupby("day_of_week")["transaction_amount"].sum().reset_index()

fig = px.bar(df_sales_by_weekday, 
             x="day_of_week", 
             y="transaction_amount", 
             title="📅 Faturamento por Dia da Semana",
             labels={"day_of_week": "Dia da Semana", "transaction_amount": "Faturamento"},
             template="plotly_dark",
             text=df_sales_by_weekday["transaction_amount"],
             color="transaction_amount",
             color_continuous_scale="purples")

fig.update_traces(textposition="outside")
fig.show()
