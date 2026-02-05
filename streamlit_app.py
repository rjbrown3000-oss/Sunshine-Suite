import streamlit as st
import datetime
import random
from streamlit_autorefresh import st_autorefresh

# 1. ANALYZER SYNC
st.set_page_config(page_title="Ricky's Executive Suite", layout="wide")
st_autorefresh(interval=60000, key="executive_sync_v126")

# 2. THE BRAIN: LED & PROBABILITY UI
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Playball&family=Oswald:wght@700&family=Orbitron:wght@700&display=swap');

    /* LED SCOREBOARD */
    .led-board {
        background: #000;
        border-top: 2px solid #444;
        border-bottom: 2px solid #00ff00;
        padding: 10px 0;
        overflow: hidden;
        display: flex;
    }
    .led-ticker {
        font-family: 'Orbitron', sans-serif;
        white-space: nowrap;
        color: #00ff00;
        text-shadow: 0 0 8px #00ff00;
        font-size: 1.1rem;
        animation: slide-left 45s linear infinite;
    }
    .led-dot {
        height: 10px; width: 10px; background-color: #ff0000;
        border-radius: 50%; display: inline-block;
        margin: 0 12px; animation: pulse 1s infinite;
    }
    @keyframes pulse { 0% { opacity: 1; } 50% { opacity: 0.2; } 100% { opacity: 1; } }
    @keyframes slide-left { 0% { transform: translateX(100%); } 100% { transform: translateX(-100%); } }

    /* RICKY'S NEON TITLE */
    .ricky-title {
        font-family: 'Playball', cursive; font-size: 5rem; text-align: center;
        color: #fff; text-shadow: 0 0 20px #00ff00; animation: neon-flicker 4s infinite;
    }
    @keyframes neon-flicker {
        0%, 18%, 22%, 25%, 53%, 57%, 100% { opacity: 1; }
        20%, 24%, 55% { opacity: 0.6; }
    }

    /* PROBABILITY METERS */
    .meter-bg {
        background: rgba(255,255,255,0.1);
        border-radius: 10px;
        height: 12px;
        width: 100%;
        margin-top: 8px;
    }
    .meter-fill {
        background: linear-gradient(90deg, #00ff00, #adff2f);
        height: 100%;
        border-radius: 10px;
        box-shadow: 0 0 10px #00ff00;
    }

    /* CARD STYLING */
    .prop-card {
        background: rgba(0,0,0,0.7); 
        border-left: 10px solid #00ff00;
        padding: 20px; 
        border-radius: 15px; 
        margin-bottom: 15px;
    }
    h1, h2, h3, b, p, span { color: white !important; text-shadow: 2px 2px 10px #000 !important; }
</style>
""", unsafe_allow_html=True)

# 3. LED DISPLAY
st.markdown(f"""
<div class="led-board">
    <div class="led-ticker">
        <span class="led-dot"></span> FEB 5-6: GIANNIS (OUT) <span class="led-dot"></span> 
        TRAE YOUNG (OUT) <span class="led-dot"></span> CUNNINGHAM (GTD) <span class="led-dot"></span> 
        PROBABILITY ENGINE: ONLINE <span class="led-dot"></span> 🏀 NIGHTOWL MODE STANDBY
    </div>
</div>
""", unsafe_allow_html=True)

st.markdown('<div class="ricky-title">Ricky Sunshine\'s</div>', unsafe_allow_html=True)

# 4. SIDEBAR INJURY REPORT
with st.sidebar:
    st.markdown("## 📊 INJURY REPORT")
    st.error("**GIANNIS ANTETOKOUNMPO**\n\nOUT (Calf)")
    st.error("**TRAE YOUNG**\n\nOUT (Knee)")
    st.warning("**CADE CUNNINGHAM**\n\nGTD (Wrist)")
    st.write("---")
    force_night = st.toggle("🌙 Manual Nightowl Swap")

# 5. TABS & ANALYZER
tab1, tab2, tab3 = st.tabs(["🎯 THE BOARD", "📡 LIVE FEED", "📈 PARLAYS"])

now = datetime.datetime.now()
is_night = (now.hour >= 22 or now.hour < 6) or force_night

with tab1:
    st.subheader("🌙 Nightowl Early Lines" if is_night else "🎯 Active Projections")
    
    # Analyzer Data with Confidence/Probability
    props = [
        {"name": "Michael Porter Jr.", "line": 24.5, "stat": "PTS", "id": "1629008", "proj": 27.2, "prob": 78},
        {"name": "Kelly Oubre Jr.", "line": 14.5, "stat": "PTS", "id": "1626162", "proj": 16.1, "prob": 64},
        {"name": "Jalen Duren", "line": 11.5, "stat": "REB", "id": "1631105", "proj": 13.8, "prob": 82}
    ]

    for p in props:
        edge = round(p['proj'] - p['line'], 1)
        st.markdown(f"""
        <div class="prop-card">
            <div style="display: flex; align-items: center;">
                <img src="https://cdn.nba.com/headshots/nba/latest/1040x760/{p['id']}.png" style="width:80px; margin-right:20px; border-radius:50%; border:2px solid #00ff00; background:#000;">
                <div style="flex-grow:1;">
                    <b style="font-size:1.4rem;">{p['name'].upper()}</b><br>
                    <span>{p['stat']} Line: {p['line']} | <span style="color:#00ff00;">Proj: {p['proj']}</span></span>
                    <div class="meter-bg"><div class="meter-fill" style="width: {p['prob']}%;"></div></div>
                    <small style="color:#00ff00;">{p['prob']}% Hit Probability</small>
                </div>
                <div style="text-align:right; min-width:80px;">
                    <b style="font-size:1.8rem; color:#00ff00;">+{edge}</b><br><small>EDGE</small>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)

with tab2:
    st.info("📡 **Live Intel:** Monitor Detroit rotations; Duren's rebounding edge has increased due to interior matchups.")

with tab3:
    st.subheader("📈 Executive Parlay Builder")
    # This success message was causing the crash because it wasn't closed correctly
    st.success("📈 **Executive Lock:** MPJ (O24.5) + Jalen Duren (O11.5 REB) = +245 Estimated")
    
    st.write("---")
    st.info("💡 **Selection Mode:** Click the player cards in 'The Board' to add them to your slip. (Logic integration in progress)")
