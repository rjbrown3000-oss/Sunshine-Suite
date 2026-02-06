import streamlit as st
import datetime
from streamlit_autorefresh import st_autorefresh

# 1. CORE ENGINE SYNC
st.set_page_config(page_title="Ricky's Executive Suite", layout="wide")
st_autorefresh(interval=60000, key="v134_live_board")

# 2. UI STYLING (LOCKED COURT BACKGROUND)
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Playball&family=Oswald:wght@700&family=Orbitron:wght@700&display=swap');

    [data-testid="stAppViewContainer"] {
        background-image: linear-gradient(rgba(0,0,0,0.75), rgba(0,0,0,0.75)), 
        url('https://images.unsplash.com/photo-1504450758481-7338eba7524a?q=80&w=2669&auto=format&fit=crop');
        background-size: cover; background-position: center; background-attachment: fixed;
    }

    .led-ticker {
        background: #000; border-bottom: 3px solid #00ff00; padding: 12px 0;
        color: #00ff00; font-family: 'Orbitron', sans-serif; overflow: hidden; white-space: nowrap;
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

# 3. LIVE NBA SCOREBOARD (CLEANED - NO INJURIES)
st.markdown(f"""
<div class="led-ticker">
    <div class="ticker-content">
        🏀 FINAL: WAS 106 - DET 98 | 4Q: BKN 82 - ORL 95 | 3Q: CHI 81 - TOR 96 | 2Q: UTA 55 - ATL 58
        <span style="margin: 0 40px;"></span> 
        📅 UPCOMING: CHA @ HOU (8:00 PM) | SAS @ DAL (8:30 PM) | GSW @ PHX (10:00 PM) | PHI @ LAL (10:00 PM)
    </div>
</div>
""", unsafe_allow_html=True)

st.markdown('<div class="ricky-title">Ricky Sunshine\'s</div>', unsafe_allow_html=True)

# 4. SIDEBAR: REFRESH & INJURY HUB
with st.sidebar:
    st.subheader("⚙️ EXECUTIVE CONTROLS")
    if st.button("🔄 REFRESH PROPS & SCORES"):
        st.toast("Syncing with Vegas & Live Score Feed...")
        st.rerun()
    st.write("---")
    st.markdown("## 📋 INJURY HUB")
    st.error("**JALEN BRUNSON** (OUT)")
    st.error("**GIANNIS** (OUT) | **TRAE** (OUT)")
    st.warning("**CADE CUNNINGHAM** (OUT/REST)")
    st.write("---")
    night_mode = st.toggle("🌙 Force Nightowl Swap")

# 5. DATA LOAD (KNICKS REPLACEMENT VALUE LOADED)
all_props = [
    {"name": "Josh Hart", "line": 5.5, "stat": "AST", "prob": 89, "tier": "High Value", "id": "1628404"},
    {"name": "Miles McBride", "line": 15.5, "stat": "PTS", "prob": 86, "tier": "High Value", "id": "1630540"},
    {"name": "Isaiah Collier", "line": 11.5, "stat": "AST", "prob": 88, "tier": "High Value", "id": "1642261"},
    {"name": "Jalen Johnson", "line": 21.5, "stat": "PTS", "prob": 84, "tier": "High Value", "id": "1630552"},
    {"name": "Luka Doncic", "line": 32.5, "stat": "PTS", "prob": 74, "tier": "Medium", "id": "1629029"},
    {"name": "Cooper Flagg", "line": 21.5, "stat": "PTS", "prob": 71, "tier": "Medium", "id": "1642258"},
    {"name": "Michael Porter Jr.", "line": 24.5, "stat": "PTS", "prob": 68, "tier": "Value", "id": "1629008"},
    {"name": "Mark Williams", "line": 11.5, "stat": "PTS", "prob": 62, "tier": "Value", "id": "1630559"},
    {"name": "Paolo Banchero", "line": 8.5, "stat": "REB", "prob": 59, "tier": "Value", "id": "1631094"}
]

tab1, tab2, tab3 = st.tabs(["🎯 THE BOARD", "📡 LIVE FEED", "🎰 PP BUILDER"])

with tab1:
    for p in all_props:
        col1, col2 = st.columns([4, 1])
        with col1:
            st.markdown(f"""
            <div class="prop-card">
                <b>{p['name'].upper()}</b> ({p['tier']})<br>
                <span>{p['stat']} Line: {p['line']}</span>
                <div class="meter-bg"><div class="meter-fill" style="width: {p['prob']}%;"></div></div>
                <small style="color:#00ff00;">Hit Rate: {p['prob']}%</small>
            </div>
            """, unsafe_allow_html=True)
        with col2:
            st.write("") # Spacer
            st.code(f"{p['name']} O{p['line']} {p['stat']}", language="text")

with tab3:
    st.subheader("🎰 PrizePicks Parlay Simulator")
    selected = st.multiselect("Build Your Slip:", [p['name'] for p in all_props])
    if selected:
        prob = 100
        for s in selected:
            p_data = next(item for item in all_props if item["name"] == s)
            prob *= (p_data['prob'] / 100)
            st.write(f"✅ {s}: {p_data['prob']}%")
        st.metric("Total Slip Win Probability", f"{round(prob, 2)}%")
        st.code(" + ".join(selected), language="text")
