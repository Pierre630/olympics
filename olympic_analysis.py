import streamlit as st
import pandas as pd

st.write("Olympic Medal Data")
olympic_chart_data = pd.read_csv('olympics.csv', usecols=['0', '12', '13', '14', '15'])
print(olympic_chart_data)