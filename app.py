import streamlit as st
import google.generativeai as genai

# এপিআই কী সেটআপ
try:
    api_key = st.secrets["GEMINI_API_KEY"]
    genai.configure(api_key=api_key)
except:
    st.error("API Key খুঁজে পাওয়া যাচ্ছে না। অনুগ্রহ করে Secrets চেক করুন।")

st.title("👨‍🏫 Master Moshai AI")
st.write("আপনার পড়াশোনা বা যেকোনো প্রশ্ন আমাকে করতে পারেন।")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("মাস্টার মশাইকে কিছু জিজ্ঞাসা করুন..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    try:
        # আমরা সবচেয়ে স্টেবল মডেলটি ব্যবহার করছি
        model = genai.GenerativeModel('gemini-pro')
        response = model.generate_content(prompt)
        
        with st.chat_message("assistant"):
            st.markdown(response.text)
        st.session_state.messages.append({"role": "assistant", "content": response.text})
    except Exception as e:
        st.error(f"মাস্টার মশাই উত্তর দিতে পারছেন না। সমস্যা: {e}")
