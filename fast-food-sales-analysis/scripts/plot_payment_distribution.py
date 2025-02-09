import plotly.express as px
from process_data import load_and_process_data

# Carregar os dados
df = load_and_process_data()

df_payment = df["transaction_type"].value_counts().reset_index()
df_payment.columns = ["Forma de Pagamento", "Quantidade"]

fig = px.pie(df_payment, 
             names="Forma de Pagamento", 
             values="Quantidade", 
             title="💰 Distribuição das Formas de Pagamento",
             template="plotly_dark",
             color="Forma de Pagamento",
             color_discrete_map={"Cash": "gold", "Online": "blue"})

fig.show()
