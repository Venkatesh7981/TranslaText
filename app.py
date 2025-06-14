import streamlit as st
from googletrans import Translator, LANGUAGES

# Translator instance
translator = Translator()

# Language list
language_names = list(LANGUAGES.values())



# Streamlit UI
st.set_page_config(page_title="TranslaText", page_icon="🌐")
st.title("🌍 TranslaText - Language Translator")

text = st.text_area("Enter text to translate", height=150)

col1, col2 = st.columns(2)
with col1:
    src_lang = st.selectbox("Translate from", language_names, index=language_names.index("english"))
with col2:
    dest_lang = st.selectbox("Translate to", language_names, index=language_names.index("spanish"))

if st.button("Translate"):
    try:
        src_key = next(k for k, v in LANGUAGES.items() if v == src_lang.lower())
        dest_key = next(k for k, v in LANGUAGES.items() if v == dest_lang.lower())
        translated = translator.translate(text, src=src_key, dest=dest_key)
        st.success(translated.text)
    except Exception as e:
        st.error(f"Translation failed: {e}")
