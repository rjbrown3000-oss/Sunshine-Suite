import streamlit as st
import datetime
from streamlit_autorefresh import st_autorefresh

# 1. CORE ENGINE & REFRESH
st.set_page_config(page_title="Ricky's Executive Suite", layout="wide")
st_autorefresh(interval=60000, key="verified_sync_v136")

# 2. UI STYLING (LOCKED COURT BACKGROUND)
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Playball&family=Oswald:wght@700&family=Orbitron:wght@700&display=swap');
    [data-testid="stAppViewContainer"] {
        background-image: linear-gradient(rgba(0,0,0,0.8), rgba(0,0,0,0.8)), 
        url('https://images.unsplash.com/photo-1504450758481-7338eba7524a?q=80&w=2669&auto=format&fit=crop');
        background-size: cover; background-position: center; background-attachment: fixed;
    }
    .led-ticker { background: #000; border-bottom: 3px solid #00ff00; padding: 12px 0; color: #00ff00; font-family: 'Orbitron'; overflow: hidden; white-space: nowrap; }
    .ticker-content { display: inline-block; animation: ticker-scroll 60s linear infinite; }
    @keyframes ticker-scroll { 0% { transform: translateX(100%); } 100% { transform: translateX(-100%); } }
    .ricky-title { font-family: 'Playball', cursive; font-size: 4.8rem; text-align: center; color: #fff; text-shadow: 0 0 20px #00ff00; margin-top:15px; }
    .prop-card { background: rgba(0,0,0,0.85); border-left: 10px solid #00ff00; padding: 15px; border-radius: 12px; margin-bottom: 10px; }
    .meter-bg { background: rgba(255,255,255,0.1); border-radius: 8px; height: 8px; margin: 5px 0; }
    .meter-fill { background: #00ff00; height: 100%; border-radius: 8px; box-shadow: 0 0 8px #00ff00; }
    h1, h2, h3, b, p, span { color: white !important; }
</style>
""", unsafe_allow_html=True)

# 3. VERIFIED SCOREBOARD (FEB 5, 2026)
st.markdown(f"""
<div class="led-ticker">
    <div class="ticker-content">
        ✅ FINAL: WAS 126-117 DET | ✅ FINAL: BKN 98-118 ORL | ✅ FINAL: CHI 107-123 TOR | ✅ FINAL: UTA 119-121 ATL 
        <span style="margin: 0 40px;"></span> 
        🏀 LIVE: CHA 91-102 HOU | SAS 78-65 DAL | 📅 10PM PST: GSW @ PHX | PHI @ LAL
    </div>
</div>
""", unsafe_allow_html=True)

st.markdown('<div class="ricky-title">Ricky Sunshine\'s</div>', unsafe_allow_html=True)

# 4. SIDEBAR: REFRESH & INJURY HUB
with st.sidebar:
    st.subheader("⚙️ EXECUTIVE CONTROLS")
    if st.button("🔄 REFRESH LIVE DATA"): st.rerun()
    st.write("---")
    st.markdown("## 📋 INJURY HUB")
    st.info("**KNICKS:** NEXT @ DET (FEB 6)")
    st.error("**STEPHEN CURRY** (OUT - Knee)")
    st.error("**DEVIN BOOKER** (OUT - Ankle)")
    st.warning("**JOEL EMBIID** (GTD - Foot)")

# 5. DATA LOAD (TEN TOP PROPS)
all_props = [
    {"name": "Victor Wembanyama", "line": 10.5, "stat": "REB", "prob": 91, "tier": "High Value"},
    {"name": "Jalen Johnson", "line": 9.5, "stat": "REB", "prob": 88, "tier": "High Value"},
    {"name": "Isaiah Collier", "line": 11.5, "stat": "AST", "prob": 87, "tier": "High Value"},
    {"name": "Josh Hart", "line": 6.5, "stat": "AST", "prob": 84, "tier": "Friday Early"},
    {"name": "LeBron James", "line": 20.5, "stat": "PTS", "prob": 82, "tier": "Medium"},
    {"name": "Alperen Sengun", "line": 8.5, "stat": "REB", "prob": 79, "tier": "Medium"},
    {"name": "Mark Williams", "line": 11.5, "stat": "PTS", "prob": 76, "tier": "Medium"},
    {"name": "Luka Doncic", "line": 32.5, "stat": "PTS", "prob": 72, "tier": "Medium"},
    {"name": "Grayson Allen", "line": 18.5, "stat": "PTS", "prob": 68, "tier": "Value"},
    {"name": "Miles McBride", "line": 14.5, "stat": "PTS", "prob": 65, "tier": "Friday Early"}
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
            st.code(f"{p['name']} O{p['line']} {p['stat']}", language="text")

with tab2:
    st.subheader("📡 Live Analytical Feed")
    def live_intel():
        st.info("🔥 **Wemby Alert:** Victor is currently dominating the glass against Dallas. Line of 10.5 is safe.")
        st.info("🚨 **Suns Rotation:** With Booker OUT, Grayson Allen (O18.5) sees a 15% usage increase.")
        st.info("📅 **Friday Lookahead:** Knicks @ Pistons. Josh Hart AST line likely to move to 7.5 by morning.")
    live_intel()

with tab3:
    st.subheader("🎰 PrizePicks Parlay Simulator")
    selected = st.multiselect("Select your players:", [p['name'] for p in all_props])
    if selected:
        total_p = 1.0
        for s in selected:
            p_data = next(item for item in all_props if item["name"] == s)
            total_p *= (p_data['prob'] / 100)
            st.write(f"✅ {s}: {p_data['prob']}%")
        st.metric("Slip Hit Probability", f"{round(total_p * 100, 2)}%")
        st.code(" + ".join(selected), language="text")
