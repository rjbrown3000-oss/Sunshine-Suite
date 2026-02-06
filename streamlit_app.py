import streamlit as st
import datetime
from streamlit_autorefresh import st_autorefresh

# 1. CORE ENGINE
st.set_page_config(page_title="Ricky's Shadow Suite v150", layout="wide")
st_autorefresh(interval=30000, key="stadium_sync_v150")

# 2. UI STYLING (STADIUM PERSPECTIVE + COURT BG)
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Playball&family=Inter:wght@900&display=swap');

    /* COURT BACKGROUND - FIXED & ANCHORED */
    [data-testid="stAppViewContainer"] {
        background-image: linear-gradient(rgba(255,255,255,0.2), rgba(255,255,255,0.2)), 
        url('https://images.unsplash.com/photo-1544919982-b61976f0ba43?q=80&w=2622&auto=format&fit=crop');
        background-size: cover; background-position: center; background-attachment: fixed;
    }

    /* 3D CYLINDRICAL STADIUM SCOREBOARD */
    .stadium-wrapper {
        perspective: 1000px;
        overflow: hidden;
        background: #000;
        border-bottom: 5px solid #00ff00;
        padding: 15px 0;
    }
    .stadium-ticker {
        display: flex;
        white-space: nowrap;
        font-family: 'Inter', sans-serif;
        color: #00ff00;
        font-weight: 900;
        font-size: 1.6rem;
        animation: stadium-spin 25s linear infinite;
        transform-style: preserve-3d;
    }
    @keyframes stadium-spin {
        0% { transform: rotateY(-15deg) translateX(100%); }
        50% { transform: rotateY(0deg) translateX(0%); filter: drop-shadow(0 0 10px #00ff00); }
        100% { transform: rotateY(15deg) translateX(-100%); }
    }

    .stTabs [data-baseweb="tab"] { background-color: rgba(10,10,10,0.95) !important; color: white !important; }
    .prop-card { background: rgba(0,0,0,0.92); border-left: 10px solid #00ff00; padding: 20px; border-radius: 12px; margin-bottom: 12px; box-shadow: 4px 4px 10px rgba(0,0,0,0.5); }
    .vegas-pill { background: #111; color: #00ff00; padding: 4px 8px; border-radius: 5px; font-size: 0.8rem; border: 1px solid #00ff00; }
</style>
""", unsafe_allow_html=True)

# 3. THE STADIUM SCOREBOARD (TODAY'S GAMES ONLY - FEB 6)
st.markdown("""
<div class="stadium-wrapper">
    <div class="stadium-ticker">
        🏀 NYK @ DET (4:30) | 🏀 MIA @ BOS (4:30) | 🏀 IND @ MIL (5:00) | 🏀 NOP @ MIN (5:00) | 🏀 MEM @ POR (7:00) | 🏀 LAC @ SAC (7:00)
        <span style="margin: 0 50px;"></span>
        🚨 LINE ALERT: JOSH HART BUMPED TO 24.5 PRA | 🚨 LINE ALERT: BOBBY PORTIS BUMPED TO 18.5 PTS
    </div>
</div>
""", unsafe_allow_html=True)

st.markdown('<div style="font-family:\'Playball\'; font-size:5.5rem; text-align:center; color:#e0ffe0; text-shadow: 0 0 10px #00ff00; margin-top:20px;">Ricky Sunshine\'s</div>', unsafe_allow_html=True)

# 4. PLAYER DATA WITH VEGAS PROBABILITY
# Selenium would populate this list
props = [
    {"name": "Josh Hart", "line": 24.5, "stat": "P+R+A", "vegas_prob": "56.4%", "diff": "+1.0", "hit": 91},
    {"name": "Bobby Portis", "line": 18.5, "stat": "PTS", "vegas_prob": "58.2%", "diff": "+2.0", "hit": 89},
    {"name": "Jaylen Brown", "line": 28.5, "stat": "PTS", "vegas_prob": "54.8%", "diff": "+1.0", "hit": 87},
    {"name": "Cade Cunningham", "line": 26.5, "stat": "PTS", "vegas_prob": "51.2%", "diff": "0.0", "hit": 86},
]

tab1, tab2, tab3 = st.tabs(["🎯 THE BOARD", "📡 LINE CHANGES", "🎰 PP BUILDER"])

with tab1:
    for p in props:
        col1, col2 = st.columns([3, 1])
        with col1:
            st.markdown(f"""
            <div class="prop-card">
                <b style="font-size:1.4rem;">{p['name'].upper()}</b> 
                <span style="float:right;" class="vegas-pill">Vegas Implied: {p['vegas_prob']}</span><br>
                <span style="color:#aaa;">{p['stat']} Line: {p['line']}</span><br>
                <small style="color:#00ff00;">Shadow Hit Rate: {p['hit']}%</small>
            </div>
            """, unsafe_allow_html=True)
        with col2:
            st.code(f"BUMP: {p['diff']}")
            st.button(f"Copy {p['name']}", key=p['name'])
