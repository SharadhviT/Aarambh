# app.py
import streamlit as st
import random
from textblob import TextBlob

st.set_page_config(page_title="Aarambh: Teen Emotional Support", layout="wide")
st.title("💬 Aarambh: Advanced Emotional Support for Teenagers")
st.markdown("Type how you're feeling and get guidance to handle your emotions!")

# -----------------------------
# Generate 1000+ emotion list
# -----------------------------
base_emotions = [
    "happy", "sad", "angry", "fearful", "anxious", "excited", "bored", "lonely",
    "jealous", "confident", "nervous", "guilty", "ashamed", "proud", "relieved",
    "embarrassed", "hopeful", "disappointed", "frustrated", "overwhelmed",
    "curious", "stressed", "grateful", "insecure", "optimistic", "pessimistic",
    "confused", "tired", "energetic", "motivated", "resentful", "disgusted",
    "peaceful", "apathetic", "jealous", "shy", "regretful", "lonely", "trusting"
]

intensities = ["slightly", "moderately", "very", "extremely", "super", "barely"]
contexts = ["about school", "about friends", "about family", "on social media",
            "about exams", "about future", "about relationships", "about self-image"]

emotions_list = []
while len(emotions_list) < 1000:
    base = random.choice(base_emotions)
    intensity = random.choice(intensities)
    context = random.choice(contexts)
    emotion = f"{intensity} {base} {context}"
    if emotion not in emotions_list:
        emotions_list.append(emotion)

# -----------------------------
# Responses and coping techniques
# -----------------------------
coping_techniques = [
    "Try deep breathing exercises for 5 minutes.",
    "Write down your thoughts in a journal.",
    "Take a short walk or do light exercise.",
    "Listen to calming music.",
    "Talk to a trusted friend or family member.",
    "Practice mindfulness or meditation.",
    "Draw or paint how you feel.",
    "Do a small act of kindness for someone else.",
    "Break down your problem into smaller steps.",
    "Focus on one positive thing about yourself today."
]

def get_emotion_response(user_input):
    blob = TextBlob(user_input)
    words = blob.words.lower()
    # Check if any emotion keyword appears in input
    matched_emotions = [e for e in emotions_list if any(word in e for word in words)]
    if not matched_emotions:
        # fallback if nothing matches
        return "Hmm, I couldn't detect a clear emotion. Can you describe it differently?"
    
    # Randomly pick one matched emotion
    chosen_emotion = random.choice(matched_emotions)
    
    # Generate response with coping technique
    technique = random.choice(coping_techniques)
    response = f"You seem to be feeling **{chosen_emotion}**.\n\nHere's something that might help: {technique}"
    return response

# -----------------------------
# Streamlit Input
# -----------------------------
user_input = st.text_area("How are you feeling today?", height=150)

if st.button("Get Support"):
    if user_input.strip() == "":
        st.warning("Please enter how you feel.")
    else:
        response = get_emotion_response(user_input)
        st.markdown(response)
