# utils/helpers.py

import pandas as pd

# Load responses
def load_responses(csv_path="responses.csv"):
    df = pd.read_csv(csv_path)
    return {row['emotion']: row['response'] for _, row in df.iterrows()}

# 20+ emotions keywords mapping
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

# Detect emotion from user input
def detect_emotion(user_input):
    user_input = user_input.lower()
    for emotion, keywords in EMOTION_KEYWORDS.items():
        if any(word in user_input for word in keywords):
            return emotion
    return "neutral"

# Get response for an emotion
def get_response(user_input, responses):
    emotion = detect_emotion(user_input)
    return responses.get(emotion, "I hear you. Tell me more.")
