import streamlit as st
import datetime
from streamlit_autorefresh import st_autorefresh

# 1. ANALYZER SYNC
st.set_page_config(page_title="Ricky's Executive Suite", layout="wide")
st_autorefresh(interval=60000, key="executive_v127_lock")

# 2. THE UI: COURT, LED, & METERS
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Playball&family=Oswald:wght@700&family=Orbitron:wght@700&display=swap');

    /* RESTORED BASKETBALL COURT */
    [data-testid="stAppViewContainer"] {
        background-image: linear-gradient(rgba(0,0,0,0.75), rgba(0,0,0,0.75)), 
        url('https://images.unsplash.com/photo-1504450758481-7338eba7524a?q=80&w=2669&auto=format&fit=crop');
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
    }

    /* LED SCOREBOARD */
    .led-board {
        background: #000;
        border-top: 2px solid #444; border-bottom: 2px solid #00ff00;
        padding: 10px 0; overflow: hidden; display: flex;
    }
    .led-ticker {
        font-family: 'Orbitron', sans-serif; white-space: nowrap;
        color: #00ff00; text-shadow: 0 0 8px #00ff00;
        font-size: 1.1rem; animation: slide-left 40s linear infinite;
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
    .meter-bg { background: rgba(255,255,255,0.1); border-radius: 10px; height: 10px; width: 100%; margin-top: 5px; }
    .meter-fill { background: #00ff00; height: 100%; border-radius: 10px; box-shadow: 0 0 8px #00ff00; }

    /* CARDS */
    .prop-card {
        background: rgba(0,0,0,0.7); border-left: 10px solid #00ff00;
        padding: 20px; border-radius: 15px; margin-bottom: 15px;
    }
    h1, h2, h3, b, p, span { color: white !important; text-shadow: 2px 2px 10px #000 !important; }
</style>
""", unsafe_allow_html=True)

# 3. LED DISPLAY
st.markdown(f"""
<div class="led-board">
    <div class="led-ticker">
        <span class="led-dot"></span> FEB 5-6: GIANNIS (OUT) <span class="led-dot"></span> 
        TRAE YOUNG (OUT) <span class="led-dot"></span> BRUNSON O/U 27.5 [HOT] <span class="led-dot"></span> 
        🏀 ANALYZER V.127 ONLINE <span class="led-dot"></span> NIGHTOWL SWAP: STANDBY
    </div>
</div>
""", unsafe_allow_html=True)

st.markdown('<div class="ricky-title">Ricky Sunshine\'s</div>', unsafe_allow_html=True)

# 4. SIDEBAR
with st.sidebar:
    st.markdown("## 📊 INJURY REPORT")
    st.error("**GIANNIS** (OUT) | **TRAE** (OUT)")
    st.warning("**CUNNINGHAM** (GTD)")
    st.write("---")
    night_toggle = st.toggle("🌙 Manual Nightowl")

# 5. TABS
tab1, tab2, tab3 = st.tabs(["🎯 THE BOARD", "📡 LIVE FEED", "📈 PARLAYS"])

with tab1:
    props = [
        {"name": "Michael Porter Jr.", "line": 24.5, "stat": "PTS", "id": "1629008", "proj": 27.2, "prob": 78, "trend": "up"},
        {"name": "Jalen Duren", "line": 11.5, "stat": "REB", "id": "1631105", "proj": 13.8, "prob": 82, "trend": "up"}
    ]
    for p in props:
        trend_icon = "📈" if p['trend'] == "up" else "📉"
        edge = round(p['proj'] - p['line'], 1)
        st.markdown(f"""
        <div class="prop-card">
            <div style="display: flex; align-items: center;">
                <img src="https://cdn.nba.com/headshots/nba/latest/1040x760/{p['id']}.png" style="width:70px; margin-right:15px; border-radius:50%; border:2px solid #00ff00;">
                <div style="flex-grow:1;">
                    <b>{p['name'].upper()} {trend_icon}</b><br>
                    <span>{p['stat']} Line: {p['line']} | <span style="color:#00ff00;">Proj: {p['proj']}</span></span>
                    <div class="meter-bg"><div class="meter-fill" style="width: {p['prob']}%;"></div></div>
                    <small style="color:#00ff00;">{p['prob']}% Hit Probability</small>
                </div>
                <div style="text-align:right;">
                    <b style="font-size:1.5rem; color:#00ff00;">+{edge}</b><br><small>EDGE</small>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)

with tab2:
    st.info("📡 Live data polling in progress...")

with tab3:
    st.success("📈 **Executive Lock:** MPJ (O24.5) + Jalen Duren (O11.5 REB) = +245 Estimated")
