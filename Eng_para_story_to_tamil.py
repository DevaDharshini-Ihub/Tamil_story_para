import streamlit as st
from googletrans import Translator
from gtts import gTTS
import os

translator = Translator()
def translate_text_to_tamil(text):
    """
    Translate English text to Tamil.
    """
    translation = translator.translate(text, src='en', dest='ta')
    return translation.text
def text_to_speech(text, filename="story.mp3"):
    """
    Convert text to speech and save it to an audio file.
    """
    tts = gTTS(text, lang='ta')
    tts.save(filename)

st.title("Story Translation and Narration")
english_story = st.text_area("Please enter your story in English (500-1000 words):", height=200)
if st.button("Translate and Narrate"):
    if english_story:
       
        tamil_story = translate_text_to_tamil(english_story)
        st.subheader("Translated Story in Tamil:")
        st.write(tamil_story)
        text_to_speech(tamil_story)
        st.audio("story.mp3")
    else:
        st.error("Please enter a story before clicking the button.")
