import streamlit as st
import time

st.title("# Pakistan")

with st.empty():
    for sec in range(10):
        st.write(f"⏳ {sec} seconds have passed")
        time.sleep(1)
    st.write("✔️ 10 seconds over!")    
    
st.write("Pakistan zinda bad")



# import streamlit as st
# import time

# st.title("Pakistan")


# with st.empty():
#     for seconds in range(10):
#         st.write(f"⏳ {seconds} seconds have passed")
#         time.sleep(1)
#     st.write("✔️ 10 seconds over!")

# st.write("Pakistan zinda bad")