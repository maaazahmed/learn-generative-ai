import streamlit as st

st.write("# Counter Example")


if("count" not in st.session_state):
    st.session_state.count= 0


def add_count():
    st.session_state.count+=1

st.button("Counter", on_click=add_count)

st.write("Count = ", st.session_state.count)
