import streamlit as st
import datetime
import pandas as pd
from streamlit_autorefresh import st_autorefresh

# 1. CORE ENGINE
st.set_page_config(page_title="Ricky's Shadow Tracker", layout="wide")
st_autorefresh(interval=30000, key="prizepicks_sync_v147")

# 2. UI STYLING (FAST 3D LED + LIGHT BG)
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Playball&family=Inter:wght@600;900&display=swap');
    [data-testid="stAppViewContainer"] {
        background-image: linear-gradient(rgba(255,255,255,0.18), rgba(255,255,255,0.18)), 
        url('https://images.unsplash.com/photo-1504450758481-7338eba7524a?q=80&w=2669&auto=format&fit=crop');
        background-size: cover; background-position: center; background-attachment: fixed;
    }
    .curve-outer { perspective: 1500px; background: #000; overflow: hidden; border-bottom: 4px solid #00ff00; padding: 10px 0; }
    .curved-ticker { display: flex; white-space: nowrap; font-family: 'Inter', sans-serif; color: #00ff00; font-weight: 900; font-size: 1.4rem; animation: scroll-3d-fast 20s linear infinite; }
    @keyframes scroll-3d-fast { 0% { transform: translateX(110%) rotateY(-15deg) scale(0.95); } 50% { transform: translateX(0%) rotateY(0deg) scale(1.15); } 100% { transform: translateX(-110%) rotateY(15deg) scale(0.95); } }
    .stTabs [data-baseweb="tab"] { background-color: rgba(20,20,20,0.95) !important; border-radius: 10px 10px 0 0; box-shadow: 0px 4px 15px rgba(0,0,0,0.6); }
    .prop-card { background: rgba(0,0,0,0.88); border-left: 10px solid #00ff00; padding: 15px; border-radius: 12px; margin-bottom: 10px; }
    .move-alert { color: #ff4b4b; font-weight: 800; font-size: 0.8rem; }
</style>
""", unsafe_allow_html=True)

# 3. 12 PM PST RESET SCOREBOARD (TODAY'S GAMES ONLY)
st.markdown("""
<div class="curve-outer">
    <div class="curved-ticker">
        📅 4:30 PM: NYK @ DET | 📅 4:30 PM: MIA @ BOS | 📅 5:00 PM: IND @ MIL | 📅 5:00 PM: PHI @ ORL | 📅 5:00 PM: CHA @ CLE | 📅 5:00 PM: MIN @ CHI | 📅 7:00 PM: MEM @ POR | 📅 7:00 PM: ATL @ PHX
    </div>
</div>
""", unsafe_allow_html=True)

st.markdown('<div class="neon-sign" style="text-align:center; font-family:\'Playball\'; font-size:5rem; color:#e0ffe0; text-shadow: 0 0 10px #00ff00;">Ricky Sunshine\'s</div>', unsafe_allow_html=True)

# 4. LINE MOVEMENT DATA (SIMULATED FOR FEB 6)
# Logic: If 'current' != 'open', flag it.
baseline_props = [
    {"name": "Josh Hart", "open": 23.5, "current": 24.5, "stat": "P+R+A", "prob": 54.2, "status": "🚨 LINE UP"},
    {"name": "Bobby Portis", "open": 16.5, "current": 18.5, "stat": "PTS", "prob": 56.8, "status": "🚨 LINE UP"},
    {"name": "Jaylen Brown", "open": 27.5, "current": 28.5, "stat": "PTS", "prob": 53.1, "status": "🚨 LINE UP"},
    {"name": "Cade Cunningham", "open": 26.5, "current": 26.5, "stat": "PTS", "prob": 51.5, "status": "✅ STABLE"},
    {"name": "Jaden Ivey", "line": 4.5, "stat": "AST", "prob": 52.4, "status": "✅ STABLE"}
]

# 5. SIDEBAR (MOVEMENT REPORT)
with st.sidebar:
    st.header("📉 LINE MOVEMENT")
    for p in baseline_props:
        if "🚨" in p['status']:
            st.write(f"{p['status']}: **{p['name']}** ({p['open']} ➔ {p['current']})")
    
    st.write("---")
    st.markdown("## 🚨 INJURY UPDATES")
    st.error("**GIANNIS (OUT)** | **LUKA (OUT)** | **TATUM (OUT)**")
    st.warning("**JOSH HART (GTD)** | **KAT (GTD)**")

# 6. TABS
tab1, tab2, tab3 = st.tabs(["🎯 THE BOARD", "📡 LINE HISTORY", "🎰 PP BUILDER"])

with tab1:
    for p in baseline_props:
        col1, col2 = st.columns([4, 1])
        with col1:
            st.markdown(f"""
            <div class="prop-card">
                <b>{p['name'].upper()}</b> <span class="move-alert" style="float:right;">{p['status']}</span><br>
                <span>{p['stat']} Line: {p.get('current', p.get('line'))}</span><br>
                <small style="color:#00ff00;">Hit Probability: {p['prob']}%</small>
            </div>
            """, unsafe_allow_html=True)
        with col2: st.code(f"{p['name']} O{p.get('current', p.get('line'))}")
