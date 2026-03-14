import streamlit as st
import google.generativeai as genai

# এপিআই কী সেটআপ
try:
    api_key = st.secrets["GEMINI_API_KEY"]
    genai.configure(api_key=api_key)
except:
    st.error("Secrets-এ API Key পাওয়া যায়নি!")

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
        # এখানে আমরা নির্দিষ্ট ভার্সন উল্লেখ করে দিচ্ছি যাতে 404 Error না আসে
        model = genai.GenerativeModel(model_name="gemini-1.5-flash")
        response = model.generate_content(prompt)
        
        with st.chat_message("assistant"):
            st.markdown(response.text)
        st.session_state.messages.append({"role": "assistant", "content": response.text})
    except Exception as e:
        # যদি flash কাজ না করে তবে pro ভার্সন ট্রাই করবে
        try:
            model = genai.GenerativeModel('gemini-1.5-flash-8b')
            response = model.generate_content(prompt)
            with st.chat_message("assistant"):
                st.markdown(response.text)
            st.session_state.messages.append({"role": "assistant", "content": response.text})
        except Exception as e2:
            st.error(f"মাস্টার মশাই কানেক্ট হতে পারছেন না। সমস্যা: {e2}")
