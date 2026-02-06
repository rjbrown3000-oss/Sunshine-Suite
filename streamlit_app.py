import streamlit as st
from streamlit_autorefresh import st_autorefresh

# 1. CORE ENGINE
st.set_page_config(page_title="Ricky's Executive Suite", layout="wide")
st_autorefresh(interval=30000, key="neon_refreshed_v139")

# 2. UI STYLING (LIGHTENED BG + NEON SIGN + MODERN TICKER)
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Playball&family=Inter:wght@700&family=Montserrat:wght@800&display=swap');

    /* LIGHTENED BACKGROUND OVERLAY */
    [data-testid="stAppViewContainer"] {
        background-image: linear-gradient(rgba(0,0,0,0.4), rgba(0,0,0,0.4)), 
        url('https://images.unsplash.com/photo-1504450758481-7338eba7524a?q=80&w=2669&auto=format&fit=crop');
        background-size: cover; background-position: center; background-attachment: fixed;
    }

    /* MODERN TICKER - INTER FONT + FASTER RESPONSE */
    .led-ticker {
        background: #000; border-bottom: 3px solid #00ff00; padding: 10px 0;
        color: #00ff00; font-family: 'Inter', sans-serif; overflow: hidden; white-space: nowrap;
        cursor: pointer; transition: opacity 0.1s;
    }
    .led-ticker:active { opacity: 0.7; transform: scale(0.99); }
    .ticker-content { display: inline-block; animation: ticker-scroll 45s linear infinite; }
    @keyframes ticker-scroll { 0% { transform: translateX(100%); } 100% { transform: translateX(-100%); } }

    /* RICKY'S NEON SIGN WITH DROP SHADOWS */
    .neon-sign {
        font-family: 'Playball', cursive; font-size: 5rem; text-align: center;
        color: #fff;
        text-shadow: 
            0 0 5px #fff, 0 0 10px #fff, 
            0 0 20px #00ff00, 0 0 30px #00ff00, 
            0 0 40px #00ff00, 4px 4px 8px rgba(0,0,0,0.8);
        animation: neon-flicker 3s infinite;
        margin-top: 20px;
    }
    @keyframes neon-flicker {
        0%, 19%, 21%, 23%, 25%, 54%, 56%, 100% { opacity: 1; }
        20%, 22%, 24%, 55% { opacity: 0.8; }
    }

    .prop-card { background: rgba(0,0,0,0.8); border-left: 10px solid #00ff00; padding: 15px; border-radius: 12px; margin-bottom: 10px; }
    .meter-bg { background: rgba(255,255,255,0.1); border-radius: 8px; height: 8px; margin: 5px 0; }
    .meter-fill { background: #00ff00; height: 100%; border-radius: 8px; box-shadow: 0 0 10px #00ff00; }
    h1, h2, h3, b, p, span { color: white !important; }
</style>
""", unsafe_allow_html=True)

# 3. SCOREBOARD (MODERN FONT)
st.markdown(f"""
<div class="led-ticker">
    <div class="ticker-content">
        ✅ FINAL: LAL 119-115 PHI | ✅ FINAL: GSW 101-97 PHX | ✅ FINAL: SAS 135-123 DAL | ✅ FINAL: HOU 99-109 CHA 
        <span style="margin: 0 40px;"></span> 
        📅 NEXT: NYK @ DET (4:30 PM) | MIA @ BOS (4:30 PM) | IND @ MIL (5:00 PM)
    </div>
</div>
""", unsafe_allow_html=True)

st.markdown('<div class="neon-sign">Ricky Sunshine\'s</div>', unsafe_allow_html=True)

# 4. SIDEBAR (INJURY LIST & REFRESH)
with st.sidebar:
    if st.button("🔄 REFRESH LIVE DATA"):
        st.cache_data.clear()
        st.rerun()
    st.write("---")
    st.markdown("## 📋 INJURY HUB")
    st.error("**TYRESE HALIBURTON** (OUT - Hamstring)")
    st.error("**JAYSON TATUM** (OUT - Knee)")
    st.error("**MILES MCBRIDE** (OUT - Surgery)")
    st.warning("**JALEN BRUNSON** (Q - Ankle)")

# 5. DATA LOAD (INJURY-FREE BOARD)
props = [
    {"name": "Josh Hart", "line": 13.5, "stat": "P+R+A", "prob": 93, "tier": "High Value"},
    {"name": "Karl-Anthony Towns", "line": 11.5, "stat": "REB", "prob": 89, "tier": "High Value"},
    {"name": "Mikal Bridges", "line": 3.5, "stat": "3PM", "prob": 86, "tier": "High Value"},
    {"name": "Cade Cunningham", "line": 8.5, "stat": "AST", "prob": 82, "tier": "Medium"},
    {"name": "Bam Adebayo", "line": 10.5, "stat": "REB", "prob": 80, "tier": "Medium"},
    {"name": "Damian Lillard", "line": 26.5, "stat": "PTS", "prob": 78, "tier": "Medium"},
    {"name": "Anfernee Simons", "line": 4.5, "stat": "AST", "prob": 75, "tier": "Value"},
    {"name": "OG Anunoby", "line": 1.5, "stat": "S+B", "prob": 72, "tier": "Value"}
]

tab1, tab2, tab3 = st.tabs(["🎯 THE BOARD", "📡 LIVE FEED", "🎰 PP BUILDER"])

with tab1:
    for p in props:
        col1, col2 = st.columns([4, 1])
        with col1:
            st.markdown(f"""<div class="prop-card"><b>{p['name'].upper()}</b> ({p['tier']})<br><span>{p['stat']} Line: {p['line']}</span><div class="meter-bg"><div class="meter-fill" style="width: {p['prob']}%;"></div></div><small style="color:#00ff00;">Hit Rate: {p['prob']}%</small></div>""", unsafe_allow_html=True)
        with col2:
            st.code(f"{p['name']} O{p['line']} {p['stat']}", language="text")

with tab2:
    st.subheader("📡 Rotation Analysis")
    st.info("🚨 **BOS Update:** With Tatum OUT, expect Jaylen Brown and Derrick White usage to spike to 35% and 24% respectively.")
    st.info("🚨 **IND Update:** Haliburton's absence puts the ball entirely in Siakam's hands for playmaking.")

with tab3:
    selected = st.multiselect("Build Your Slip:", [p['name'] for p in props])
    if selected:
        prob = 100
        for s in selected:
            p_data = next(item for item in props if item["name"] == s)
            prob *= (p_data['prob'] / 100)
        st.metric("Slip Probability", f"{round(prob, 2)}%")
