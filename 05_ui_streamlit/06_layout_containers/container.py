import streamlit as st

import numpy as np


with st.container():
    st.write("this is inside the container")

    st.bar_chart(np.random.rand(50,3))

st.write("This is outside the container")    