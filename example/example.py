import streamlit as st
import pickle
import pandas as pd
import numpy as np

dtypes = pickle.load(open("dtypes.pkl", "rb"))
example = pd.read_csv("example.csv")

categorical_columns = ["WorkClass","Education","MaritalStatus", "Occupation", "Relationship", 
"Race", "Gender", "NativeCountry"]

data = {}

for col, dtype in dtypes.iteritems():
    if col in categorical_columns:
        values = dtype.categories.values
        values2idx = dict(zip(values, range(len(values))))
        
        example_value = example[col].values[0]
        example_idx = values2idx[example_value]
        
        data[col] = st.selectbox(col, values, index=example_idx)
    else:
        example_value = example[col].values[0]
        
        data[col] = st.number_input(col, value=example_value)