import streamlit as st
import os
from openai import OpenAI

client = OpenAI(api_key=os.getenv("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"))


st.set_page_config(page_title="Therapist AI", page_icon="🧠")

st.title("🧠 Therapist AI")
st.write("I'm here to listen. Take your time.")

# Memory
if "messages" not in st.session_state:
    st.session_state.messages = [
        {
            "role": "system",
            "content": """
You are a kind, calm therapist.

- Be warm and understanding
- Reflect emotions
- Ask meaningful questions
- Keep responses human-like and not robotic
"""
        }
    ]

# Display chat
for msg in st.session_state.messages[1:]:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# Input
user_input = st.chat_input("How are you feeling today?")

if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})

    with st.chat_message("user"):
        st.markdown(user_input)

    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=st.session_state.messages
    )

    reply = response.choices[0].message.content
    st.session_state.messages.append({"role": "assistant", "content": reply})

    with st.chat_message("assistant"):
        st.markdown(reply)
