import streamlit as st

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
