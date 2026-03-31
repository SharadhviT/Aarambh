import streamlit as st
import pandas as pd
import random
import plotly.express as px
from datetime import datetime

# -----------------------------
# PAGE CONFIG
# -----------------------------
st.set_page_config(page_title="Aarambh AI", page_icon="💛", layout="wide")

st.title("💛 Aarambh AI — Emotional Support Chatbot")
st.write("Talk freely. I'm here for you.")

# -----------------------------
# SESSION STATE
# -----------------------------
if "chat" not in st.session_state:
    st.session_state.chat = []

if "moods" not in st.session_state:
    st.session_state.moods = []

if "time" not in st.session_state:
    st.session_state.time = []

# -----------------------------
# MOOD DETECTION
# -----------------------------
def detect_mood(text):
    text = text.lower()
    if any(w in text for w in ["happy", "good", "great", "excited"]):
        return "happy"
    elif any(w in text for w in ["sad", "down", "depressed", "cry"]):
        return "sad"
    elif any(w in text for w in ["angry", "mad", "frustrated"]):
        return "angry"
    elif any(w in text for w in ["anxious", "stress", "nervous", "worried"]):
        return "anxious"
    else:
        return "neutral"

# -----------------------------
# AI RESPONSE ENGINE
# -----------------------------
def chatbot_response(user_input, mood):

    responses = {
        "happy": [
            "That’s amazing to hear 😊 What made your day good?",
            "I love that energy! Tell me more 💛",
            "Happiness looks great on you!"
        ],
        "sad": [
            "I’m really sorry you’re feeling this way 💛 Want to talk about it?",
            "It’s okay to feel sad sometimes. I’m here for you.",
            "You don’t have to go through this alone."
        ],
        "angry": [
            "That sounds frustrating 😡 What happened?",
            "Take a deep breath. Let’s talk it out.",
            "I hear you. Anger can be overwhelming."
        ],
        "anxious": [
            "That sounds stressful 😰 Let’s slow things down together.",
            "Try taking a deep breath with me.",
            "You’re safe. We can figure this out."
        ],
        "neutral": [
            "I’m here to listen 💛 Tell me more.",
            "How has your day been so far?",
            "Anything on your mind?"
        ]
    }

    return random.choice(responses[mood])

# -----------------------------
# CHAT UI
# -----------------------------
st.header("💬 Chat with Aarambh AI")

user_input = st.text_input("Type your message:")

if st.button("Send"):
    if user_input.strip() == "":
        st.warning("Please type something")
    else:
        mood = detect_mood(user_input)
        reply = chatbot_response(user_input, mood)

        # Save chat
        st.session_state.chat.append(("You", user_input))
        st.session_state.chat.append(("Aarambh", reply))

        # Save mood
        st.session_state.moods.append(mood)
        st.session_state.time.append(datetime.now())

# -----------------------------
# DISPLAY CHAT
# -----------------------------
for sender, message in st.session_state.chat:
    if sender == "You":
        st.markdown(f"**🧑 You:** {message}")
    else:
        st.markdown(f"**💛 Aarambh:** {message}")

# -----------------------------
# MOOD TRACKER
# -----------------------------
st.header("📊 Mood Tracker")

if st.session_state.moods:
    df = pd.DataFrame({
        "mood": st.session_state.moods,
        "time": st.session_state.time
    })

    fig = px.bar(df["mood"].value_counts(), title="Mood Frequency")
    st.plotly_chart(fig)

else:
    st.info("No mood data yet.")

# -----------------------------
# SELF CARE SUGGESTIONS
# -----------------------------
st.header("✨ Self-Care Suggestion")

tips = [
    "Take a deep breath 🌿",
    "Drink some water 💧",
    "Talk to a friend 📞",
    "Go for a short walk 🚶",
    "Listen to music 🎧",
    "Write your thoughts ✍️"
]

st.success(random.choice(tips))

# -----------------------------
# CLEAR CHAT
# -----------------------------
if st.button("Clear Chat"):
    st.session_state.chat = []
    st.session_state.moods = []
    st.session_state.time = []
    st.success("Chat cleared!")
