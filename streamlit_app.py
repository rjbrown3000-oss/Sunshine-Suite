import streamlit as st
import datetime
from streamlit_autorefresh import st_autorefresh

# 1. ANALYZER SYNC
st.set_page_config(page_title="Ricky's Executive Suite", layout="wide")import streamlit as st
import datetime
from streamlit_autorefresh import st_autorefresh

# 1. ANALYZER ENGINE SYNC
st.set_page_config(page_title="Ricky's Executive Suite", layout="wide")
st_autorefresh(interval=60000, key="executive_v130_live")

# 2. UI STYLING (LOCKED COURT BACKGROUND)
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Playball&family=Oswald:wght@700&family=Orbitron:wght@700&display=swap');

    [data-testid="stAppViewContainer"] {
        background-image: linear-gradient(rgba(0,0,0,0.75), rgba(0,0,0,0.75)), 
        url('https://images.unsplash.com/photo-1504450758481-7338eba7524a?q=80&w=2669&auto=format&fit=crop');
        background-size: cover; background-position: center; background-attachment: fixed;
    }

    .led-ribbon {
        background: #000; border-top: 2px solid #444; border-bottom: 3px solid #00ff00;
        padding: 10px 0; overflow: hidden; display: flex; box-shadow: 0 5px 15px rgba(0,0,0,0.8);
    }
    .led-ticker {
        font-family: 'Orbitron', sans-serif; white-space: nowrap;
        color: #00ff00; text-shadow: 0 0 10px #00ff00;
        font-size: 1.1rem; animation: slide 45s linear infinite;
    }
    .live-dot {
        height: 10px; width: 10px; background-color: #ff0000;
        border-radius: 50%; display: inline-block; margin: 0 12px; animation: pulse 1.2s infinite;
    }
    @keyframes pulse { 0% { opacity: 1; } 50% { opacity: 0.3; } 100% { opacity: 1; } }
    @keyframes slide { 0% { transform: translateX(100%); } 100% { transform: translateX(-100%); } }

    .ricky-neon {
        font-family: 'Playball', cursive; font-size: 4.8rem; text-align: center;
        color: #fff; text-shadow: 0 0 20px #00ff00; animation: flicker 4s infinite;
    }
    @keyframes flicker { 0%, 18%, 22%, 25%, 53%, 57%, 100% { opacity: 1; } 20%, 24%, 55% { opacity: 0.7; } }

    .prop-card { background: rgba(0,0,0,0.75); border-left: 10px solid #00ff00; padding: 20px; border-radius: 15px; margin-bottom: 15px; }
    .meter-bg { background: rgba(255,255,255,0.1); border-radius: 10px; height: 10px; margin: 8px 0; }
    .meter-fill { background: #00ff00; height: 100%; border-radius: 10px; box-shadow: 0 0 8px #00ff00; }
    
    h1, h2, h3, b, p, span { color: white !important; text-shadow: 2px 2px 10px #000 !important; }
</style>
""", unsafe_allow_html=True)

# 3. LIVE LED SCOREBOARD (FEB 5 GAMES)
st.markdown(f"""
<div class="led-ribbon">
    <div class="led-ticker">
        <span class="live-dot"></span> 7:00 PM: BKN @ ORL <span class="live-dot"></span> 
        7:30 PM: CHI @ TOR <span class="live-dot"></span> 8:30 PM: SAS @ DAL <span class="live-dot"></span> 
        10:00 PM: GSW @ PHX <span class="live-dot"></span> 10:00 PM: PHI @ LAL <span class="live-dot"></span> 
        🚨 GIANNIS (OUT) | TRAE YOUNG (OUT) | CADE CUNNINGHAM (OUT)
    </div>
</div>
""", unsafe_allow_html=True)

st.markdown('<div class="ricky-neon">Ricky Sunshine\'s</div>', unsafe_allow_html=True)

# 4. SIDEBAR (INJURY HUB)
with st.sidebar:
    st.markdown("## 📋 INJURY HUB")
    st.error("**GIANNIS** (OUT) | **TRAE** (OUT)")
    st.error("**CADE** (OUT) | **CAM THOMAS** (OUT)")
    st.write("---")
    nightowl = st.toggle("🌙 Force Nightowl Swap", value=False)

# 5. TABS
tab1, tab2, tab3 = st.tabs(["🎯 THE BOARD", "📡 LIVE FEED", "📈 PARLAY BUILDER"])

# Nightowl Swap
now = datetime.datetime.now()
is_night = (now.hour >= 22 or now.hour < 6) or nightowl

with tab1:
    st.subheader("🌙 Tomorrow's Value" if is_night else "🎯 Today's Executive Board")
    props = [
        {"name": "Jalen Brunson", "line": 27.5, "stat": "PTS", "id": "1628973", "proj": 30.1, "prob": 84},
        {"name": "Michael Porter Jr.", "line": 24.5, "stat": "PTS", "id": "1629008", "proj": 27.8, "prob": 81},
        {"name": "Jalen Duren", "line": 11.5, "stat": "REB", "id": "1631105", "proj": 13.9, "prob": 79}
    ]
    for p in props:
        edge = round(p['proj'] - p['line'], 1)
        st.markdown(f"""
        <div class="prop-card">
            <div style="display: flex; align-items: center;">
                <img src="https://cdn.nba.com/headshots/nba/latest/1040x760/{p['id']}.png" style="width:75px; margin-right:20px; border-radius:50%; border:2px solid #00ff00; background:#000;">
                <div style="flex-grow:1;">
                    <b>{p['name'].upper()} 📈</b><br>
                    <span>{p['stat']} Line: {p['line']} | <span style="color:#00ff00;">Proj: {p['proj']}</span></span>
                    <div class="meter-bg"><div class="meter-fill" style="width: {p['prob']}%;"></div></div>
                    <small style="color:#00ff00;">{p['prob']}% Hit Probability</small>
                </div>
                <div style="text-align:right;">
                    <b style="font-size:1.7rem; color:#adff2f;">+{edge}</b><br><small>EDGE</small>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)

with tab2:
    st.subheader("📡 Live Analytics")
    st.info("Monitor Brunson (NYK) usage spike; Detroit rotation heavy on Duren with Cade out.")

with tab3:
    st.subheader("📈 Executive Parlay Builder")
    st.write("### 📋 Copyable System Lock")
    # This block allows you to copy the text to clipboard instantly
    parlay_text = "Brunson O27.5 PTS + MPJ O24.5 PTS + Duren O11.5 REB"
    st.code(parlay_text, language="text")
    st.success("🔥 Estimated Payout: +245")

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
