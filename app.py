import streamlit as st
import pandas as pd
import plotly.express as px
from datetime import datetime
import google.generativeai as genai

# -----------------------------
# CONFIG
# -----------------------------
st.set_page_config(page_title="Aarambh AI+", page_icon="💛", layout="wide")

st.title("💛 Aarambh AI+ — Real Emotional AI Companion (Gemini)")
st.markdown("Powered by advanced AI for emotional support and analytics.")

# -----------------------------
# GEMINI SETUP
# -----------------------------
genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
model = genai.GenerativeModel("gemini-1.5-flash")

# -----------------------------
# SESSION STATE
# -----------------------------
if "messages" not in st.session_state:
    st.session_state.messages = []

if "moods" not in st.session_state:
    st.session_state.moods = []

if "time" not in st.session_state:
    st.session_state.time = []

# -----------------------------
# MOOD DETECTION
# -----------------------------
def detect_mood(text):
    text = text.lower()
    if "happy" in text:
        return "happy"
    elif "sad" in text:
        return "sad"
    elif "angry" in text:
        return "angry"
    elif "anxious" in text or "stress" in text:
        return "anxious"
    else:
        return "neutral"

# -----------------------------
# CHAT INPUT
# -----------------------------
st.header("💬 Chat with Aarambh AI")

user_input = st.text_input("Type your message")

if st.button("Send"):
    if user_input.strip() == "":
        st.warning("Please type something")
    else:
        st.session_state.messages.append({"role": "user", "content": user_input})

        # Build conversation context
        context = "You are a kind, empathetic emotional support AI for teenagers.\n"

        for msg in st.session_state.messages:
            if msg["role"] == "user":
                context += f"User: {msg['content']}\n"
            else:
                context += f"AI: {msg['content']}\n"

        # Generate response
        response = model.generate_content(context)
        reply = response.text

        st.session_state.messages.append({"role": "assistant", "content": reply})

        # Track mood
        st.session_state.moods.append(detect_mood(user_input))
        st.session_state.time.append(datetime.now())

# -----------------------------
# DISPLAY CHAT
# -----------------------------
for msg in st.session_state.messages:
    if msg["role"] == "user":
        st.markdown(f"**🧑 You:** {msg['content']}")
    else:
        st.markdown(f"**💛 Aarambh:** {msg['content']}")

# -----------------------------
# ANALYTICS
# -----------------------------
st.header("📊 Mood Analytics")

if st.session_state.moods:
    df = pd.DataFrame({
        "Mood": st.session_state.moods,
        "Time": st.session_state.time
    })

    st.plotly_chart(px.bar(df["Mood"].value_counts()))
else:
    st.info("Start chatting to see analytics")

# -----------------------------
# RESET
# -----------------------------
if st.button("Reset Chat"):
    st.session_state.messages = []
    st.session_state.moods = []
    st.session_state.time = []
    st.success("Chat reset!")
