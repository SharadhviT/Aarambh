# utils/helpers.py
import nltk
nltk.download('punkt')  # required for TextBlob

from textblob import TextBlob
import pandas as pd
import os
from datetime import datetime
import json

# ---------------------------
# Load predefined responses
# ---------------------------
def load_responses(file_path="responses.json"):
    """
    Load chatbot responses from a JSON file.
    """
    if not os.path.exists(file_path):
        return {}
    with open(file_path, "r", encoding="utf-8") as f:
        data = json.load(f)
    return data

# ---------------------------
# Get response based on input
# ---------------------------
def get_response(user_input, responses_dict):
    """
    Returns a response based on user input matching keywords.
    """
    for key, response in responses_dict.items():
        if key.lower() in user_input.lower():
            return response
    return "I'm here to listen. Can you tell me more?"

# ---------------------------
# Detect emotion using TextBlob
# ---------------------------
def detect_emotion(text):
    """
    Simple emotion detection using TextBlob polarity.
    Returns 'Positive', 'Negative', or 'Neutral'
    """
    analysis = TextBlob(text)
    polarity = analysis.sentiment.polarity
    if polarity > 0.2:
        return "Positive"
    elif polarity < -0.2:
        return "Negative"
    else:
        return "Neutral"

# ---------------------------
# Log moods into CSV
# ---------------------------
def log_mood(user_input, emotion, log_file="mood_log.csv"):
    """
    Save user's input and detected emotion into a CSV.
    """
    df = pd.DataFrame([[datetime.now(), user_input, emotion]], columns=["Timestamp", "Input", "Emotion"])
    if os.path.exists(log_file):
        df_existing = pd.read_csv(log_file)
        df = pd.concat([df_existing, df], ignore_index=True)
    df.to_csv(log_file, index=False)
