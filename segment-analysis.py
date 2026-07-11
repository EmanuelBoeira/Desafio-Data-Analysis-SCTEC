import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("Sample-Superstore.csv", encoding="latin1")

#cleaning data
df["Order Date"] = pd.to_datetime(df["Order Date"])
df["Ship Date"] = pd.to_datetime(df["Ship Date"])
df.dropna(inplace=True)
df.drop_duplicates(inplace=True)

#Analysis of profit and sales by segment
fig, ax = plt.subplots(1,2)

#Profit by segment plot
segments_profits = df.groupby("Segment")["Profit"].sum()

rects1 = ax[0].bar(segments_profits.index, segments_profits, 0.4, label="Lucro")
ax[0].set_title("Lucro por segmento")
ax[0].set_ylabel("Lucro (US$)")


#Sales by region plot 
consumers_group = df.groupby("Segment").get_group("Consumer")
consumers_group_sales = consumers_group.groupby("Region")["Sales"].sum()

rect_sales = ax[1].bar(consumers_group_sales.index, consumers_group_sales, 0.4, label="Vendas")
ax[1].set_title("Vendas por segmento")
ax[1].set_ylabel(" Vendas (US$)")

fig.tight_layout()

plt.show()

print(
'''
Conclusão

O seguimento de maior lucro é o de consumo pessoal(Consumer), portanto seria interressante dar maior atenção a este seguimento 
Neste seguimento, as regiões Leste e Oeste apresentam mais vendas
'''
)