import streamlit as st
import google.generativeai as genai

# টাইটেল ও বর্ণনা
st.set_page_config(page_title="Master Moshai AI", page_icon="👨‍🏫")
st.title("👨‍🏫 Master Moshai AI")
st.write("আপনার পড়াশোনা বা যেকোনো প্রশ্ন আমাকে করতে পারেন।")

# এপিআই কী সেটআপ
if "GEMINI_API_KEY" not in st.secrets:
    st.error("Secrets-এ GEMINI_API_KEY পাওয়া যায়নি!")
    st.stop()

genai.configure(api_key=st.secrets["GEMINI_API_KEY"])

# আপনার কী-তে কোন মডেল কাজ করবে তা অটো খুঁজে বের করার ফাংশন
def get_working_model():
    try:
        # প্রথমে সবচেয়ে জনপ্রিয় মডেল চেষ্টা করবে
        m = genai.GenerativeModel('gemini-1.5-flash')
        m.generate_content("test")
        return 'gemini-1.5-flash'
    except:
        try:
            # না হলে পুরনো ভার্সন চেষ্টা করবে
            m = genai.GenerativeModel('gemini-pro')
            m.generate_content("test")
            return 'gemini-pro'
        except:
            return None

# সেশন স্টেট
if "messages" not in st.session_state:
    st.session_state.messages = []

# চ্যাট হিস্ট্রি দেখানো
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# ইউজার ইনপুট
if prompt := st.chat_input("মাস্টার মশাইকে কিছু জিজ্ঞাসা করুন..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    try:
        # অটো মডেল সিলেকশন ব্যবহার করছি
        model_name = get_working_model()
        if model_name:
            model = genai.GenerativeModel(model_name)
            response = model.generate_content(prompt)
            
            with st.chat_message("assistant"):
                st.markdown(response.text)
            st.session_state.messages.append({"role": "assistant", "content": response.text})
        else:
            st.error("আপনার API Key-তে কোনো মডেল কাজ করছে না। দয়া করে নতুন কী (Key) তৈরি করুন।")
    except Exception as e:
        st.error(f"মাস্টার মশাই উত্তর দিতে পারছেন না। সমস্যা: {e}")
