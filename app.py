import streamlit as st
import google.generativeai as genai

st.title("🤖 Gemini Q&A App")

api_key = st.secrets["GEMINI_API_KEY"]

genai.configure(api_key=api_key)

question = st.text_input("Ask your question:")

if st.button("Ask Gemini"):
    if question.strip():
        try:
            model = genai.GenerativeModel("gemini-3-flash-preview")
            response = model.generate_content(question)

            st.markdown("### 📢 Answer:")
            st.markdown(response.text)

        except Exception as e:
            st.error(f"Error: {e}")
    else:
        st.warning("Please enter a question")