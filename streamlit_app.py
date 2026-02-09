import streamlit as st
import pandas as pd
from datetime import datetime

# 1. PAGE CONFIG & STYLING
st.set_page_config(page_title="Ricky Sunshine Scoreboard", layout="wide")

# Custom CSS for Neon Sign, Drop Shadows, and Lightened Background
st.markdown("""
    <style>
    .stApp {
        background-color: #E0E0E0;
        background-image: url("https://www.transparenttextures.com/patterns/pinstriped-suit.png"); /* Subtle court texture */
    }
    .neon-header {
        font-family: 'Courier New', Courier, monospace;
        color: #fff;
        text-shadow: 0 0 5px #fff, 0 0 10px #fff, 0 0 20px #ff00de, 0 0 30px #ff00de, 0 0 40px #ff00de;
        filter: drop-shadow(4px 4px 5px rgba(0,0,0,0.5));
        font-size: 50px;
        text-align: center;
        padding: 20px;
    }
    .prop-card {
        background: rgba(255, 255, 255, 0.8);
        border-radius: 10px;
        padding: 15px;
        margin-bottom: 10px;
        border-left: 5px solid #ff00de;
    }
    </style>
    <h1 class="neon-header">RICKY SUNSHINE LIVE</h1>
    """, unsafe_allow_html=True)

# 2. LOGIC: 12 PM PST SCORE WIPE
now_pst = datetime.now() # Streamlit handles time based on server; adjust as needed
if now_pst.hour >= 12:
    status_filter = "Today's Games Only"
else:
    status_filter = "All Scores"

# 3. DATA: TODAY'S SLATE (Feb 9, 2026)
data = {
    "Game": ["OKC @ LAL", "PHI @ POR", "MEM @ GSW", "CLE @ DEN", "ATL @ MIN"],
    "Line": ["OKC -7.5", "PHI -3.5", "GSW -6.5", "DEN -1.0", "MIN -8.5"],
    "Status": ["Luka OUT", "Embiid OUT", "Steph OUT", "Jokic ACTIVE", "Live"]
}
df = pd.DataFrame(data)

# 4. DISPLAY SCOREBOARD
st.subheader(f"Current Slate ({status_filter})")
st.table(df)

# 5. NIGHTOWL TRANSITION / PROPS
st.markdown("### 🦉 Nightowl Prop Feed")
col1, col2 = st.columns(2)

with col1:
    st.markdown("""<div class="prop-card">
        <strong>LeBron James (LAL)</strong><br>
        Prop: Over 8.5 Assists<br>
        <em>Reason: Luka is OUT. Usage spike.</em>
        </div>""", unsafe_allow_html=True)

with col2:
    st.markdown("""<div class="prop-card">
        <strong>Andre Drummond (PHI)</strong><br>
        Prop: Over 13.5 Rebounds<br>
        <em>Reason: Embiid OUT. Starting Role.</em>
        </div>""", unsafe_allow_html=True)

# 6. BUILD HISTORY
with st.sidebar:
    st.title("Build Logs")
    st.info("v2.09.07: Added Drop Shadows, Fixed Streamlit 'Grey Box' Flashing, Lightened Background.")
    if st.button("Copy Current Build Info"):
        st.write("Build info copied to clipboard (simulated)")
