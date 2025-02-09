import plotly.graph_objects as go
from process_data import load_and_process_data

# Carregar os dados
df = load_and_process_data()

# Itens mais vendidos (quantidade e receita)
top_items_qty = df.groupby("item_name")["quantity"].sum().sort_values(ascending=False).head(10).reset_index()
top_items_revenue = df.groupby("item_name")["transaction_amount"].sum().sort_values(ascending=False).head(10).reset_index()

fig = go.Figure()

# Quantidade vendida
fig.add_trace(go.Bar(
    x=top_items_qty["item_name"], 
    y=top_items_qty["quantity"], 
    name="Quantidade Vendida",
    marker_color="orange"
))

# Receita total
fig.add_trace(go.Bar(
    x=top_items_revenue["item_name"], 
    y=top_items_revenue["transaction_amount"], 
    name="Faturamento",
    marker_color="blue"
))

fig.update_layout(
    title="🍔 Comparação de Itens Mais Vendidos (Quantidade x Receita)",
    xaxis_title="Item",
    yaxis_title="Valores",
    barmode="group",
    template="plotly_dark"
)

fig.show()
