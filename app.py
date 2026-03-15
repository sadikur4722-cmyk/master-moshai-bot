import streamlit as st
import google.generativeai as genai

# টাইটেল (একবারই থাকবে)
st.title("👨‍🏫 Master Moshai AI")

# Secrets থেকে API Key নেওয়া
if "GEMINI_API_KEY" in st.secrets:
    api_key = st.secrets["GEMINI_API_KEY"]
    genai.configure(api_key=api_key)
    
    # চ্যাট ইনপুট (এটি কোডে একবারই থাকতে হবে)
    if prompt := st.chat_input("মাস্টার মশাইকে প্রশ্ন করুন..."):
        st.chat_message("user").write(prompt)
        
        try:
            model = genai.GenerativeModel('gemini-1.5-flash-latest')
            response = model.generate_content(prompt)
            st.chat_message("assistant").write(response.text)
        except Exception as e:
            st.error(f"গুগল সার্ভার এরর: {e}")
else:
    st.warning("দয়া করে Secrets-এ API Key যোগ করুন।")
