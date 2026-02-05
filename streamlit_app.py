import streamlit as st
import datetime
from streamlit_autorefresh import st_autorefresh

# 1. CORE ENGINE
st.set_page_config(page_title="Ricky's Executive Suite", layout="wide")
st_autorefresh(interval=60000, key="restoration_v131")

# 2. THE UI (LOCKED BACKGROUND)
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
        padding: 10px 0; overflow: hidden; display: flex;
    }
    .led-ticker {
        font-family: 'Orbitron', sans-serif; white-space: nowrap;
        color: #00ff00; text-shadow: 0 0 10px #00ff00;
        font-size: 1.1rem; animation: slide 45s linear infinite;
    }
    @keyframes slide { 0% { transform: translateX(100%); } 100% { transform: translateX(-100%); } }

    .ricky-neon {
        font-family: 'Playball', cursive; font-size: 4.8rem; text-align: center;
        color: #fff; text-shadow: 0 0 20px #00ff00; animation: flicker 4s infinite;
    }
    @keyframes flicker { 0%, 18%, 22%, 25%, 53%, 57%, 100% { opacity: 1; } 20%, 24%, 55% { opacity: 0.7; } }

    .prop-card { background: rgba(0,0,0,0.8); border-left: 10px solid #00ff00; padding: 15px; border-radius: 12px; margin-bottom: 15px; }
    .meter-bg { background: rgba(255,255,255,0.1); border-radius: 8px; height: 8px; margin: 5px 0; }
    .meter-fill { background: #00ff00; height: 100%; border-radius: 8px; box-shadow: 0 0 8px #00ff00; }
    
    h1, h2, h3, b, p, span { color: white !important; text-shadow: 2px 2px 10px #000 !important; }
    .tier-label { font-size: 0.8rem; padding: 2px 8px; border-radius: 5px; text-transform: uppercase; font-weight: bold; }
</style>
""", unsafe_allow_html=True)

# 3. SCOREBOARD
st.markdown(f"""
<div class="led-ribbon"><div class="led-ticker">
    🚨 LIVE INTEL: GIANNIS (OUT) | TRAE YOUNG (OUT) | CADE CUNNINGHAM (OUT) | CAM THOMAS (OUT) <span style="margin:0 20px;"></span>
    🏀 7:30 PM: CHI @ TOR | 8:30 PM: SAS @ DAL | 10:00 PM: GSW @ PHX | 10:00 PM: PHI @ LAL
</div></div>
""", unsafe_allow_html=True)

st.markdown('<div class="ricky-neon">Ricky Sunshine\'s</div>', unsafe_allow_html=True)

# 4. SIDEBAR INJURIES
with st.sidebar:
    st.markdown("## 📋 INJURY HUB")
    st.error("**GIANNIS** (OUT) | **TRAE** (OUT)")
    st.error("**CADE** (OUT) | **CAM THOMAS** (OUT)")
    st.warning("**TOBIAS HARRIS** (GTD - Hip)")
    st.write("---")
    night_mode = st.toggle("🌙 Force Nightowl Swap")

# 5. DATA LOAD
props = [
    # HIGH VALUE
    {"name": "Isaiah Collier", "line": 11.5, "stat": "AST", "id": "1642261", "proj": 14.1, "prob": 88, "tier": "High Value", "color": "#00ff00"},
    {"name": "Jalen Johnson", "line": 19.5, "stat": "PTS", "id": "1630552", "proj": 23.4, "prob": 85, "tier": "High Value", "color": "#00ff00"},
    {"name": "Oso Ighodaro", "line": 4.5, "stat": "REB", "id": "1642273", "proj": 6.8, "prob": 82, "tier": "High Value", "color": "#00ff00"},
    # MEDIUM VALUE
    {"name": "Jalen Brunson", "line": 27.5, "stat": "PTS", "id": "1628973", "proj": 30.2, "prob": 79, "tier": "Medium", "color": "#ffaa00"},
    {"name": "Jalen Duren", "line": 11.5, "stat": "REB", "id": "1631105", "proj": 13.2, "prob": 76, "tier": "Medium", "color": "#ffaa00"},
    {"name": "VJ Edgecombe", "line": 13.5, "stat": "PTS", "id": "1642265", "proj": 15.8, "prob": 74, "tier": "Medium", "color": "#ffaa00"},
    # VALUE PROPS
    {"name": "Michael Porter Jr.", "line": 24.5, "stat": "PTS", "id": "1629008", "proj": 26.1, "prob": 68, "tier": "Value", "color": "#00ccff"},
    {"name": "Immanuel Quickley", "line": 5.5, "stat": "REB", "id": "1630193", "proj": 4.7, "prob": 65, "tier": "Value (Under)", "color": "#00ccff"},
    {"name": "Cooper Flagg", "line": 23.5, "stat": "PTS", "id": "1642258", "proj": 20.9, "prob": 63, "tier": "Value (Under)", "color": "#00ccff"},
    {"name": "Marcus Smart", "line": 6.5, "stat": "PTS", "id": "203935", "proj": 8.5, "prob": 61, "tier": "Value", "color": "#00ccff"}
]

tab1, tab2, tab3 = st.tabs(["🎯 THE BOARD", "📡 LIVE FEED", "📈 PARLAY BUILDER"])

with tab1:
    for p in props:
        edge = round(abs(p['proj'] - p['line']), 1)
        col1, col2 = st.columns([4, 1])
        with col1:
            st.markdown(f"""
            <div class="prop-card">
                <div style="display: flex; align-items: center;">
                    <img src="https://cdn.nba.com/headshots/nba/latest/1040x760/{p['id']}.png" style="width:60px; margin-right:15px; border-radius:50%; border:2px solid {p['color']};">
                    <div style="flex-grow:1;">
                        <span class="tier-label" style="background:{p['color']}; color:black;">{p['tier']}</span><br>
                        <b>{p['name'].upper()}</b><br>
                        <span>{p['stat']} Line: {p['line']} | <span style="color:#00ff00;">Proj: {p['proj']}</span></span>
                        <div class="meter-bg"><div class="meter-fill" style="width: {p['prob']}%;"></div></div>
                        <small style="color:#00ff00;">{p['prob']}% Hit Rate | Edge: +{edge}</small>
                    </div>
                </div>
            </div>
            """, unsafe_allow_html=True)
        with col2:
            st.write(" ") # Padding
            st.code(f"{p['name']} O{p['line']} {p['stat']}", language="text")

with tab2:
    st.info("📡 **Live Analytics:** Isaiah Collier (Utah) projected for massive assist volume tonight vs Atlanta's fast pace.")

with tab3:
    st.subheader("📈 System Lock")
    st.code("Collier O11.5 AST + J. Johnson O19.5 PTS + Ighodaro O4.5 REB", language="text")
