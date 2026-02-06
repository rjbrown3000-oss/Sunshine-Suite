import streamlit as st
from streamlit_autorefresh import st_autorefresh

# 1. CORE ENGINE & BACKGROUND LOCK
st.set_page_config(page_title="Ricky's Shadow Suite v152", layout="wide")
st_autorefresh(interval=30000, key="v152_ultra_sync")

st.markdown("""
<style>
    /* ANCHORED BASKETBALL BACKGROUND */
    [data-testid="stAppViewContainer"] {
        background: linear-gradient(rgba(255,255,255,0.2), rgba(255,255,255,0.2)), 
        url('https://images.unsplash.com/photo-1544919982-b61976f0ba43?q=80&w=2622&auto=format&fit=crop');
        background-size: cover; background-position: center; background-attachment: fixed !important;
    }

    /* HIGH-SPEED CYLINDRICAL STADIUM SCOREBOARD */
    .stadium-wrapper {
        perspective: 1200px;
        background: #000;
        border-bottom: 5px solid #00ff00;
        padding: 12px 0;
        overflow: hidden;
    }
    .stadium-ticker {
        display: flex;
        white-space: nowrap;
        font-family: 'Inter', sans-serif;
        color: #00ff00;
        font-weight: 900;
        font-size: 1.7rem;
        animation: stadium-spin-fast 14s linear infinite; /* INCREASED SPEED */
    }
    @keyframes stadium-spin-fast {
        0% { transform: rotateY(-12deg) translateX(100%); }
        100% { transform: rotateY(12deg) translateX(-110%); }
    }

    .prop-card { background: rgba(0,0,0,0.92); border-left: 10px solid #00ff00; padding: 20px; border-radius: 12px; margin-bottom: 12px; }
    .vegas-pill { background: #111; color: #00ff00; padding: 4px 8px; border-radius: 5px; font-size: 0.8rem; border: 1px solid #00ff00; }
</style>
""", unsafe_allow_html=True)

# 2. THE 6-GAME FRIDAY SLATE (FEB 6, 2026)
st.markdown("""
<div class="stadium-wrapper">
    <div class="stadium-ticker">
        🏀 MIA @ BOS (4:30) | 🏀 NYK @ DET (4:30) | 🏀 IND @ MIL (5:00) | 🏀 NOP @ MIN (5:00) | 🏀 MEM @ POR (7:00) | 🏀 LAC @ SAC (7:00)
        <span style="margin: 0 40px;"></span>
        🚨 INJURY ALERT: GIANNIS (OUT) | TATUM (OUT) | HERRO (OUT) | HALIBURTON (OUT)
    </div>
</div>
""", unsafe_allow_html=True)

st.markdown('<div style="font-family:\'Playball\'; font-size:5.5rem; text-align:center; color:#e0ffe0; text-shadow: 0 0 10px #00ff00;">Ricky Sunshine\'s</div>', unsafe_allow_html=True)

# 3. 10 HIGH-VALUE PLAYER PROPS (SHADOW ANALYTICS)
# Analyzing value based on the 54.25% breakeven rule
props = [
    {"name": "Bobby Portis", "line": 18.5, "stat": "PTS", "v_prob": "58.2%", "edge": "ELITE", "notes": "No Giannis"},
    {"name": "Josh Hart", "line": 24.5, "stat": "P+R+A", "v_prob": "56.4%", "edge": "HIGH", "notes": "Usage Spike"},
    {"name": "Bam Adebayo", "line": 18.5, "stat": "PTS", "v_prob": "55.8%", "edge": "HIGH", "notes": "No Herro"},
    {"name": "Jaylen Brown", "line": 28.5, "stat": "PTS", "v_prob": "54.8%", "edge": "VALUE", "notes": "No Tatum"},
    {"name": "Cade Cunningham", "line": 26.5, "stat": "PTS", "v_prob": "51.2%", "edge": "NEUTRAL", "notes": "Stable"},
    {"name": "OG Anunoby", "line": 25.5, "stat": "P+R+A", "v_prob": "57.1%", "edge": "HIGH", "notes": "KAT Doubtful"},
    {"name": "Jaden Ivey", "line": 4.5, "stat": "AST", "v_prob": "54.2%", "edge": "VALUE", "notes": "Pace Play"},
    {"name": "Tyrese Maxey", "line": 6.5, "stat": "AST", "v_prob": "53.7%", "edge": "NEUTRAL", "notes": "Heavy Usage"},
    {"name": "Pascal Siakam", "line": 23.5, "stat": "PTS", "v_prob": "54.5%", "edge": "VALUE", "notes": "No Hali"},
    {"name": "Jrue Holiday", "line": 13.5, "stat": "PTS", "v_prob": "55.1%", "edge": "HIGH", "notes": "Scoring Gap"}
]

tab1, tab2, tab3 = st.tabs(["🎯 THE BOARD", "📡 LIVE FEED", "🎰 PP BUILDER"])

with tab1:
    for p in props:
        col1, col2 = st.columns([3, 1])
        with col1:
            st.markdown(f"""
            <div class="prop-card">
                <b style="font-size:1.4rem;">{p['name'].upper()}</b> 
                <span style="float:right;" class="vegas-pill">Vegas Implied: {p['v_prob']}</span><br>
                <span style="color:#aaa;">{p['stat']} Line: {p['line']} | <span style="color:#00ff00;">{p['edge']}</span></span><br>
                <small style="color:#888;">{p['notes']}</small>
            </div>
            """, unsafe_allow_html=True)
        with col2:
            st.code(f"Pick: OVER")
            st.button(f"Copy", key=f"btn_{p['name']}")

with tab2:
    st.subheader("📡 Live Value Radar")
    st.error("🚨 STALE LINE: Portis 18.5 PTS. Vegas moved to 20.5. Take the Over.")
    st.info("🕒 Market update: Hart PRA is stable at 24.5; juice shifted to Under (-145).")
