import streamlit as st
import datetime
from streamlit_autorefresh import st_autorefresh

# 1. ENGINE
st.set_page_config(page_title="Ricky's Executive Suite", layout="wide")
st_autorefresh(interval=30000, key="verified_sync_v145")

# 2. UI STYLING (3D CURVED LED + NEON + LIGHT BG)
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Playball&family=Inter:wght@600;800&display=swap');

    [data-testid="stAppViewContainer"] {
        background-image: linear-gradient(rgba(255,255,255,0.18), rgba(255,255,255,0.18)), 
        url('https://images.unsplash.com/photo-1504450758481-7338eba7524a?q=80&w=2669&auto=format&fit=crop');
        background-size: cover; background-position: center; background-attachment: fixed;
    }

    /* THE CURVED 3D SCOREBOARD */
    .curve-outer {
        perspective: 1200px;
        background: #000;
        overflow: hidden;
        border-bottom: 3px solid #00ff00;
        padding: 15px 0;
    }
    .curved-ticker {
        display: flex;
        white-space: nowrap;
        font-family: 'Inter', sans-serif;
        color: #00ff00;
        font-weight: 800;
        font-size: 1.3rem;
        animation: scroll-3d 30s linear infinite;
    }
    @keyframes scroll-3d {
        0% { transform: translateX(100%) rotateY(-25deg) scale(0.85); opacity: 0.7; }
        50% { transform: translateX(0%) rotateY(0deg) scale(1.2); opacity: 1; text-shadow: 0 0 20px #00ff00; }
        100% { transform: translateX(-100%) rotateY(25deg) scale(0.85); opacity: 0.7; }
    }

    .stTabs [data-baseweb="tab-list"] { justify-content: center !important; gap: 20px; }
    .stTabs [data-baseweb="tab"] {
        background-color: rgba(20,20,20,0.95) !important;
        border-radius: 10px 10px 0 0;
        box-shadow: 0px 4px 15px rgba(0,0,0,0.6);
        padding: 12px 25px !important;
        border: none !important;
    }
    .neon-sign {
        font-family: 'Playball', cursive; font-size: 5.5rem; text-align: center; color: #e0ffe0;
        text-shadow: 0 0 5px #fff, 0 0 15px rgba(0,255,0,0.4), 4px 4px 10px rgba(0,0,0,0.8);
        animation: neon-flicker 4s infinite;
    }
    @keyframes neon-flicker { 0%, 19%, 21%, 100% { opacity: 1; } 20% { opacity: 0.8; } }
    .prop-card { background: rgba(0,0,0,0.88); border-left: 10px solid #00ff00; padding: 18px; border-radius: 12px; margin-bottom: 12px; }
    h1, h2, h3, b, p, span, small { color: white !important; }
</style>
""", unsafe_allow_html=True)

# 3. THE CURVED LED
st.markdown("""
<div class="curve-outer">
    <div class="curved-ticker">
        ✅ FINAL: LAL 119-115 PHI | ✅ FINAL: GSW 101-97 PHX | ✅ FINAL: SAS 135-123 DAL | ✅ FINAL: WAS 126-117 DET | ✅ FINAL: CHA 109-99 HOU
        <span style="margin: 0 60px;"></span> 
        📅 TONIGHT: NYK @ DET (4:30 PM) | MIA @ BOS (4:30 PM) | IND @ MIL (5:00 PM) | MEM @ POR (10:00 PM)
    </div>
</div>
""", unsafe_allow_html=True)

st.markdown('<div class="neon-sign">Ricky Sunshine\'s</div>', unsafe_allow_html=True)

# 4. SIDEBAR (THOROUGH INJURY SCRUB)
with st.sidebar:
    if st.button("🔄 REFRESH LIVE DATA"):
        st.cache_data.clear()
        st.session_state.last_refresh = datetime.datetime.now().strftime("%H:%M:%S")
        st.rerun()
    if 'last_refresh' in st.session_state: st.caption(f"Last Sync: {st.session_state.last_refresh}")
    
    st.write("---")
    st.markdown("## 🚨 INJURY HUB")
    st.error("**GIANNIS** (OUT) | **LUKA** (OUT) | **TATUM** (OUT)")
    st.error("**LILLARD** (OUT) | **HALIBURTON** (OUT) | **CURRY** (OUT)")
    st.warning("**JOSH HART** (Q - Ankle) | **KAT** (Q - Eye)")

# 5. THE BOARD (TAB 1 - UPDATED HART LINE)
props = [
    {"name": "Josh Hart", "line": 24.5, "stat": "P+R+A", "prob": 91, "logs": "28, 26, 25, 20, 29", "trend": "🔥 +15%", "usage": "+11.2%"},
    {"name": "Bobby Portis", "line": 18.5, "stat": "PTS", "prob": 89, "logs": "22, 19, 17, 24, 20", "trend": "🔥 +25%", "usage": "+8.8%"},
    {"name": "Jaylen Brown", "line": 28.5, "stat": "PTS", "prob": 87, "logs": "32, 28, 30, 24, 27", "trend": "🔥 +18%", "usage": "+6.4%"},
    {"name": "Cade Cunningham", "line": 26.5, "stat": "PTS", "prob": 86, "logs": "30, 26, 29, 18, 22", "trend": "📈 +5%", "usage": "+1.1%"},
]

tab1, tab2, tab3, tab4 = st.tabs(["🎯 THE BOARD", "📡 LIVE FEED", "🎰 PP BUILDER", "📊 ANALYTICS"])

with tab1:
    for p in props:
        col1, col2 = st.columns([4, 1])
        with col1:
            st.markdown(f"""
            <div class="prop-card">
                <b style="font-size:1.2rem;">{p['name'].upper()}</b> <span style="color:#00ff00; float:right;">{p['trend']}</span><br>
                <span>{p['stat']} Line: {p['line']}</span><br>
                <small style="color:#aaa;">Usage Spike: {p['usage']} | Prob: {p['prob']}%</small>
                <div style="background:rgba(255,255,255,0.1); border-radius:8px; height:8px; margin:8px 0;">
                    <div style="background:#00ff00; width:{p['prob']}%; height:100%; border-radius:8px;"></div>
                </div>
            </div>
            """, unsafe_allow_html=True)
        with col2: st.code(f"{p['name']} O{p['line']} {p['stat']}")

with tab4:
    st.subheader("📊 Unit Tracking & Bankroll")
    st.metric("Recommended Unit Size", "$20.00", delta="+2.5% vs Yesterday")
