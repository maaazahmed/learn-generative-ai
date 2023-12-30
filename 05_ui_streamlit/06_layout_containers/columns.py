import streamlit as st


col1, col2, col3 = st.columns(3)


# col1.header("Hellow World")

with col1:
    st.header("A Cate")
    st.image("https://static.streamlit.io/examples/cat.jpg")

with col2:
    st.header("A Dog")
    st.image("https://static.streamlit.io/examples/dog.jpg")    

with col3:
    st.header("An owl")    
    st.image("https://static.streamlit.io/examples/owl.jpg")

