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

#Ship mode analysis
shipping_modes = df.groupby("Ship Mode").size()
colors = plt.get_cmap("Blues")(np.linspace(0.2, 0.7, len(shipping_modes.index)))

ax.pie(shipping_modes, colors=colors, labels=shipping_modes.index, autopct="%1.f%%")
ax.set_title("Formas de envio")

plt.show()

'''
Conclusão

A forma de envio padrão é a mais escolhida.

Provavelmente, a maioria dos consumidores não acham vantajoso o custo adicional
em relação as vantagens oferecidas pelos outros métodos. 
'''