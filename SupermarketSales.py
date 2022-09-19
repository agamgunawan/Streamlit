import pandas as pd
import numpy as np
import streamlit  as st

st.write("""
# Supermarket Grocery Sales
Supermarket sales report analysis from 2014-2018.""")

df = pd.dataframe(r'Supermart Grocery Sales - Retail Analytics Dataset.csv')
st.dataframe(df)
