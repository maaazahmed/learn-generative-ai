import streamlit as st

add_selectbox = st.sidebar.selectbox("How would you like to be contacted?",
                                    ("Email", "Home phone", "Mobile phone")
                                    )


with st.sidebar:
    st.radio(
        "Choose a shipping method",
        ("Standard (5-15 days)", "Express (2-5 days)")
    )