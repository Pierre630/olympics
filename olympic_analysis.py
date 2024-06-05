import streamlit as st
import pandas as pd

olympic_chart_data = pd.read_csv('olypics.csv', usecols=['0', '12', '13', '14', '15'])
print(olympic_chart_data)