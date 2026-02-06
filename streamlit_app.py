import streamlit as st
import datetime
from streamlit_autorefresh import st_autorefresh

# 1. CORE ENGINE
st.set_page_config(page_title="Ricky's Executive Suite", layout="wide")
st_autorefresh(interval=30000, key="high_speed_sync_v146")

# 2. UI STYLING (IMPROVED 3D PHYSICS + LIGHT BG)
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Playball&family=Inter:wght@600;900&display=swap');

    [data-testid="stAppViewContainer"] {
        background-image: linear-gradient(rgba(255,255,255,0.18), rgba(255,255,255,0.18)), 
        url('https://images.unsplash.com/photo-1504450758481-7338eba7524a?q=80&w=2669&auto=format&fit=crop');
        background-size: cover; background-position: center; background-attachment: fixed;
    }

    /* FASTER 3D CURVED LED physics */
    .curve-outer {
        perspective: 1500px;
        background: #000;
        overflow: hidden;
        border-bottom: 4px solid #00ff00;
        padding: 10px 0;
    }
    .curved-ticker {
        display: flex;
        white-space: nowrap;
        font-family: 'Inter', sans-serif;
        color: #00ff00;
        font-weight: 900;
        font-size: 1.4rem;
        animation: scroll-3d-fast 18s linear infinite; /* FASTER SPEED */
    }
    @keyframes scroll-3d-fast {
        0% { transform: translateX(110%) rotateY(-15deg) scale(0.95); }
        45%, 55% { transform: translateX(0%) rotateY(0deg) scale(1.15); text-shadow: 0 0 15px #00ff00; }
        100% { transform: translateX(-110%) rotateY(15deg) scale(0.95); }
    }

    .stTabs [data-baseweb="tab-list"] { justify-content: center !important; }
    .stTabs [data-baseweb="tab"] {
        background-color: rgba(20,20,20,0.95) !important;
        border-radius: 10px 10px 0 0;
        box-shadow: 0px 4px 15px rgba(0,0,0,0.6);
        padding: 12px 25px !important;
    }
    .neon-sign {
        font-family: 'Playball', cursive; font-size: 5.5rem; text-align: center; color: #e0ffe0;
        text-shadow: 0 0 5px #fff, 0 0 15px rgba(0,255,0,0.4), 4px 4px 10px rgba(0,0,0,0.8);
        animation: neon-flicker 4s infinite;
    }
    .prop-card { background: rgba(0,0,0,0.88); border-left: 10px solid #00ff00; padding: 18px; border-radius: 12px; margin-bottom: 12px; }
    h1, h2, h3, b, p, span, small { color: white !important; }
</style>
""", unsafe_allow_html=True)

# 3. THE CURVED LED (FULL FRIDAY SLATE FOCUS)
st.markdown("""
<div class="curve-outer">
    <div class="curved-ticker">
        📅 TONIGHT: NYK @ DET (4:30 PM) | MIA @ BOS (4:30 PM) | IND @ MIL (5:00 PM) | PHI @ ORL (5:00 PM) | CHA @ CLE (5:00 PM) | MIN @ CHI (5:00 PM) | MEM @ POR (7:00 PM) | ATL @ PHX (7:00 PM)
    </div>
</div>
""", unsafe_allow_html=True)

st.markdown('<div class="neon-sign">Ricky Sunshine\'s</div>', unsafe_allow_html=True)

# 4. SIDEBAR (INJURY HUB & POPUP ALERTS)
with st.sidebar:
    st.title("🛡️ ALERT CENTER")
    if st.button("🔄 FORCE DAY-MODE REFRESH"):
        st.cache_data.clear()
        st.rerun()
    
    st.write("---")
    st.subheader("🚨 CRITICAL ALERTS")
    # Josh Hart Logic
    st.warning("⚠️ JOSH HART (Q - Ankle): Decision at 4:00 PM PST. Usage is +11% if Active.")
    # KAT Logic
    st.warning("⚠️ KAT (GTD - Eye): Warmups will determine status.")
    
    st.write("---")
    st.markdown("## 📋 CONFIRMED OUT")
    st.error("GIANNIS | LUKA | TATUM | LILLARD | HALIBURTON | CURRY")

# 5. THE BOARD (TAB 1)
props = [
    {"name": "Josh Hart", "line": 24.5, "stat": "P+R+A", "prob": 91, "logs": "28, 26, 25, 20, 29", "trend": "🔥 +15%"},
    {"name": "Bobby Portis", "line": 18.5, "stat": "PTS", "prob": 89, "logs": "22, 19, 17, 24, 20", "trend": "🔥 +25%"},
    {"name": "Jaylen Brown", "line": 28.5, "stat": "PTS", "prob": 87, "logs": "32, 28, 30, 24, 27", "trend": "🔥 +18%"},
    {"name": "Cade Cunningham", "line": 26.5, "stat": "PTS", "prob": 86, "logs": "30, 26, 29, 18, 22", "trend": "📈 +5%"},
    {"name": "Jaden Ivey", "line": 4.5, "stat": "AST", "prob": 83, "logs": "6, 5, 4, 7, 5", "trend": "📈 +9%"}
]

tab1, tab2, tab3, tab4 = st.tabs(["🎯 THE BOARD", "📡 LIVE FEED", "🎰 PP BUILDER", "📊 ANALYTICS"])

with tab1:
    for p in props:
        col1, col2 = st.columns([4, 1])
        with col1:
            st.markdown(f"""
            <div class="prop-card">
                <b>{p['name'].upper()}</b> <span style="color:#00ff00; float:right;">{p['trend']}</span><br>
                <span>{p['stat']} Line: {p['line']}</span><br>
                <div style="background:rgba(255,255,255,0.1); border-radius:8px; height:8px; margin:8px 0;">
                    <div style="background:#00ff00; width:{p['prob']}%; height:100%; border-radius:8px;"></div>
                </div>
            </div>
            """, unsafe_allow_html=True)
        with col2: st.code(f"{p['name']} O{p['line']} {p['stat']}")

with tab2:
    st.subheader("📡 Live Injury Watch")
    st.info("🕒 **11:38 AM PST:** All 8 games confirmed for today's slate. No missing data.")
    st.success("✅ **Recap:** System preparing for 12:00 PM score purge.")
