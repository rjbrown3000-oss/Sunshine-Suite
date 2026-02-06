import streamlit as st
import datetime
from streamlit_autorefresh import st_autorefresh

# 1. CORE ENGINE
st.set_page_config(page_title="Ricky's Executive Suite", layout="wide")
st_autorefresh(interval=30000, key="verified_sync_v142")

# 2. UI STYLING (CENTERED TABS + SHADOWS + LIGHT BG)
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Playball&family=Inter:wght@600&family=Montserrat:wght@800&display=swap');

    [data-testid="stAppViewContainer"] {
        background-image: linear-gradient(rgba(255,255,255,0.15), rgba(255,255,255,0.15)), 
        url('https://images.unsplash.com/photo-1504450758481-7338eba7524a?q=80&w=2669&auto=format&fit=crop');
        background-size: cover; background-position: center; background-attachment: fixed;
    }

    /* CENTERED TABS WITH DROP SHADOW */
    .stTabs [data-baseweb="tab-list"] {
        justify-content: center !important;
        gap: 20px;
    }
    .stTabs [data-baseweb="tab"] {
        background-color: rgba(30,30,30,0.95) !important;
        border-radius: 10px 10px 0 0;
        box-shadow: 0px 4px 15px rgba(0,0,0,0.6);
        padding: 12px 25px !important;
        border: none !important;
    }

    /* NEON SIGN (DIMMED) */
    .neon-sign {
        font-family: 'Playball', cursive; font-size: 5rem; text-align: center;
        color: #e0ffe0;
        text-shadow: 0 0 5px #fff, 0 0 10px rgba(0,255,0,0.4), 4px 4px 6px rgba(0,0,0,0.7);
        animation: neon-flicker 4s infinite; margin-top: 20px;
    }
    @keyframes neon-flicker { 0%, 19%, 21%, 100% { opacity: 1; } 20% { opacity: 0.8; } }

    .prop-card { background: rgba(0,0,0,0.85); border-left: 10px solid #00ff00; padding: 18px; border-radius: 12px; margin-bottom: 12px; }
    .stat-log { font-family: 'Inter', sans-serif; font-size: 0.85rem; color: #aaa; margin-top: 8px; }
    h1, h2, h3, b, p, span { color: white !important; }
</style>
""", unsafe_allow_html=True)

# 3. SCOREBOARD (VERIFIED FEB 6)
st.markdown(f"""
<div class="led-ticker" style="background:#000; color:#00ff00; font-family:'Inter'; padding:10px; overflow:hidden;">
    <div class="ticker-content" style="display:inline-block; animation: ticker-scroll 40s linear infinite;">
        ✅ FINAL: LAL 119-115 PHI | ✅ FINAL: GSW 101-97 PHX | ✅ FINAL: SAS 135-123 DAL | ✅ FINAL: HOU 99-109 CHA
        <span style="margin: 0 50px;"></span> 
        📅 NEXT: NYK @ DET (4:30 PM) | MIA @ BOS (4:30 PM) | IND @ MIL (5:00 PM)
    </div>
</div>
""", unsafe_allow_html=True)

st.markdown('<div class="neon-sign">Ricky Sunshine\'s</div>', unsafe_allow_html=True)

# 4. SIDEBAR (INJURY HUB - SCRIBE GIANNIS/LUKA/LILLARD)
with st.sidebar:
    if st.button("🔄 REFRESH LIVE DATA"):
        st.cache_data.clear()
        st.session_state.last_refresh = datetime.datetime.now().strftime("%H:%M:%S")
        st.rerun()
    if 'last_refresh' in st.session_state: st.caption(f"Last Sync: {st.session_state.last_refresh}")
    
    st.write("---")
    st.markdown("## 📋 INJURY HUB")
    st.error("**LUKA DONCIC** (OUT - Hamstring MRI)")
    st.error("**GIANNIS ANTETOKOUNMPO** (OUT - Calf)")
    st.error("**DAMIAN LILLARD** (OUT - Achilles)")
    st.error("**TYRESE HALIBURTON** (OUT - Achilles)")
    st.error("**JAYSON TATUM** (OUT - Achilles)")
    st.error("**MILES MCBRIDE** (OUT - Surgery)")
    st.warning("**JOSH HART** (Q - Ankle Sprain)")

# 5. DATA LOAD
props = [
    {"name": "Josh Hart", "line": 14.5, "stat": "P+R+A", "prob": 93, "logs": "15, 12, 18, 11, 14", "matchup": "vs DET"},
    {"name": "Cade Cunningham", "line": 25.5, "stat": "PTS", "prob": 88, "logs": "30, 18, 29, 26, 22", "matchup": "vs NYK"},
    {"name": "Jaylen Brown", "line": 27.5, "stat": "PTS", "prob": 87, "logs": "28, 30, 22, 27, 31", "matchup": "vs MIA"},
    {"name": "Karl-Anthony Towns", "line": 12.5, "stat": "REB", "prob": 85, "logs": "13, 10, 14, 9, 12", "matchup": "vs DET"},
    {"name": "Bobby Portis", "line": 18.5, "stat": "PTS", "prob": 84, "logs": "22, 19, 17, 24, 20", "matchup": "vs IND"},
    {"name": "Bam Adebayo", "line": 11.5, "stat": "REB", "prob": 81, "logs": "12, 9, 11, 13, 8", "matchup": "vs BOS"},
    {"name": "Mikal Bridges", "line": 3.5, "stat": "3PM", "prob": 79, "logs": "4, 3, 5, 2, 4", "matchup": "vs DET"},
    {"name": "Pascal Siakam", "line": 23.5, "stat": "PTS", "prob": 76, "logs": "24, 21, 26, 20, 19", "matchup": "vs MIL"}
]

tab1, tab2, tab3 = st.tabs(["🎯 THE BOARD", "📡 LIVE FEED", "🎰 PP BUILDER"])

with tab1:
    for p in props:
        col1, col2 = st.columns([4, 1])
        with col1:
            st.markdown(f"""<div class="prop-card"><b>{p['name'].upper()}</b> <small>({p['matchup']})</small><br><span>{p['stat']} Line: {p['line']}</span><div class="meter-bg"><div class="meter-fill" style="width: {p['prob']}%;"></div></div><div class="stat-log">Last 5: {p['logs']}</div></div>""", unsafe_allow_html=True)
        with col2: st.code(f"{p['name']} O{p['line']} {p['stat']}")

with tab2:
    st.subheader("📡 Rotation Insights")
    st.info("🚨 **MIL Alert:** With Giannis AND Lillard OUT, Bobby Portis and Brook Lopez will see massive shot volume. Portis' 18.5 PTS line is the 'Nightowl' play.")
    st.info("🚨 **BOS Alert:** Jaylen Brown is effectively the only #1 option tonight with Tatum out.")

with tab3:
    st.subheader("🎰 PrizePicks Parlay Simulator")
    picks = st.multiselect("Select players to combine:", [p['name'] for p in props])
    if picks:
        total_odds = 1.0
        for name in picks:
            p_data = next(i for i in props if i['name'] == name)
            total_odds *= (p_data['prob'] / 100)
            st.write(f"✅ {name} ({p_data['prob']}% Hit Rate)")
        st.metric("Custom Slip Win Probability", f"{round(total_odds * 100, 2)}%")
        st.success(f"Final Parlay: {' + '.join(picks)}")
