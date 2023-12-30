
import streamlit as st
 
# xp =  st.expander("See explanation")

# xp.write("The chart above shows some numbers I picked for you. I rolled actual dice for these, so they're guaranteed to be random.")
# xp.image("https://static.streamlit.io/examples/dice.jpg")


with st.expander("See explanation"):
    st.write("The chart above shows some numbers I picked for you. I rolled actual dice for these, so they're guaranteed to be random.")
    st.image("https://static.streamlit.io/examples/dice.jpg")