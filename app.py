import streamlit as st

# -----------------------------
# 20+ emotions and responses
# -----------------------------
EMOTION_KEYWORDS = {
    "happy": ["happy", "joy", "glad", "cheerful", "smile", "delighted"],
    "sad": ["sad", "unhappy", "down", "depressed", "cry", "lonely"],
    "angry": ["angry", "mad", "furious", "annoyed", "frustrated"],
    "anxious": ["anxious", "worried", "nervous", "scared", "uneasy"],
    "excited": ["excited", "thrilled", "ecstatic", "pumped", "energized"],
    "bored": ["bored", "uninterested", "meh", "dull", "tired of"],
    "confused": ["confused", "lost", "unsure", "puzzled", "uncertain"],
    "lonely": ["lonely", "isolated", "alone", "abandoned"],
    "tired": ["tired", "sleepy", "exhausted", "drained", "fatigued"],
    "stressed": ["stressed", "pressure", "overwhelmed", "tense"],
    "motivated": ["motivated", "driven", "inspired", "determined"],
    "surprised": ["surprised", "shocked", "amazed", "astonished"],
    "hopeful": ["hopeful", "optimistic", "confident", "positive"],
    "disappointed": ["disappointed", "let down", "sad", "regretful"],
    "guilty": ["guilty", "remorse", "ashamed", "sorry"],
    "jealous": ["jealous", "envious", "resentful"],
    "proud": ["proud", "accomplished", "fulfilled"],
    "relaxed": ["relaxed", "calm", "peaceful", "chill"],
    "curious": ["curious", "interested", "inquiring", "questioning"],
    "grateful": ["grateful", "thankful", "appreciative"],
    "nostalgic": ["nostalgic", "memories", "reminiscing", "sentimental"],
    "shy": ["shy", "timid", "quiet", "reserved"]
}

RESPONSES = {
    "happy": "That's wonderful! Keep smiling 🙂",
    "sad": "I'm here for you. It's okay to feel sad 😔",
    "angry": "Take a deep breath. I understand you're angry 😡",
    "anxious": "Try some slow breathing. You can get through this 😟",
    "excited": "Wow! That's exciting! 🎉",
    "bored": "Let's find something fun to do 🤔",
    "confused": "No worries, let's break it down together 🤓",
    "lonely": "You're not alone. I'm here 💛",
    "tired": "Make sure to rest. Self-care matters 😴",
    "stressed": "Let's try to relax for a few minutes 🧘",
    "motivated": "Keep going! You're doing great 💪",
    "surprised": "Oh! That's unexpected 😲",
    "hopeful": "Keep faith! Things can get better 🌈",
    "disappointed": "It's okay to feel disappointed. You'll bounce back 💛",
    "guilty": "Remember, everyone makes mistakes. Forgive yourself 💙",
    "jealous": "Focus on your own growth. Comparison is tough 💚",
    "proud": "You should feel proud! 🎖️",
    "relaxed": "Enjoy this calm moment 😌",
    "curious": "That's interesting! Let's explore 🧐",
    "grateful": "Feeling grateful is powerful 🙏",
    "nostalgic": "Ah, memories… cherish them 💛",
    "shy": "It's okay to take your time 😊",
    "neutral": "I hear you. Tell me more."
}

# -----------------------------
# Functions
# -----------------------------
def detect_emotion(user_input):
    user_input = user_input.lower()
    for emotion, keywords in EMOTION_KEYWORDS.items():
        if any(word in user_input for word in keywords):
            return emotion
    return "neutral"

def get_response(user_input):
    emotion = detect_emotion(user_input)
    return RESPONSES.get(emotion, RESPONSES["neutral"])

# -----------------------------
# Streamlit UI
# -----------------------------
st.set_page_config(page_title="Aarambh - Emotional Support", layout="centered")
st.title("💛 Aarambh - Teen Emotional Support")
st.markdown("Talk to me about how you feel. I understand 20+ emotions!")

user_input = st.text_input("How are you feeling today?")

if user_input:
    response = get_response(user_input)
    st.markdown(f"**Aarambh:** {response}")
