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
fig, ax = plt.subplots()

#Analysis of sales by all period
sales = df.groupby(df["Order Date"].dt.to_period("M"))["Sales"].sum()

sales.index = sales.index.to_timestamp()

ax.plot(sales)
ax.set_title("Lucros ao longo do tempo")

plt.show()

'''
Conclusão

As vendas apresentaram um crescimento dentro do periodo
No período de agosto a novembro de cada ano houve um crescimento no número de vendas,
portanto os meses anteriores são o período ideal para aumentar o marketing e atrair 
mais clientes para aumentar ainda mais o faturamento. 
'''