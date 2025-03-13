import streamlit as st
from deep_translator import GoogleTranslator

# Translator Class
class Translator:
    def translate(self, text, target_lang):
        return GoogleTranslator(source='en', target=target_lang).translate(text)

# Initialize Translator
translator = Translator()

# Page Configuration
st.set_page_config(page_title="PreetAI Translate", layout="centered")

# Page Title
st.title("PreetAI Translate 🌍")

# Input Box for English Text
english_text = st.text_area("Enter text in English:", height=150)

# Language Selection
languages = {
    "Hindi": "hi",
    "Gujarati": "gu",
    "Marathi": "mr",
    "Punjabi": "pa",
    "Bengali": "bn",
    "Tamil": "ta",
    "Telugu": "te",
    "Kannada": "kn",
    "Malayalam": "ml",
    "Urdu": "ur"
}

selected_language = st.selectbox("Select Target Language:", list(languages.keys()))

# Translate Button
if st.button("Translate"):
    if english_text.strip():
        with st.spinner("Translating..."):
            target_lang_code = languages[selected_language]
            translation = translator.translate(english_text, target_lang_code)
        st.subheader(f"Translation in {selected_language}:")
        st.text_area("Translation:", translation, height=150)
    else:
        st.warning("Please enter some text to translate.")