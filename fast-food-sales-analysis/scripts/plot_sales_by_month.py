import plotly.express as px
from process_data import load_and_process_data

# Carregar os dados
df = load_and_process_data()

df_sales_by_month = df.groupby("month")["transaction_amount"].sum().reset_index()

fig = px.line(df_sales_by_month, 
              x="month", 
              y="transaction_amount", 
              title="📆 Faturamento por Mês",
              labels={"month": "Mês", "transaction_amount": "Faturamento"},
              template="plotly_dark",
              markers=True)

fig.show()
