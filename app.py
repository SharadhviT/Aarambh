import streamlit as st
import pandas as pd
import plotly.express as px
from utils import detect_mood, get_recommendation, get_resources

st.set_page_config(page_title="Aarambh", page_icon="💛", layout="wide")

st.title("💛 Aarambh — Teen Emotional Support")
st.markdown("Track your mood and get support.")

# --- Mood Input ---
st.header("How are you feeling?")
user_input = st.text_area("Type here")

if st.button("Submit"):
    if user_input.strip() == "":
        st.warning("Enter something")
    else:
        mood = detect_mood(user_input)
        st.success(f"Mood detected: {mood}")
        st.info(get_recommendation(mood))

        if "history" not in st.session_state:
            st.session_state.history = []
        st.session_state.history.append(mood)

# --- Graph ---
st.header("Mood Tracker")

if "history" in st.session_state and st.session_state.history:
    df = pd.DataFrame(st.session_state.history, columns=["mood"])
    fig = px.bar(df["mood"].value_counts())
    st.plotly_chart(fig)
else:
    st.info("No data yet")

# --- Resources ---
st.header("Resources")

category = st.selectbox("Filter", ["All","helpline","mindfulness","creative","social","education"])

data = get_resources(None if category=="All" else category)

for _, row in data.iterrows():
    st.markdown(f"**{row['name']}** - {row['description']} [Link]({row['link']})")

# --- Download ---
if "history" in st.session_state:
    df = pd.DataFrame(st.session_state.history, columns=["mood"])
    st.download_button("Download CSV", df.to_csv(index=False))
