import streamlit as st
import pandas as pd
from utils.helpers import load_responses, get_response, detect_emotion, log_mood
import nltk
nltk.download('punkt') 
st.set_page_config(page_title="Aarambh - Teen Support", layout="wide")
st.title("🌱 Aarambh - Emotional Support for Teens")
st.markdown("Share your feelings and get thoughtful guidance.")

# Load responses
responses = load_responses()

# User input
user_text = st.text_input("How are you feeling today?")

# Auto-detect or manual emotion selection
auto_detect = st.checkbox("Auto-detect emotion from text", value=True)
if auto_detect and user_text:
    emotion = detect_emotion(user_text)
    st.info(f"Detected Emotion: {emotion}")
else:
    emotion = st.selectbox("Select your emotion", list({r['emotion'] for r in responses}))

# Generate response
if st.button("Get Support"):
    if not user_text:
        st.warning("Please write something about your feelings!")
    else:
        response = get_response(emotion, responses)
        st.success(response)
        log_mood(emotion, user_text)

# Mood trend visualization
st.markdown("### Your Mood Trends")
try:
    mood_df = pd.read_csv("data/mood_log.csv", names=["date","emotion","input"])
    mood_counts = mood_df['emotion'].value_counts()
    st.bar_chart(mood_counts)
except FileNotFoundError:
    st.info("No mood data yet. Use the app to log your first entry!")
