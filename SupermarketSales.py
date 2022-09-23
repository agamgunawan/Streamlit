#library
import pandas as pd
import numpy as np
import streamlit  as st
#import plotly.express as px  # pip install plotly-express

#judul
st.title("""
# Penjualan Grosir Supermarket
""")

#markdown
st.markdown("""
Laporan Analisi Penjualan Supermarket dari tahun 2014-2018.
* **Librari pythin yang digunakan :** numpy, pandas, streamlit
* **Data source:** [Kaggle.com](https://www.kaggle.com/datasets/mohamedharris/supermart-grocery-sales-retail-analytics-dataset).
""")


#load dataset
df = pd.read_csv("Supermart Grocery Sales - Retail Analytics Dataset.csv")

#buat kolom tahun pada dataset
df['Order Date'] = pd.to_datetime(df['Order Date'])
df['Year'] = df['Order Date'].dt.year

#panggil dataset
st.write(df)



#buat sidebar
st.sidebar.header("Masukkan Filter:")

#filter tahun
Year = st.sidebar.multiselect(
    "Masukkan Tahun:",
    options=df["Year"].unique(),
    default=df["Year"].unique(),
)

#filter region
Region = st.sidebar.multiselect(
    "Masukkan Region:",
    options=df["Region"].unique(),
    default=df["Region"].unique(),
)

#filter kategori
Category = st.sidebar.multiselect(
    "Masukkan Kategori:",
    options=df["Category"].unique(),
    default=df["Category"].unique()
)

df_selection = df.query(
    "Year == @Year & Region == @Region Category == @Category"
)

#mainpage
st.write("# Sales Dashboard")
st.markdown("##")

total_sales = int(df_selection["Sales"].sum())
total_Profit = int(df_selection["Profit"].sum())
average_profit_by_sales = round(df_selection["Profit"].mean(), 2)


# SALES BY Category [BAR CHART]
sales_by_category = (
    df_selection.groupby(by=["Category"]).sum()[["Sales"]].sort_values(by="Sales")
)
fig_product_sales = px.bar(
    sales_by_category,
    x="Sales",
    y=sales_by_category.index,
    orientation="h",
    title="<b>Sales by Category</b>",
    color_discrete_sequence=["#0083B8"] * len(sales_by_category),
    template="plotly_white",
)
fig_product_sales.update_layout(
    plot_bgcolor="rgba(0,0,0,0)",
    xaxis=(dict(showgrid=False))
)


st.plotly_chart(fig_product_sales, use_container_width=True)
