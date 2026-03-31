# app.py
import streamlit as st
import json
from textblob import TextBlob
from datetime import datetime

# -------------------------------
# Page Configuration
# -------------------------------
st.set_page_config(page_title="Aarambh - Emotional Support", layout="centered")
st.title("🌸 Aarambh: Your Emotional Support App")
st.markdown("Talk to me about how you're feeling today!")

# -------------------------------
# Load Responses
# -------------------------------
@st.cache_data
def load_responses():
    with open("responses.json", "r", encoding="utf-8") as file:
        return json.load(file)

responses = load_responses()

# -------------------------------
# Detect Emotion
# -------------------------------
def detect_emotion(user_input):
    user_input_lower = user_input.lower()
    
    # 1. Keyword matching
    for emotion in responses.keys():
        if emotion in user_input_lower:
            return emotion
    
    # 2. Sentiment analysis fallback
    polarity = TextBlob(user_input).sentiment.polarity
    if polarity > 0.2:
        return "happy"
    elif polarity < -0.2:
        return "sad"
    else:
        return "neutral"

# -------------------------------
# Get Response
# -------------------------------
def get_response(user_input):
    emotion = detect_emotion(user_input)
    response = responses.get(emotion, "I'm here to listen. Can you tell me more?")
    return response

# -------------------------------
# Log Mood (Optional)
# -------------------------------
def log_mood(user_input, response):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("mood_log.txt", "a", encoding="utf-8") as f:
        f.write(f"{timestamp} | User: {user_input} | Bot: {response}\n")

# -------------------------------
# Streamlit Chat Interface
# -------------------------------
user_input = st.text_input("You:", "")

if user_input:
    response = get_response(user_input)
    st.text_area("Aarambh:", value=response, height=100, max_chars=None)
    
    # Log mood
    log_mood(user_input, response)
