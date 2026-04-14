import streamlit as st
import google.generativeai as genai
import google.api_core.exceptions

st.title("🤖 Gemini Q&A App")

# API key from Streamlit secrets
api_key = st.secrets["GEMINI_API_KEY"]
genai.configure(api_key=api_key)

# Model
model = genai.GenerativeModel("gemini-3-flash-preview")

# Input
question = st.text_input("Ask your question:")

# Button
if st.button("Ask Gemini"):

    if question.strip():

        prompt = question

        try:
            response = model.generate_content(prompt)

            st.markdown("### 📢 Answer:")
            st.markdown(response.text)

        except google.api_core.exceptions.ResourceExhausted:
            st.error("⚠️ Too many requests! You hit the Free Tier limit. Try again later.")

        except Exception as e:
            st.error(f"❌ Unexpected error: {e}")

    else:
        st.warning("Please enter a question")