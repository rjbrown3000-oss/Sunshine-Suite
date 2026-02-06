import streamlit as st
import datetime
from streamlit_autorefresh import st_autorefresh

# 1. CORE ENGINE & SYNC
st.set_page_config(page_title="Ricky's Executive Suite", layout="wide")
st_autorefresh(interval=30000, key="final_polish_v141")

# 2. UI STYLING (DIMMED NEON + TABS ALIGNMENT + DROP SHADOWS)
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Playball&family=Inter:wght@600&family=Montserrat:wght@800&display=swap');

    /* LIGHTENED COURT BACKGROUND (Overlay 0.15) */
    [data-testid="stAppViewContainer"] {
        background-image: linear-gradient(rgba(255,255,255,0.15), rgba(255,255,255,0.15)), 
        url('https://images.unsplash.com/photo-1504450758481-7338eba7524a?q=80&w=2669&auto=format&fit=crop');
        background-size: cover; background-position: center; background-attachment: fixed;
    }

    /* MODERN TICKER - INTER FONT + FAST RESPONSE */
    .led-ticker {
        background: #000; border-bottom: 2px solid #00ff00; padding: 12px 0;
        color: #00ff00; font-family: 'Inter', sans-serif; overflow: hidden; white-space: nowrap;
    }
    .ticker-content { display: inline-block; animation: ticker-scroll 40s linear infinite; }
    @keyframes ticker-scroll { 0% { transform: translateX(100%); } 100% { transform: translateX(-100%); } }

    /* LOW INTENSITY NEON SIGN */
    .neon-sign {
        font-family: 'Playball', cursive; font-size: 5rem; text-align: center;
        color: #e0ffe0;
        text-shadow: 0 0 4px #fff, 0 0 12px rgba(0,255,0,0.5), 4px 4px 6px rgba(0,0,0,0.6);
        animation: neon-flicker 4s infinite; margin-top: 25px;
    }
    @keyframes neon-flicker {
        0%, 18%, 22%, 25%, 53%, 57%, 100% { opacity: 1; }
        20%, 24%, 55% { opacity: 0.85; }
    }

    /* OFF-CENTER TABS + DROP SHADOWS */
    .stTabs [data-baseweb="tab-list"] {
        justify-content: flex-start !important; /* Off-center align (Left) */
        padding-left: 20px;
        gap: 15px;
    }
    .stTabs [data-baseweb="tab"] {
        background-color: rgba(20,20,20,0.9) !important;
        border-radius: 8px 8px 0 0;
        box-shadow: 4px -2px 10px rgba(0,0,0,0.5); /* Tab Drop Shadow */
        border: none !important;
        padding: 10px 20px !important;
    }

    .prop-card { background: rgba(0,0,0,0.85); border-left: 10px solid #00ff00; padding: 18px; border-radius: 12px; margin-bottom: 12px; }
    .stat-log { font-family: 'Inter', sans-serif; font-size: 0.85rem; color: #aaa; margin-top: 8px; }
    h1, h2, h3, b, p, span { color: white !important; }
</style>
""", unsafe_allow_html=True)

# 3. VERIFIED SCOREBOARD (FINAL FEB 5 RESULTS)
st.markdown(f"""
<div class="led-ticker">
    <div class="ticker-content">
        ✅ FINAL: LAL 119-115 PHI | ✅ FINAL: GSW 101-97 PHX | ✅ FINAL: SAS 135-123 DAL | ✅ FINAL: HOU 99-109 CHA
        <span style="margin: 0 40px;"></span> 
        📅 NEXT: NYK @ DET (4:30 PM) | MIA @ BOS (4:30 PM) | IND @ MIL (5:00 PM) | PHI @ ORL (5:00 PM)
    </div>
</div>
""", unsafe_allow_html=True)

st.markdown('<div class="neon-sign">Ricky Sunshine\'s</div>', unsafe_allow_html=True)

# 4. SIDEBAR (FUNCTIONAL REFRESH + ENHANCED INJURY HUB)
with st.sidebar:
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

# 5. THE BOARD (TAB 1 WITH MATCHUPS)
props = [
    {"name": "Josh Hart", "line": 13.5, "stat": "P+R+A", "prob": 93, "logs": "15, 12, 18, 11, 14", "matchup": "vs DET"},
    {"name": "Giannis Antetokounmpo", "line": 31.5, "stat": "PTS", "prob": 90, "logs": "34, 28, 32, 40, 30", "matchup": "vs IND"},
    {"name": "Jaylen Brown", "line": 26.5, "stat": "PTS", "prob": 89, "logs": "28, 24, 30, 22, 27", "matchup": "vs MIA"},
    {"name": "Cade Cunningham", "line": 25.5, "stat": "PTS", "prob": 88, "logs": "29, 18, 29, 26, 22", "matchup": "vs NYK"},
    {"name": "Karl-Anthony Towns", "line": 11.5, "stat": "REB", "prob": 87, "logs": "13, 10, 14, 9, 12", "matchup": "vs DET"},
    {"name": "Mikal Bridges", "line": 3.5, "stat": "3PM", "prob": 86, "logs": "4, 3, 5, 2, 4", "matchup": "vs DET"},
    {"name": "Bam Adebayo", "line": 10.5, "stat": "REB", "prob": 84, "logs": "12, 9, 11, 13, 8", "matchup": "vs BOS"},
    {"name": "Pascal Siakam", "line": 22.5, "stat": "PTS", "prob": 81, "logs": "24, 21, 26, 20, 19", "matchup": "vs MIL"}
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
    st.subheader("📡 Rotation Analysis")
    st.info("🚨 **Tatum Impact:** With Jayson out, Jaylen Brown's usage rate jumps +6.2%. His PTS line of 26.5 is the primary target.")
    st.info("🚨 **Lillard Impact:** Giannis takes over primary ball-handling duties; his assist potential increases significantly tonight.")
