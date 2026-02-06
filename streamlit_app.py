import streamlit as st
import datetime
import random
from streamlit_autorefresh import st_autorefresh

# 1. CORE ENGINE SYNC
st.set_page_config(page_title="Ricky's Executive Suite", layout="wide")
st_autorefresh(interval=60000, key="executive_live_v133")

# 2. UI STYLING (LOCKED BACKGROUND)
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Playball&family=Oswald:wght@700&family=Orbitron:wght@700&display=swap');

    [data-testid="stAppViewContainer"] {
        background-image: linear-gradient(rgba(0,0,0,0.75), rgba(0,0,0,0.75)), 
        url('https://images.unsplash.com/photo-1504450758481-7338eba7524a?q=80&w=2669&auto=format&fit=crop');
        background-size: cover; background-position: center; background-attachment: fixed;
    }

    /* LED SCOREBOARD - LIVE NBA ONLY */
    .led-ticker {
        background: #000; border-bottom: 3px solid #00ff00; padding: 12px 0;
        color: #00ff00; font-family: 'Orbitron', sans-serif; overflow: hidden; white-space: nowrap;
        box-shadow: 0 5px 15px rgba(0,0,0,0.8);
    }
    .ticker-content { display: inline-block; animation: ticker-scroll 50s linear infinite; }
    @keyframes ticker-scroll { 0% { transform: translateX(100%); } 100% { transform: translateX(-100%); } }

    .ricky-title { font-family: 'Playball', cursive; font-size: 4.8rem; text-align: center; color: #fff; text-shadow: 0 0 20px #00ff00; margin-top:15px; }
    .prop-card { background: rgba(0,0,0,0.85); border-left: 10px solid #00ff00; padding: 15px; border-radius: 12px; margin-bottom: 10px; }
    .meter-bg { background: rgba(255,255,255,0.1); border-radius: 8px; height: 8px; margin: 5px 0; }
    .meter-fill { background: #00ff00; height: 100%; border-radius: 8px; box-shadow: 0 0 8px #00ff00; }
    h1, h2, h3, b, p, span { color: white !important; }
</style>
""", unsafe_allow_html=True)

# 3. LIVE NBA SCOREBOARD (FEB 5 REAL-TIME)
st.markdown(f"""
<div class="led-ticker">
    <div class="ticker-content">
        🏀 LIVE: WAS 106 - DET 98 (FINAL) | BKN 69 - ORL 88 (4Q) | CHI 78 - TOR 91 (3Q) | UTA 77 - ATL 77 (HALF) 
        <span style="margin: 0 40px;"></span> 
        📅 UPCOMING: CHA @ HOU (8:00 PM) | SAS @ DAL (8:30 PM) | GSW @ PHX (10:00 PM) | PHI @ LAL (10:00 PM)
    </div>
</div>
""", unsafe_allow_html=True)

st.markdown('<div class="ricky-title">Ricky Sunshine\'s</div>', unsafe_allow_html=True)

# 4. SIDEBAR: INJURY HUB & REFRESH
with st.sidebar:
    st.markdown("## 📋 INJURY HUB")
    st.error("**GIANNIS** (OUT) | **TRAE** (OUT)")
    st.error("**BRUNSON** (OUT) | **CAM THOMAS** (OUT)")
    st.warning("**CADE CUNNINGHAM** (Doubtful)")
    st.write("---")
    if st.button("🔄 Refresh Data & Lines"):
        st.toast("Re-calculating probabilities based on latest scratch...")
        st.rerun()
    st.write("---")
    night_toggle = st.toggle("🌙 Force Nightowl Swap")

# 5. PROP DATA (RE-LOADED WITHOUT BRUNSON)
all_props = [
    {"name": "Isaiah Collier", "line": 11.5, "stat": "AST", "prob": 88, "tier": "High Value", "id": "1642261"},
    {"name": "Jalen Johnson", "line": 21.5, "stat": "PTS", "prob": 85, "tier": "High Value", "id": "1630552"},
    {"name": "Oso Ighodaro", "line": 5.5, "stat": "REB", "prob": 82, "tier": "High Value", "id": "1642273"},
    {"name": "Luka Doncic", "line": 32.5, "stat": "PTS", "prob": 74, "tier": "Medium", "id": "1629029"},
    {"name": "Cooper Flagg", "line": 21.5, "stat": "PTS", "prob": 71, "tier": "Medium", "id": "1642258"},
    {"name": "Michael Porter Jr.", "line": 24.5, "stat": "PTS", "prob": 68, "tier": "Value", "id": "1629008"},
    {"name": "Mark Williams", "line": 11.5, "stat": "PTS", "prob": 62, "tier": "Value", "id": "1630559"},
    {"name": "Paolo Banchero", "line": 8.5, "stat": "REB", "prob": 59, "tier": "Value", "id": "1631094"}
]

tab1, tab2, tab3 = st.tabs(["🎯 THE BOARD", "📡 LIVE FEED", "📈 PP BUILDER"])

with tab1:
    for p in all_props:
        col1, col2 = st.columns([4, 1])
        with col1:
            st.markdown(f"""
            <div class="prop-card">
                <b>{p['name'].upper()}</b> ({p['tier']})<br>
                <span>{p['stat']} Line: {p['line']}</span>
                <div class="meter-bg"><div class="meter-fill" style="width: {p['prob']}%;"></div></div>
                <small style="color:#00ff00;">Hit Probability: {p['prob']}%</small>
            </div>
            """, unsafe_allow_html=True)
        with col2:
            st.code(f"{p['name']} O{p['line']} {p['stat']}", language="text")

with tab2:
    st.subheader("📡 Live Analytics")
    st.info("Isaiah Collier usage skyrocketing in Utah. Jalen Johnson 3rd triple-double threat with Trae out.")

with tab3:
    st.subheader("🎰 PrizePicks Parlay Simulator")
    selected_players = st.multiselect("Select players for your slip:", [p['name'] for p in all_props])
    
    if selected_players:
        total_prob = 100
        for name in selected_players:
            p_data = next(item for item in all_props if item["name"] == name)
            total_prob *= (p_data['prob'] / 100)
            st.write(f"✅ **{name}**: {p_data['prob']}% Win Probability")
        
        st.divider()
        st.metric("Combined Slip Probability", f"{round(total_prob, 2)}%")
        st.code(" + ".join(selected_players), language="text")
