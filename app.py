import streamlit as st
from config.Engine import model
from config.Memory import Memory

# Configure page settings
st.set_page_config(page_title="RME.AI", page_icon="🤖", layout="centered")

st.title("Rme ai")
st.write("Aisis nki? Kmn acis be?")

memory = Memory()


if st.sidebar.button("Clear History"):
    with open(memory.file_path, "w") as f:
        f.write("")
    st.sidebar.success("History cleared successfully!!")


history = memory.get_history()

for msg in history:
    st.chat_message(msg["role"]).write(msg["message"])

user_input = st.chat_input("Kicu bolbi?")

if user_input:

    st.chat_message("user").write(user_input)
    memory.add("user", user_input)

    with st.spinner("Thinking..."):

        prompt = model.build_prompt(user_input)

        response = model.get_model_response(prompt)
        st.chat_message("assistant").write(response)
        memory.add("assistant", response)
