import streamlit as st
import google.generativeai as genai
import pandas as pd
import os
from datetime import datetime

# ===============================
# 🔐 GEMINI API SETUP
# ===============================
genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
model = genai.GenerativeModel("gemini-pro")

# ===============================
# 🎨 PAGE CONFIG
# ===============================
st.set_page_config(page_title="Aarambh AI", page_icon="🧠")

st.title("🧠 Aarambh: AI Mental Health Intelligence System")
st.caption("A safe space to talk, reflect, and understand your emotions.")

# ===============================
# 🧠 INITIAL MEMORY
# ===============================
if "messages" not in st.session_state:
    st.session_state.messages = []

# ===============================
# 🧠 THERAPIST PROMPT
# ===============================
SYSTEM_PROMPT = """
You are a calm, kind, and empathetic therapist.

- Speak naturally like a human
- Reflect emotions before responding
- Ask thoughtful questions
- Be warm and non-judgmental
- Keep responses concise
"""

# ===============================
# 🧠 EMOTION DETECTION
# ===============================
def detect_mood(text):
    text = text.lower()

    if any(word in text for word in ["sad", "tired", "exhausted", "low", "depressed"]):
        return "Low"
    elif any(word in text for word in ["anxious", "nervous", "scared", "stress", "worried"]):
        return "Anxiety"
    elif any(word in text for word in ["happy", "good", "excited", "calm", "great"]):
        return "Positive"
    else:
        return "Neutral"

# ===============================
# 💾 SAVE DATA
# ===============================
def save_data(mood, text):
    data = {
        "time": datetime.now(),
        "mood": mood,
        "text": text
    }

    df = pd.DataFrame([data])

    if not os.path.exists("mood_log.csv"):
        df.to_csv("mood_log.csv", index=False)
    else:
        df.to_csv("mood_log.csv", mode="a", header=False, index=False)

# ===============================
# 💬 DISPLAY CHAT
# ===============================
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# ===============================
# 🧠 USER INPUT
# ===============================
user_input = st.chat_input("How are you feeling today?")

if user_input:
    mood = detect_mood(user_input)
    save_data(mood, user_input)

    # Save user message
    st.session_state.messages.append({
        "role": "user",
        "content": user_input
    })

    with st.chat_message("user"):
        st.markdown(user_input)

    # ===============================
    # 🤖 GEMINI RESPONSE
    # ===============================
    try:
        # Build conversation context
        conversation_text = SYSTEM_PROMPT + "\n\n"

        for msg in st.session_state.messages:
            if msg["role"] == "user":
                conversation_text += f"User: {msg['content']}\n"
            else:
                conversation_text += f"Therapist: {msg['content']}\n"

        response = model.generate_content(conversation_text)

        reply = response.text

    except Exception as e:
        st.error("⚠️ Error communicating with AI.")
        st.text(str(e))
        reply = "I'm having trouble responding right now. Please try again."

    # Save AI reply
    st.session_state.messages.append({
        "role": "assistant",
        "content": reply
    })

    with st.chat_message("assistant"):
        st.markdown(reply)

# ===============================
# 📊 ANALYTICS DASHBOARD
# ===============================
st.divider()
st.subheader("📊 Emotional Insights")

if os.path.exists("mood_log.csv"):
    df = pd.read_csv("mood_log.csv")

    st.write("### Mood Distribution")
    st.bar_chart(df["mood"].value_counts())

    # Pattern detection
    recent = df.tail(5)

    if len(recent) >= 5:
        most_common = recent["mood"].mode()[0]

        if most_common == "Anxiety":
            st.warning("⚠️ You've been feeling anxious frequently. Try slowing down and taking breaks.")
        elif most_common == "Low":
            st.warning("⚠️ You've been feeling low lately. Consider reaching out to someone you trust.")
        elif most_common == "Positive":
            st.success("🌟 You've been feeling positive! Keep it up!")
else:
    st.info("Start chatting to generate emotional insights.")
