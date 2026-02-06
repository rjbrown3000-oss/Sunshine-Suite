import streamlit as st
from streamlit_autorefresh import st_autorefresh

# 1. CORE ENGINE
st.set_page_config(page_title="Ricky's Executive Suite", layout="wide")
st_autorefresh(interval=60000, key="verified_sync_v135")

# 2. UI STYLING (LOCKED BACKGROUND)
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Playball&family=Oswald:wght@700&family=Orbitron:wght@700&display=swap');
    [data-testid="stAppViewContainer"] {
        background-image: linear-gradient(rgba(0,0,0,0.75), rgba(0,0,0,0.75)), 
        url('https://images.unsplash.com/photo-1504450758481-7338eba7524a?q=80&w=2669&auto=format&fit=crop');
        background-size: cover; background-position: center; background-attachment: fixed;
    }
    .led-ticker { background: #000; border-bottom: 3px solid #00ff00; padding: 12px 0; color: #00ff00; font-family: 'Orbitron'; overflow: hidden; white-space: nowrap; }
    .ticker-content { display: inline-block; animation: ticker-scroll 55s linear infinite; }
    @keyframes ticker-scroll { 0% { transform: translateX(100%); } 100% { transform: translateX(-100%); } }
    .ricky-title { font-family: 'Playball', cursive; font-size: 4.8rem; text-align: center; color: #fff; text-shadow: 0 0 20px #00ff00; margin-top:15px; }
    .prop-card { background: rgba(0,0,0,0.85); border-left: 10px solid #00ff00; padding: 15px; border-radius: 12px; margin-bottom: 10px; }
</style>
""", unsafe_allow_html=True)

# 3. VERIFIED SCOREBOARD
st.markdown(f"""
<div class="led-ticker">
    <div class="ticker-content">
        ✅ FINAL: WAS 126-117 DET | ✅ FINAL: BKN 98-118 ORL | ✅ FINAL: CHI 107-123 TOR | ✅ FINAL: UTA 119-121 ATL 
        <span style="margin: 0 40px;"></span> 
        🔥 LIVE: CHA 91-102 HOU | SAS 78-65 DAL | 📅 10PM PST: GSW @ PHX | PHI @ LAL
    </div>
</div>
""", unsafe_allow_html=True)

st.markdown('<div class="ricky-title">Ricky Sunshine\'s</div>', unsafe_allow_html=True)

# 4. SIDEBAR: REFRESH & INJURY HUB
with st.sidebar:
    st.subheader("⚙️ EXECUTIVE CONTROLS")
    if st.button("🔄 REFRESH LIVE DATA"):
        st.rerun()
    st.write("---")
    st.markdown("## 📋 INJURY HUB")
    st.info("**KNICKS:** NEXT GAME FEB 6 @ DET")
    st.error("**JALEN DUREN** (OUT - Left Knee)")
    st.error("**TRAE YOUNG** (OUT)")
    st.warning("**CADE CUNNINGHAM** (30 PTS TONIGHT)")

# 5. TABS & PROPS
tab1, tab2, tab3 = st.tabs(["🎯 THE BOARD", "📡 LIVE FEED", "🎰 PP BUILDER"])

with tab1:
    st.subheader("🌙 Friday Early Value (Knicks @ Pistons)")
    early_props = [
        {"name": "Josh Hart", "line": 6.5, "stat": "AST", "prob": 88, "tier": "High Value", "id": "1628404"},
        {"name": "Miles McBride", "line": 14.5, "stat": "PTS", "prob": 85, "tier": "High Value", "id": "1630540"}
    ]
    for p in early_props:
        col1, col2 = st.columns([4, 1])
        with col1:
            st.markdown(f"""<div class="prop-card"><b>{p['name'].upper()}</b><br><span>{p['stat']} Line: {p['line']}</span><br><small style="color:#00ff00;">Hit Rate: {p['prob']}%</small></div>""", unsafe_allow_html=True)
        with col2:
            st.code(f"{p['name']} O{p['line']} {p['stat']}", language="text")
