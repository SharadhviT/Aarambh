import json
import random
import pandas as pd
import nltk
nltk.download('punkt')
from textblob import TextBlob

# Load responses
def load_responses(file_path="data/responses.json"):
    with open(file_path, "r") as f:
        return json.load(f)

# Get a random response for the chosen emotion
def get_response(emotion, responses):
    matched = [r['response'] for r in responses if r['emotion'] == emotion]
    return random.choice(matched) if matched else "Sorry, no response found."

# Optional: Detect emotion from text
def detect_emotion(user_text):
    polarity = TextBlob(user_text).sentiment.polarity
    if polarity > 0.3:
        return "happy"
    elif polarity < -0.3:
        return "sad"
    else:
        return "stressed"

# Log mood entry to CSV
def log_mood(emotion, user_text, file_path="data/mood_log.csv"):
    df = pd.DataFrame([[pd.Timestamp.now(), emotion, user_text]],
                      columns=["date","emotion","input"])
    df.to_csv(file_path, mode='a', header=False, index=False)
