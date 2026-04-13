import streamlit as st
from google import genai
import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key=api_key)

st.title("🤖 Gemini Q&A App")

question = st.text_input("Ask your question:")

if st.button("Ask Gemini"):
    if question:
        try:
            response = client.models.generate_content(
                model="gemini-3-flash-preview",
                contents=question
            )

            st.markdown("### 📢 Answer:")
            st.markdown(response.text)

        except Exception as e:
            st.error(f"Error: {e}")
    else:
        st.warning("Please enter a question")