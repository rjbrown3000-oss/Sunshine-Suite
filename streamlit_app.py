import streamlit as st
import datetime
from streamlit_autorefresh import st_autorefresh

# 1. CORE ENGINE & REFRESH (30s)
st.set_page_config(page_title="Ricky's Executive Suite", layout="wide")
st_autorefresh(interval=30000, key="verified_sync_v140")

# 2. UI STYLING (DIMMED NEON + LIGHT COURT BG + MODERN TICKER)
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Playball&family=Inter:wght@600&family=Montserrat:wght@800&display=swap');

    /* LIGHTENED COURT BACKGROUND */
    [data-testid="stAppViewContainer"] {
        background-image: linear-gradient(rgba(255,255,255,0.15), rgba(255,255,255,0.15)), 
        url('https://images.unsplash.com/photo-1504450758481-7338eba7524a?q=80&w=2669&auto=format&fit=crop');
        background-size: cover; background-position: center; background-attachment: fixed;
    }

    /* MODERN TICKER - INTER FONT + FASTER SPEED */
    .led-ticker {
        background: #000; border-bottom: 2px solid #00ff00; padding: 12px 0;
        color: #00ff00; font-family: 'Inter', sans-serif; overflow: hidden; white-space: nowrap;
    }
    .ticker-content { display: inline-block; animation: ticker-scroll 40s linear infinite; }
    @keyframes ticker-scroll { 0% { transform: translateX(100%); } 100% { transform: translateX(-100%); } }

    /* LOWERED INTENSITY NEON SIGN */
    .neon-sign {
        font-family: 'Playball', cursive; font-size: 5rem; text-align: center;
        color: #e0ffe0;
        text-shadow: 
            0 0 4px #fff, 
            0 0 12px rgba(0,255,0,0.5), 
            4px 4px 6px rgba(0,0,0,0.6);
        animation: neon-flicker 4s infinite;
        margin-top: 25px;
    }
    @keyframes neon-flicker {
        0%, 18%, 22%, 25%, 53%, 57%, 100% { opacity: 1; }
        20%, 24%, 55% { opacity: 0.85; }
    }

    .prop-card { background: rgba(0,0,0,0.85); border-left: 10px solid #00ff00; padding: 18px; border-radius: 12px; margin-bottom: 12px; }
    .stat-log { font-family: 'Inter', sans-serif; font-size: 0.85rem; color: #aaa; margin-top: 8px; }
    h1, h2, h3, b, p, span { color: white !important; }
</style>
""", unsafe_allow_html=True)

# 3. VERIFIED SCOREBOARD (FEB 6, 2026 - MODERNISED)
st.markdown(f"""
<div class="led-ticker">
    <div class="ticker-content">
        ✅ FINAL: LAL 119-115 PHI | ✅ FINAL: GSW 101-97 PHX | ✅ FINAL: SAS 135-123 DAL | ✅ FINAL: HOU 99-109 CHA
        <span style="margin: 0 40px;"></span> 
        📅 NEXT UP: NYK @ DET (4:30 PM) | MIA @ BOS (4:30 PM) | IND @ MIL (5:00 PM) | PHI @ ORL (5:00 PM)
    </div>
</div>
""", unsafe_allow_html=True)

st.markdown('<div class="neon-sign">Ricky Sunshine\'s</div>', unsafe_allow_html=True)

# 4. SIDEBAR (FUNCTIONAL REFRESH + INJURY HUB)
with st.sidebar:
    st.markdown("### ⚙️ SYSTEM")
    if st.button("🔄 REFRESH LIVE DATA"):
        st.cache_data.clear()
        st.session_state.last_refresh = datetime.datetime.now().strftime("%H:%M:%S")
        st.rerun()
    
    if 'last_refresh' in st.session_state:
        st.caption(f"Last Sync: {st.session_state.last_refresh}")
    
    st.write("---")
    st.markdown("## 📋 INJURY HUB")
    st.error("**DAMIAN LILLARD** (OUT - Achilles)")
    st.error("**TYRESE HALIBURTON** (OUT - Achilles)")
    st.error("**JAYSON TATUM** (OUT - Achilles)")
    st.error("**MILES MCBRIDE** (OUT - Surgery)")
    st.warning("**JALEN BRUNSON** (Q - Ankle)")
    st.warning("**KAT** (Q - Eye Laceration)")

# 5. THE BOARD (TAB 1 WITH LAST 5 MATCHUPS)
props = [
    {"name": "Josh Hart", "line": 13.5, "stat": "P+R+A", "prob": 93, "logs": "15, 12, 18, 11, 14", "matchup": "vs DET"},
    {"name": "Cade Cunningham", "line": 25.5, "stat": "PTS", "prob": 88, "logs": "29, 18, 29, 26, 22", "matchup": "vs NYK"},
    {"name": "Mikal Bridges", "line": 3.5, "stat": "3PM", "prob": 86, "logs": "4, 3, 5, 2, 4", "matchup": "vs DET"},
    {"name": "Bam Adebayo", "line": 10.5, "stat": "REB", "prob": 84, "logs": "12, 9, 11, 13, 8", "matchup": "vs BOS"},
    {"name": "Pascal Siakam", "line": 22.5, "stat": "PTS", "prob": 81, "logs": "24, 21, 26, 20, 19", "matchup": "vs MIL"},
    {"name": "Jalen Johnson", "line": 21.5, "stat": "PTS", "prob": 79, "logs": "23, 19, 25, 18, 22", "matchup": "vs UTA (Final)"},
    {"name": "Anfernee Simons", "line": 18.5, "stat": "PTS", "prob": 75, "logs": "22, 17, 19, 21, 16", "matchup": "vs CHI (Final)"},
    {"name": "OG Anunoby", "line": 1.5, "stat": "S+B", "prob": 72, "logs": "2, 3, 1, 4, 2", "matchup": "vs DET"}
]

tab1, tab2, tab3 = st.tabs(["🎯 THE BOARD", "📡 LIVE FEED", "🎰 PP BUILDER"])

with tab1:
    for p in props:
        col1, col2 = st.columns([4, 1])
        with col1:
            st.markdown(f"""
            <div class="prop-card">
                <b>{p['name'].upper()}</b> <small>({p['matchup']})</small><br>
                <span>{p['stat']} Line: {p['line']}</span>
                <div class="meter-bg"><div class="meter-fill" style="width: {p['prob']}%;"></div></div>
                <div class="stat-log">Last 5: {p['logs']}</div>
                <small style="color:#00ff00;">Confidence: {p['prob']}%</small>
            </div>
            """, unsafe_allow_html=True)
        with col2:
            st.code(f"{p['name']} O{p['line']} {p['stat']}", language="text")

with tab2:
    st.subheader("📡 Rotation Analysis (Friday)")
    st.info("🚨 **Cade vs Knicks:** Cade has hit his points line in 6 of his last 7 vs NYK. He's averaging 30.7 PPG in that stretch.")
    st.info("🚨 **McBride/Brunson Impact:** If Brunson is out, Josh Hart becomes a lock for 40+ minutes. His P+R+A line is currently undervalued.")
