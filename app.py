import streamlit as st
import google.generativeai as genai

# এপিআই কী সেটিংস
api_key = st.secrets["GEMINI_API_KEY"]
genai.configure(api_key=api_key)

st.title("👨‍🏫 Master Moshai AI")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("মাস্টার মশাইকে প্রশ্ন করুন..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    try:
        # আমরা সরাসরি এই মডেলটি ব্যবহার করব
        model = genai.GenerativeModel('gemini-1.5-flash')
        response = model.generate_content(prompt)
        
        with st.chat_message("assistant"):
            st.markdown(response.text)
        st.session_state.messages.append({"role": "assistant", "content": response.text})
    except Exception as e:
        import streamlit as st
import google.generativeai as genai

# এপিআই কী সেটিংস
api_key = st.secrets["GEMINI_API_KEY"]
genai.configure(api_key=api_key)

st.title("👨‍🏫 Master Moshai AI")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("মাস্টার মশাইকে প্রশ্ন করুন..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    try:
        # আমরা সরাসরি এই মডেলটি ব্যবহার করব
        model = genai.GenerativeModel('gemini-1.5-flash')
        response = model.generate_content(prompt)
        
        with st.chat_message("assistant"):
            st.markdown(response.text)
        st.session_state.messages.append({"role": "assistant", "content": response.text})
    except Exception as e:
        import streamlit as st
import google.generativeai as genai

# এপিআই কী সেটিংস
api_key = st.secrets["GEMINI_API_KEY"]
genai.configure(api_key=api_key)

st.title("👨‍🏫 Master Moshai AI")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("মাস্টার মশাইকে প্রশ্ন করুন..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    try:
        # আমরা সরাসরি এই মডেলটি ব্যবহার করব
        model = genai.GenerativeModel('gemini-1.5-flash')
        response = model.generate_content(prompt)
        
        with st.chat_message("assistant"):
            st.markdown(response.text)
        st.session_state.messages.append({"role": "assistant", "content": response.text})
    except Exception as e:
        st.error(f"Error: {e}")
