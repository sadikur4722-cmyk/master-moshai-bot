import streamlit as st
import google.generativeai as genai

# API key load
genai.configure(api_key=st.secrets["GEMINI_API_KEY"])

# Model
model = genai.GenerativeModel("gemini-1.5-flash")

st.title("👨‍🏫 Master Moshai AI")

# Chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Show old messages
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# User input
prompt = st.chat_input("মাস্টার মশাইকে প্রশ্ন করুন...")

if prompt:
    st.session_state.messages.append({"role": "user", "content": prompt})

    with st.chat_message("user"):
        st.markdown(prompt)

    response = model.generate_content(prompt)

    with st.chat_message("assistant"):
        st.markdown(response.text)

    st.session_state.messages.append(
        {"role": "assistant", "content": response.text}
    )
