import streamlit as st
import numpy as np

# message =  st.chat_message("assistant")
# message.write("Hello Human")

# message.bar_chart(np.random.randn(30, 3))


# message_1 =  st.chat_message("use")
# message_1.write("Thank you")



usr =  st.chat_message("user")
sys = st.chat_message("assistant")

usr.write("Hello AI, How are you today")
sys.write("I am fine what about you!")

sys.write("Sure I am here for you")

usr.write("I want to learn about you, can you teach me  ")

