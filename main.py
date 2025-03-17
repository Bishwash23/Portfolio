import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images\profile.jpg")

with col2:
    st.title("Bishwash Bhattarai")
    content = """Hi, I'm Bishwash, a Python developer passionate about building efficient and scalable solutions. 
             I specialize in backend development. 
             I enjoy solving problems through clean and optimized code."""
    
    st.info(content)

content2 = """
Below you can find some of the apps I have built in Python.
"""

st.write(content2)

col3, col4 = st.columns(2)

df = pd.read_csv("data.csv", sep=";")
with col3:
    for index, row in df[:10].iterrows():
        st.header(row["title"])

with col4:
    for index, row in df[10:].iterrows():
        st.header(row["title"])
