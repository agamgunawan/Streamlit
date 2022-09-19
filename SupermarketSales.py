import pandas as pd
import numpy as np
import streamlit  as st

st.write("""
# Supermarket Grocery Sales
Supermarket sales report analysis from 2014-2018.""")

df = pd.DataFrame(
   np.random.randn(50, 20),
   columns=('col %d' % i for i in range(20)))

st.dataframe(df)  # Same as st.write(df)
