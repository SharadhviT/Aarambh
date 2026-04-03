import streamlit as st
from openai import OpenAI
import os
import pandas as pd
from datetime import datetime

# ===============================
# 🔐 API SETUP (SECURE)
# ===============================
api_key = os.getenv("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")
st.write("DEBUG → API KEY:", api_key)
client = OpenAI(api_key=api_key)

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
    st.session_state.messages = [
        {
            "role": "system",
            "content": "You are a calm, kind, and empathetic therapist. Speak naturally, reflect emotions, and ask thoughtful questions."
        }
    ]

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
    if msg["role"] != "system":
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])

# ===============================
# 🧠 USER INPUT
# ===============================
user_input = st.chat_input("How are you feeling today?")

if user_input:
    # Detect mood + save
    mood = detect_mood(user_input)
    save_data(mood, user_input)

    # Store user message
    st.session_state.messages.append({
        "role": "user",
        "content": user_input
    })

    with st.chat_message("user"):
        st.markdown(user_input)

    # ===============================
    # 🧠 SAFE MESSAGE FORMAT (FIX)
    # ===============================
    safe_messages = [
        {"role": m["role"], "content": str(m["content"])}
        for m in st.session_state.messages
    ]

    # ===============================
    # 🤖 AI RESPONSE (SAFE CALL)
    # ===============================
    try:
        response = client.chat.completions.create(
            model="gpt-4.1-mini",
            messages=safe_messages
        )

        reply = response.choices[0].message.content

    except Exception as e:
        st.error("⚠️ Error communicating with AI.")
        st.text(str(e))
        reply = "I'm having trouble responding right now. Please try again."

    # Store AI reply
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
