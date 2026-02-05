import streamlit as st
import datetime
from streamlit_autorefresh import st_autorefresh

# 1. ANALYZER ENGINE SYNC
st.set_page_config(page_title="Ricky's Executive Suite", layout="wide")
st_autorefresh(interval=60000, key="executive_flicker")

# 2. THE UI BRAIN (NO BACKGROUND TOUCHED)
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Playball&family=Oswald:wght@700&family=Orbitron:wght@700&display=swap');

    /* LED SCOREBOARD DISPLAY */
    .led-display {
        background: #000;
        border-top: 2px solid #444;
        border-bottom: 2px solid #00ff00;
        padding: 10px 0;
        overflow: hidden;
        display: flex;
        box-shadow: 0 5px 15px rgba(0,0,0,0.5);
    }
    .led-ticker {
        font-family: 'Orbitron', sans-serif;
        white-space: nowrap;
        color: #00ff00;
        text-shadow: 0 0 8px #00ff00;
        font-size: 1.1rem;
        animation: slide-left 40s linear infinite;
    }
    .status-pulse {
        height: 10px; width: 10px; background-color: #ff0000;
        border-radius: 50%; display: inline-block;
        margin: 0 10px; animation: pulse 1s infinite;
    }
    @keyframes pulse { 0% { opacity: 1; } 50% { opacity: 0.2; } 100% { opacity: 1; } }
    @keyframes slide-left { 0% { transform: translateX(100%); } 100% { transform: translateX(-100%); } }

    /* RICKY'S NEON TITLE */
    .ricky-title {
        font-family: 'Playball', cursive; font-size: 4.8rem; text-align: center;
        color: #fff; text-shadow: 0 0 20px #00ff00; animation: neon-flicker 4s infinite;
    }
    @keyframes neon-flicker {
        0%, 18%, 22%, 25%, 53%, 57%, 100% { opacity: 1; }
        20%, 24%, 55% { opacity: 0.6; }
    }

    /* TABS & SIDEBAR TEXT */
    h1, h2, h3, b, p, span { color: white !important; text-shadow: 2px 2px 8px #000 !important; }
    .prop-card {
        background: rgba(0,0,0,0.65); border-left: 8px solid #00ff00;
        padding: 15px; border-radius: 12px; margin-bottom: 12px;
    }
</style>
""", unsafe_allow_html=True)

# 3. THE LED SCOREBOARD
st.markdown(f"""
<div class="led-display">
    <div class="led-ticker">
        <span class="status-pulse"></span> FEB 5-6 INTEL: GIANNIS (OUT - CALF) <span class="status-pulse"></span> 
        TRAE YOUNG (OUT - KNEE) <span class="status-pulse"></span> CUNNINGHAM (GTD) <span class="status-pulse"></span> 
        MPJ OVER 24.5 [EDGE +2.3] <span class="status-pulse"></span> ⚡ LATE NIGHT TRANSITION: STANDBY
    </div>
</div>
""", unsafe_allow_html=True)

st.markdown('<div class="ricky-title">Ricky Sunshine\'s</div>', unsafe_allow_html=True)

# 4. THE SIDEBAR (INJURY REPORT & TOGGLES)
with st.sidebar:
    st.markdown("## 📊 ANALYZER SETTINGS")
    st.write("---")
    st.error("**GIANNIS ANTETOKOUNMPO**\n\nStatus: OUT (Right Calf)")
    st.error("**TRAE YOUNG**\n\nStatus: OUT (Right Knee)")
    st.warning("**CADE CUNNINGHAM**\n\nStatus: Questionable (Wrist)")
    st.write("---")
    night_mode = st.toggle("🌙 Force Nightowl Transition", value=False)

# 5. TABS & PROP ANALYZER
tab1, tab2, tab3 = st.tabs(["🎯 THE BOARD", "📡 LIVE FEED", "📈 PARLAY BUILDER"])

# Nightowl Logic
now = datetime.datetime.now()
is_nightowl = (now.hour >= 22 or now.hour < 6) or night_mode

with tab1:
    header = "🌙 Tomorrow's Early Props (Feb 6)" if is_nightowl else "🎯 Today's Live Projections"
    st.subheader(header)
    
    # Active Prop Data
    active_props = [
        {"name": "Michael Porter Jr.", "line": 24.5, "stat": "PTS", "id": "1629008", "proj": 26.8},
        {"name": "Kelly Oubre Jr.", "line": 14.5, "stat": "PTS", "id": "1626162", "proj": 15.9}
    ]
    
    for p in active_props:
        edge = round(p['proj'] - p['line'], 1)
        st.markdown(f"""
        <div class="prop-card">
            <div style="display: flex; align-items: center;">
                <img src="https://cdn.nba.com/headshots/nba/latest/1040x760/{p['id']}.png" style="width:75px; margin-right:15px; border-radius:50%; border:1px solid #00ff00; background:#000;">
                <div style="flex-grow:1;">
                    <b>{p['name'].upper()}</b><br>
                    <span>{p['stat']} Line: {p['line']} | <span style="color:#00ff00;">Proj: {p['proj']}</span></span>
                </div>
                <div style="text-align:right;">
                    <b style="font-size:1.4rem; color:#00ff00;">+{edge}</b><br><small>EDGE</small>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)

with tab2:
    st.subheader("📡 Live Rotation Feed")
    st.write("• **Brooklyn Alert:** MPJ seeing increased volume in early shootarounds.")
    st.write("• **Philadelphia Alert:** Kelly Oubre Jr. has hit 15+ PTS in 3 straight games.")

with tab3:
    st.subheader("📈 Executive Parlay Builder")
    st.info("Select props from the board to calculate total odds. (Session State initialization in progress)")
