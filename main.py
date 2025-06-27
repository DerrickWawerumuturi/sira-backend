import streamlit as st
from models.models import chat_with_bots

st.set_page_config(page_title="Sira", page_icon="🤖")

st.title("Sira Chatbot")

# Input text
user_input = st.text_area("Enter your message:")

# Select model
model_name = st.selectbox("Choose a model:", ["google", "facebook", "bart"])

# Submit button
if st.button("Send"):
    if user_input.strip() == "":
        st.warning("Please enter some text.")
    else:
        with st.spinner("Thinking..."):
            reply = chat_with_bots(user_input, model_name=model_name)
            st.success("Bot says:")
            st.write(reply)
