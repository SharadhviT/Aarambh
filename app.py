import streamlit as st
import pandas as pd
import random
import plotly.express as px
from datetime import datetime

# -----------------------------
# CONFIG
# -----------------------------
st.set_page_config(page_title="Aarambh AI+", page_icon="💛", layout="wide")

st.title("💛 Aarambh AI+ — Intelligent Emotional Support")
st.markdown("Talk to your AI companion. You're not alone.")

# -----------------------------
# SESSION STATE
# -----------------------------
if "chat" not in st.session_state:
    st.session_state.chat = []

if "moods" not in st.session_state:
    st.session_state.moods = []

if "scores" not in st.session_state:
    st.session_state.scores = []

if "time" not in st.session_state:
    st.session_state.time = []

# -----------------------------
# EMOTION ANALYSIS
# -----------------------------
def analyze_emotion(text):
    text = text.lower()
    intensity = random.randint(40, 95)

    if any(w in text for w in ["happy", "great", "excited"]):
        return "happy", intensity
    elif any(w in text for w in ["sad", "cry", "down"]):
        return "sad", intensity
    elif any(w in text for w in ["angry", "mad", "frustrated"]):
        return "angry", intensity
    elif any(w in text for w in ["anxious", "stress", "worried"]):
        return "anxious", intensity
    else:
        return "neutral", intensity

# -----------------------------
# SMART RESPONSE ENGINE
# -----------------------------
def generate_response(user_input, mood, score):
    
    if mood == "sad":
        return f"I’m really sorry you're feeling this way 💛 (Intensity: {score})\nWant to talk more about what’s bothering you?"

    elif mood == "happy":
        return f"That’s amazing 😊 (Intensity: {score})\nWhat made you feel this way?"

    elif mood == "angry":
        return f"That sounds frustrating 😡 (Intensity: {score})\nLet’s slow down and unpack it."

    elif mood == "anxious":
        return f"I hear you 😰 (Intensity: {score})\nTry taking a deep breath. You're okay."

    else:
        return f"I’m here for you 💛 (Intensity: {score})\nTell me more."

# -----------------------------
# CHAT INPUT
# -----------------------------
st.header("💬 Chat")

user_input = st.text_input("Type your message")

if st.button("Send"):
    if user_input.strip() == "":
        st.warning("Please type something")
    else:
        mood, score = analyze_emotion(user_input)
        reply = generate_response(user_input, mood, score)

        st.session_state.chat.append(("You", user_input))
        st.session_state.chat.append(("Aarambh", reply))

        st.session_state.moods.append(mood)
        st.session_state.scores.append(score)
        st.session_state.time.append(datetime.now())

# -----------------------------
# DISPLAY CHAT
# -----------------------------
for sender, msg in st.session_state.chat:
    if sender == "You":
        st.markdown(f"**🧑 You:** {msg}")
    else:
        st.markdown(f"**💛 Aarambh:** {msg}")

# -----------------------------
# ANALYTICS
# -----------------------------
st.header("📊 Emotional Analytics")

if st.session_state.moods:
    df = pd.DataFrame({
        "Mood": st.session_state.moods,
        "Time": st.session_state.time,
        "Score": st.session_state.scores
    })

    st.subheader("Mood Frequency")
    st.plotly_chart(px.bar(df["Mood"].value_counts()))

    st.subheader("Emotion Intensity Over Time")
    st.plotly_chart(px.line(df, x="Time", y="Score"))

    dominant = df["Mood"].value_counts().idxmax()
    st.success(f"Dominant Emotion: {dominant.upper()}")

else:
    st.info("Start chatting to see analytics")

# -----------------------------
# SELF CARE
# -----------------------------
st.header("✨ Smart Self-Care")

if st.session_state.moods:
    last_mood = st.session_state.moods[-1]

    tips = {
        "sad": ["Talk to a friend 💛", "Write your thoughts ✍️"],
        "happy": ["Keep doing what you love 😊", "Share your joy!"],
        "angry": ["Take deep breaths 🌿", "Go for a walk 🚶"],
        "anxious": ["Try meditation 🧘", "Slow breathing 🌬️"],
        "neutral": ["Try something new 🌟", "Listen to music 🎧"]
    }

    st.success(random.choice(tips[last_mood]))

# -----------------------------
# CLEAR BUTTON
# -----------------------------
if st.button("Clear Chat"):
    st.session_state.chat = []
    st.session_state.moods = []
    st.session_state.scores = []
    st.session_state.time = []
    st.success("Reset complete!")
