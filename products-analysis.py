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
fig, ax = plt.subplots(3,1, figsize=(10,12))

#Sales by category
categories_sales = df.groupby("Category")["Sales"].sum()

rect_sales = ax[0].bar(categories_sales.index, categories_sales, 0.4, label="Vendas")
ax[0].set_title("Vendas por categoria")

#Profit by category
categories_profit = df.groupby("Category")["Profit"].sum()

rect_profit = ax[1].bar(categories_profit.index, categories_profit, 0.4, label="Lucro")
ax[1].set_title("Lucro por categoria")

#Top 5 products
products_profit = df.groupby("Product Name")["Profit"].sum().nlargest(5).sort_values(ascending=True)

rect_products = ax[2].barh(products_profit.index, products_profit, 0.4, label="Lucro")
ax[2].set_title("Top 5 produtos com maior lucro")

fig.tight_layout()

plt.show()

print(
'''
Conclusão

É possível ver que a categoria de mobília(furniture) não apresenta um lucro alto mesmo tendo 
uma grande quantidade de vendas.

A categoria de produtos que tem mais vendas é a de tecnologia(Technology) e também apresenta o 
maior lucro, além disso, os 5 produtos com maior lucro também pertencem a essa catogoria.
'''
)