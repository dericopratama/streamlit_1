import streamlit as st
import pandas as pd
import time
import altair as alt

st.write("""
# Altair Chart
""")

with st.empty():
  while True:
    df = pd.read_csv("realtime.csv")
    c = alt.Chart(df).mark_trail().encode(
      x='hoursminutesseconds(Timestamp):T',
      y='Value:Q',
      size = 'Value:Q',
      tooltip=[alt.Tooltip('yearmonthdatehoursminutesseconds(Timestamp)', title='Timestamp'),
                           'Value']).interactive()
    st.altair_chart(c, use_container_width=True)
    time.sleep(5)