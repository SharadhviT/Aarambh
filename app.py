# app.py

import streamlit as st
from utils.helpers import load_responses, get_response

# Load responses from CSV
responses = load_responses("responses.csv")

# Streamlit UI
st.set_page_config(page_title="Aarambh - Emotional Support", layout="centered")
st.title("💛 Aarambh - Teen Emotional Support")
st.markdown("Talk to me about how you feel. I can understand 20+ emotions!")

# User input
user_input = st.text_input("How are you feeling today?")

# Display response
if user_input:
    response = get_response(user_input, responses)
    st.markdown(f"**Aarambh:** {response}")
