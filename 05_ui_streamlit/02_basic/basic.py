import streamlit as st

st.success("this is success")
st.info("this is info")
st.warning("this is warning")

st.error("this is error")

# Exception - This has been added later
exp = ZeroDivisionError("Trying to divide by Zero")
st.exception(exp)


st.write(range(0,10))



from PIL import Image


if st.checkbox("Show/Hide"):
    st.text("Showing the widget")



status = st.radio("Select Gander", ["Male", "Female"])

st.text(status)

hobby =  st.selectbox("Hobbies", ["Developemnt 1", "Developemnt 2", "Developemnt 3"])

st.write("Selected Time: ", hobby, "as a Hobbies")


st.button("click me for no response")


hobbies =  st.multiselect("Select", ['Dancing', 'Reading', 'Sports'])

st.write("You Selected", hobbies, "Hobbies")

st.code("""
let x = myFunction(4, 3);

function myFunction(a, b) {
// Function returns the product of a and b
  return a * b;
}

""")


if st.button("About"):
    st.write("Welcome To World of Generative AI!!!")





name = st.text_input("Enter Your name", "type here....")

if st.button("Submit"):
    res =  name.title()
    st.success(res)



level =  st.slider("select Level", 1,10)
st.text('Selected: {}'.format(level))    

    