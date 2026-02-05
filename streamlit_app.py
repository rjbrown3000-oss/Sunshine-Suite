import streamlit as st
import datetime
from streamlit_autorefresh import st_autorefresh

# 1. PAGE SYNC
st.set_page_config(page_title="Ricky's Executive Suite", layout="wide")
st_autorefresh(interval=60000, key="executive_sync")

# 2. THE ANALYZER UI (STYLING ONLY - NO BACKGROUND CHANGES)
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Playball&family=Oswald:wght@700&family=Orbitron:wght@700&display=swap');

    /* LED SCOREBOARD STYLING */
    .led-container {
        background: #000;
        border-top: 2px solid #333;
        border-bottom: 2px solid #00ff00;
        padding: 8px 0;
        overflow: hidden;
        display: flex;
    }
    .led-text {
        font-family: 'Orbitron', sans-serif;
        white-space: nowrap;
        color: #00ff00;
        text-shadow: 0 0 10px #00ff00;
        font-size: 1.1rem;
        animation: ticker 35s linear infinite;
    }
    /* MINI ANIMATION: PULSING DOT */
    .live-dot {
        height: 10px; width: 10px; background-color: #ff0000;
        border-radius: 50%; display: inline-block;
        margin: 0 10px; animation: pulse 1s infinite;
    }
    @keyframes pulse { 0% { opacity: 1; } 50% { opacity: 0.3; } 100% { opacity: 1; } }
    @keyframes ticker { 0% { transform: translateX(100%); } 100% { transform: translateX(-100%); } }

    /* FLICKER TITLE */
    .flicker-title {
        font-family: 'Playball', cursive; font-size: 4.5rem; text-align: center;
        color: #fff; text-shadow: 0 0 20px #00ff00; animation: ricky-flicker 3s infinite;
    }
    @keyframes ricky-flicker {
        0%, 19%, 21%, 23%, 25%, 54%, 56%, 100% { opacity: 1; }
        20%, 22%, 24%, 55% { opacity: 0.6; }
    }

    /* PROP CARDS & TABS */
    .stTabs [data-baseweb="tab-list"] { gap: 10px; }
    .stTabs [data-baseweb="tab"] {
        background-color: rgba(255,255,255,0.05);
        border-radius: 10px 10px 0 0;
        padding: 10px 20px;
        color: white;
    }
    .prop-card {
        background: rgba(0,0,0,0.6);
        border-left: 8px solid #00ff00;
        padding: 15px;
        border-radius: 12px;
        margin-bottom: 10px;
    }
    h1, h2, h3, b, p, span { color: white !important; text-shadow: 2px 2px 8px #000 !important; }
</style>
""", unsafe_allow_html=True)

# 3. LED SCOREBOARD (WITH ANIMATIONS)
st.markdown(f"""
<div class="led-container">
    <div class="led-text">
        <span class="live-dot"></span> FEB 5-6 ANALYTICS: GIANNIS (OUT) <span class="live-dot"></span> 
        BRUNSON O/U 27.5 [HOT] <span class="live-dot"></span> 
        LATE NIGHT TRANSITION: ACTIVE <span class="live-dot"></span> 
        🔥 LOCK OF THE NIGHT: JALEN DUREN REBS 📈
    </div>
</div>
""", unsafe_allow_html=True)

st.markdown('<div class="flicker-title">Ricky Sunshine\'s</div>', unsafe_allow_html=True)

# 4. SIDEBAR (INJURY REPORT)
with st.sidebar:
    st.markdown("## 📋 INJURY REPORT")
    st.error("GIANNIS: OUT (CALF)")
    st.error("TRAE YOUNG: OUT (KNEE)")
    st.warning("CADE CUNNINGHAM: GTD")
    st.write("---")
    st.write("### 🌙 Nightowl Control")
    nightowl_manual = st.toggle("Force Nightowl Mode", value=False)

# 5. TABS & PROP ANALYZER
tab1, tab2, tab3 = st.tabs(["🎯 THE BOARD", "📡 LIVE FEED", "📈 PARLAY BUILDER"])

now = datetime.datetime.now()
is_night = (now.hour >= 22 or now.hour < 6) or nightowl_manual

with tab1:
    st.markdown(f"### {'🌙 Tomorrow\'s Early Value' if is_night else '🎯 Today\'s Live Board'}")
    
    # Analyzer Logic
    props = [
        {"name": "Jalen Brunson", "line": 27.5, "stat": "PTS", "id": "1628973", "proj": 29.8},
        {"name": "Jalen Duren", "line": 11.5, "stat": "REB", "id": "1631105", "proj": 13.2}
    ]
    
    for p in props:
        diff = round(p['proj'] - p['line'], 1)
        st.markdown(f"""
        <div class="prop-card">
            <div style="display: flex; align-items: center;">
                <img src="https://cdn.nba.com/headshots/nba/latest/1040x760/{p['id']}.png" style="width:70px; margin-right:15px; border-radius:50%; border:1px solid #00ff00;">
                <div style="flex-grow:1;">
                    <b style="font-size:1.2rem;">{p['name']}</b><br>
                    <span>{p['stat']} Line: {p['line']} | <span style="color:#00ff00;">Proj: {p['proj']}</span></span>
                </div>
                <div style="text-align:right;">
                    <b style="font-size:1.5rem; color:#00ff00;">+{diff}</b><br>
                    <small>EDGE</small>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)

with tab2:
    st.markdown("### 📡 Live Analytics Feed")
    st.write("• SGA usage spike expected with backup minutes shifting.")
    st.write("• Detroit transition defense ranking bottom 5; monitor opposing PG speeds.")

with tab3:
    st.markdown("### 🔥 Parlay Builder")
    st.info("Select props from the board to build your ticket (Feature integration pending).")
