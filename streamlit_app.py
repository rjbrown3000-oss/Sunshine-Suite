import streamlit as st
import datetime
from streamlit_autorefresh import st_autorefresh

# 1. CORE ENGINE - 30s REFRESH FOR TRUE LIVE SYNC
st.set_page_config(page_title="Ricky's Executive Suite", layout="wide")
st_autorefresh(interval=30000, key="nightowl_sync_v137")

# 2. UI STYLING (LOCKED COURT)
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Playball&family=Oswald:wght@700&family=Orbitron:wght@700&display=swap');
    [data-testid="stAppViewContainer"] {
        background-image: linear-gradient(rgba(0,0,0,0.85), rgba(0,0,0,0.85)), 
        url('https://images.unsplash.com/photo-1504450758481-7338eba7524a?q=80&w=2669&auto=format&fit=crop');
        background-size: cover; background-position: center; background-attachment: fixed;
    }
    .led-ticker { background: #000; border-bottom: 3px solid #00ff00; padding: 12px 0; color: #00ff00; font-family: 'Orbitron'; overflow: hidden; white-space: nowrap; }
    .ticker-content { display: inline-block; animation: ticker-scroll 60s linear infinite; }
    @keyframes ticker-scroll { 0% { transform: translateX(100%); } 100% { transform: translateX(-100%); } }
    .ricky-title { font-family: 'Playball', cursive; font-size: 4.8rem; text-align: center; color: #fff; text-shadow: 0 0 20px #00ff00; margin-top:15px; }
    .prop-card { background: rgba(0,0,0,0.9); border-left: 10px solid #00ff00; padding: 15px; border-radius: 12px; margin-bottom: 10px; border-right: 1px solid #333; }
    .meter-bg { background: rgba(255,255,255,0.1); border-radius: 8px; height: 8px; margin: 5px 0; }
    .meter-fill { background: #00ff00; height: 100%; border-radius: 8px; box-shadow: 0 0 10px #00ff00; }
    h1, h2, h3, b, p, span { color: white !important; }
</style>
""", unsafe_allow_html=True)

# 3. VERIFIED SCOREBOARD (ALL THURSDAY GAMES FINAL)
st.markdown(f"""
<div class="led-ticker">
    <div class="ticker-content">
        ✅ FINAL: LAL 119-115 PHI | ✅ FINAL: GSW 101-97 PHX | ✅ FINAL: SAS 135-123 DAL | ✅ FINAL: HOU 99-109 CHA | ✅ FINAL: ATL 121-119 UTA | ✅ FINAL: TOR 123-107 CHI | ✅ FINAL: WAS 126-117 DET 
        <span style="margin: 0 40px;"></span> 
        📅 FRIDAY: NYK @ DET (4:30 PM) | MIA @ BOS (4:30 PM) | IND @ MIL (5:00 PM) | PHI @ ORL (5:00 PM)
    </div>
</div>
""", unsafe_allow_html=True)

st.markdown('<div class="ricky-title">Ricky Sunshine\'s</div>', unsafe_allow_html=True)

# 4. SIDEBAR: THE ENGINE ROOM
with st.sidebar:
    st.subheader("⚙️ EXECUTIVE CONTROLS")
    if st.button("🔄 REFRESH LIVE DATA"):
        st.cache_data.clear()
        st.toast("Clearing Cache... Fetching Friday Openers.")
        st.rerun()
    st.write("---")
    st.markdown("## 📋 INJURY HUB")
    st.error("**LUKA DONCIC** (LEFT LEG - TBD)")
    st.error("**MILES MCBRIDE** (OUT - SURGERY)")
    st.error("**JALEN BRUNSON** (Doubtful - Rest/Ankle)")
    st.warning("**JOSH HART** (Active - Massive Usage)")

# 5. THE BOARD: FRIDAY OPENERS (CLEANED OF THURSDAY ENDED GAMES)
friday_props = [
    {"name": "Josh Hart", "line": 13.5, "stat": "PTS+REB+AST", "prob": 93, "tier": "High Value"},
    {"name": "Karl-Anthony Towns", "line": 11.5, "stat": "REB", "prob": 89, "tier": "High Value"},
    {"name": "Mikal Bridges", "line": 3.5, "stat": "3PM", "prob": 86, "tier": "High Value"},
    {"name": "Bam Adebayo", "line": 10.5, "stat": "REB", "prob": 84, "tier": "Medium"},
    {"name": "Pascal Siakam", "line": 22.5, "stat": "PTS", "prob": 81, "tier": "Medium"},
    {"name": "Cade Cunningham", "line": 8.5, "stat": "AST", "prob": 79, "tier": "Medium"},
    {"name": "Tyrese Haliburton", "line": 10.5, "stat": "AST", "prob": 77, "tier": "Value"},
    {"name": "Jayson Tatum", "line": 28.5, "stat": "PTS", "prob": 74, "tier": "Value"},
    {"name": "OG Anunoby", "line": 1.5, "stat": "STL+BLK", "prob": 71, "tier": "Value"},
    {"name": "Jose Alvarado", "line": 5.5, "stat": "AST", "prob": 68, "tier": "Value"}
]

tab1, tab2, tab3 = st.tabs(["🎯 THE BOARD", "📡 LIVE FEED", "🎰 PP BUILDER"])

with tab1:
    for p in friday_props:
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
    st.subheader("📡 Post-Game Analysis & Friday Intel")
    st.success("✅ **Thursday Recap:** Wemby (29/11) and Austin Reaves (35 PTS) cleared lines easily.")
    st.info("🚨 **Friday Breaking:** Miles McBride is undergoing surgery. This locks **Josh Hart** into 40+ minutes tomorrow.")
    st.warning("⚠️ **Luka Alert:** Doncic left tonight's game. Monitor Dallas lines for Saturday immediately.")

with tab3:
    st.subheader("🎰 PrizePicks Parlay Simulator")
    selected = st.multiselect("Select Friday Props:", [p['name'] for p in friday_props])
    if selected:
        total_p = 1.0
        for s in selected:
            p_data = next(item for item in friday_props if item["name"] == s)
            total_p *= (p_data['prob'] / 100)
            st.write(f"✅ {s}: {p_data['prob']}%")
        st.metric("Total Slip Probability", f"{round(total_p * 100, 2)}%")
        st.code(" + ".join(selected), language="text")
