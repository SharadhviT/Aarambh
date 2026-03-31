import pandas as pd
import random

RESPONSES_URL = "https://raw.githubusercontent.com/<your-username>/Aarambh/main/data/responses_large.csv"
RESOURCES_URL = "https://raw.githubusercontent.com/<your-username>/Aarambh/main/data/resources.csv"

responses_df = pd.read_csv(RESPONSES_URL)
resources_df = pd.read_csv(RESOURCES_URL)

def detect_mood(text):
    text = text.lower()
    if any(w in text for w in ["happy", "great", "good"]):
        return "happy"
    elif any(w in text for w in ["sad", "down"]):
        return "sad"
    elif any(w in text for w in ["angry", "mad"]):
        return "angry"
    elif any(w in text for w in ["anxious", "stressed"]):
        return "anxious"
    else:
        return "neutral"

def get_recommendation(mood):
    mood_responses = responses_df[responses_df['mood'] == mood]['response'].tolist()
    return random.choice(mood_responses)

def get_resources(category=None):
    if category:
        return resources_df[resources_df['category'] == category]
    return resources_df
