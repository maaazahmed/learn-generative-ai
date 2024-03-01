import streamlit as st
import random
import time
from openai import OpenAI
from modal import AiAssistant
from dotenv import dotenv_values


st.title("Echo Bot")

# st.info("API_KEY: {}".format(st.secrets["OPENAI_API_KEY"]))
OPENAI_API_KEY:str = dotenv_values(".env").get("OPENAI_API_KEY")


client = OpenAI(api_key=OPENAI_API_KEY)



ai_assistant:AiAssistant = AiAssistant()

# ai_assistant.create_assistant()



if "openai_model" not in st.session_state:
    st.session_state["openai_model"] = "gpt-3.5-turbo-1106"

if "messages" not in st.session_state:
    st.session_state.messages = []

print("assistant_id" not in st.session_state, "00000000000000000000000")
if "assistant_id" not in st.session_state:
    print("-assistant-")
    ai_asst = ai_assistant.create_assistant()
    st.session_state["assistant_id"] = ai_asst.id


st.sidebar.header("Sidebar Header")
st.sidebar.subheader("Subheader")
if "assistant_id" in st.session_state:
    # st.sidebar.text(st.session_state["assistant_id"])
    if st.button:
        st.sidebar.button(label=st.session_state["assistant_id"])



for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])
        



prompt = st.chat_input("Say something")
if prompt:
    st.session_state.messages.append({"role":"user", "content":prompt})
    
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        full_response:str = ""

        chat_response = client.chat.completions.create(
            model=st.session_state["openai_model"],
            messages=[{"role":m["role"],"content":m["content"]} for m in st.session_state["messages"]],
            stream=True
        )
        

    for response in chat_response:
        if(response.choices[0].delta.content):
            full_response += response.choices[0].delta.content

        message_placeholder.markdown(full_response)
    message_placeholder.markdown(full_response)
    st.session_state.messages.append({"role":"assistant", "content":full_response})
    






