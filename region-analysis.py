import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("Sample-Superstore.csv", encoding="latin1")

#cleaning data
df["Order Date"] = pd.to_datetime(df["Order Date"])
df["Ship Date"] = pd.to_datetime(df["Ship Date"])
df.dropna(inplace=True)
df.drop_duplicates(inplace=True)

#Plotting grafics
fig, ax = plt.subplots(figsize=(10,12))

#Profit and Sales by region
region_profits = df.groupby("Region")["Sales"].sum()
region_sales = df.groupby("Region")["Profit"].sum()

rect_profits = ax.bar(np.arange(len(region_profits.index)) - 0.2, region_profits, 0.4, label="Lucro")
rect_sales = ax.bar(np.arange(len(region_sales.index)) + 0.2, region_sales, 0.4, label="Vendas")
ax.set_xticks(np.arange(len(region_profits.index)), region_profits.index)
ax.grid(alpha=0.4)
ax.legend()

plt.show()

print(
'''
Conclusão

Leste e Oeste apresentam melhor performance tanto de vendas quanto de lucros
'''
)