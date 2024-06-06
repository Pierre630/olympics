import streamlit as st
import pandas as pd

st.write("Olympic MedaData")
olympic_chart_data = pd.read_csv('olympics.csv', usecols=['0', '15'])
df = pd.read_csv('olympics.csv')
ax = df.plot(kind = bar, x= '0', y = '15',legend = False)
st.pyplot(ax.get_figure())
# st.table(olympic_chart_data)
#st.bar_chart(olympic_chart_data)