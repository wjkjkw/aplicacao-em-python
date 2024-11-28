import os
import pandas as pd
from IPython.display import display
import plotly.express as px

lista_arquivo = os.listdir('C:/Users/aguia/Downloads/Vendas')
display(lista_arquivo)

tabela_total = pd.DataFrame()

for arquivo in lista_arquivo:
    if "Vendas" in arquivo:
        tabela = pd.read_csv(f"C:/Users/aguia/Downloads/Vendas/{arquivo}")
        tabela_total = tabela_total._append(tabela)
display(tabela_total)

tabela_produtos = tabela_total.groupby("Produto").sum()
tabela_produtos = tabela_produtos[["Quantidade Vendida"]].sort_values(
    by="Quantidade Vendida", ascending=False)
display(tabela_produtos)
tabela_total["Faturamento"] = tabela_total["Quantidade Vendida"] * \
    tabela_total["Preco Unitario"]
tabela_faturamento = tabela_total.groupby("Produto").sum()
tabela_faturamento = tabela_faturamento[["Faturamento"]].sort_values(
    by="Faturamento", ascending=False)
display(tabela_faturamento)

tabela_lojas = tabela_total.groupby("Loja").sum()
tabela_lojas = tabela_lojas[["Faturamento"]]
display(tabela_lojas)

grafico = px.bar(tabela_lojas, x=tabela_lojas.index, y="Faturamento")
grafico.show()
