import streamlit as st

st.write("# Counter Example")

count:int = 0

increment = st.button("Increment")

if(increment):
    count+=1

st.code(" Count = {}".format(count))    