import streamlit as st

st.write("# Counter Example")


if('count' not in st.session_state):
    st.session_state.count = 0

increment =  st.button("increment")

if(increment):
    st.session_state.count +=1

st.code("Count = {}".format(st.session_state.count))    