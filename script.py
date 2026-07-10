import pandas as pd

df = pd.read_csv("Sample-Superstore.csv", encoding="latin1")

#analysing
# print(df.head())
# print(df.info())
# print(df.describe())
# print(df.dtypes)

#cleaning data
df.dropna(inplace=True)
df["Order Date"] = pd.to_datetime(df["Order Date"])
df["Ship Date"] = pd.to_datetime(df["Ship Date"])
df.drop_duplicates(inplace=True)

#basic informations
# print(clear_df["Order Date"].min())
# print(clear_df["Order Date"].max())
# print("Quantidade de clientes: %s" %(df["Customer ID"].nunique()))
# print("Quantidade de seguimentos: %s" %(df["Segment"].nunique()))
# print("Quantidade de países: %s" %(df["Country"].nunique()))
# print("Quantidade de estados: %s" %(df["State"].nunique()))
# print("Quantidade de cidades: %s" %(df["City"].nunique()))
# print("Quantidade de categorias: %s" %(df["Category"].nunique()))
# print("Quantidade de produtos: %s" %(df["Product Name"].nunique()))

#Total Profit
# print("Lucro total: US$ %s\n" %(df["Profit"].sum()))

#Total Sales
print("Total de vendas: US$ %s\n" %(df["Sales"].sum()))

#Profit by segment
# print("Lucro por %s\n" %(df.groupby("Segment")["Profit"].sum()))

#profit by Category
# print("Lucro por %s\n" %(df.groupby("Category")["Profit"].sum()))

#profit by Region
# print("Lucro por %s\n" %(df.groupby("Region")["Profit"].sum()))

#profit by State
# print("Lucro por %s\n" %(df.groupby("State")["Profit"].sum().nlargest(5)))

#Sales by segment
# print("Total em vendas (US$) por %s\n" %(df.groupby("Segment")["Sales"].sum()))

#Sales by Category
# print("Total em vendas (US$) por %s\n" %(df.groupby("Category")["Sales"].sum()))

#Sales by Region
# print("Total em vendas (US$) por %s\n" %(df.groupby("Region")["Sales"].sum()))

#Sales by State
# print("Total em vendas (US$) por %s\n" %(df.groupby("State")["Sales"].sum().nlargest(5)))

#Top 5 buying costumers (Name/Sales-US$)
# print("Top 5 clientes que mais compraram: %s\n" %(df.groupby("Customer Name")["Sales"].sum().nlargest(5)))

#Top 5 buying cities (Name/Sales-US$)
# print("Top 5 cidades que mais compraram: %s\n" %(df.groupby("City")["Sales"].sum().nlargest(5)))

#Top 5 best selling products in quantity(Name/Sales-US$)
# print("Top 5 produtos mais vendidos: %s\n" %(df.groupby("Product Name")["Quantity"].sum().nlargest(5)))

#Top 5 best selling products (Name/Sales-US$)
# print("Top 5 produtos mais vendidos: %s\n" %(df.groupby("Product Name")["Profit"].sum().nlargest(5)))