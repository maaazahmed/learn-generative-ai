import streamlit as st
from types import UnionType
st.title('Counter Example using Callbacks with args')


if "count" not in st.session_state:
    st.session_state.count=0

increment_val = st.number_input("Enter Value", value=1, step=5)     


def add_value(num):
    st.session_state.count += num

increment =  st.button("Increment", on_click=add_value, args=(increment_val, ))


st.write("Count = ", st.session_state.count)    

 