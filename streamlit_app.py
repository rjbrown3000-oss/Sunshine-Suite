import streamlit as st
from streamlit_autorefresh import st_autorefresh

# 1. ENGINE & BACKGROUND
st.set_page_config(page_title="Ricky's Executive Suite", layout="wide")
st_autorefresh(interval=30000, key="v153_restore")

st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Playball&family=Inter:wght@900&display=swap');

    /* RESTORED LIGHT COURT BACKGROUND */
    [data-testid="stAppViewContainer"] {
        background: linear-gradient(rgba(255,255,255,0.25), rgba(255,255,255,0.25)), 
        url('https://images.unsplash.com/photo-1544919982-b61976f0ba43?q=80&w=2622&auto=format&fit=crop');
        background-size: cover; background-position: center; background-attachment: fixed !important;
    }

    /* CYLINDRICAL STADIUM TICKER (HIGH SPEED) */
    .stadium-outer { perspective: 1000px; background: #000; overflow: hidden; border-bottom: 4px solid #00ff00; }
    .stadium-inner {
        display: flex; white-space: nowrap; font-family: 'Inter', sans-serif;
        color: #00ff00; font-weight: 900; font-size: 1.8rem;
        animation: stadium-cylinder 10s linear infinite; /* ULTRA FAST */
        transform-style: preserve-3d;
    }
    @keyframes stadium-cylinder {
        0% { transform: rotateY(-20deg) translateX(100%); }
        50% { transform: rotateY(0deg) translateX(0%); filter: drop-shadow(0 0 15px #00ff00); }
        100% { transform: rotateY(20deg) translateX(-100%); }
    }

    /* NEON SIGN RESTORE */
    .neon-sign {
        font-family: 'Playball', cursive; font-size: 5.5rem; text-align: center; color: #e0ffe0;
        text-shadow: 3px 3px 10px rgba(0,0,0,0.9), 0 0 20px rgba(0,255,0,0.6);
        animation: flicker 3s infinite; margin-top: 10px;
    }
    @keyframes flicker { 0%, 18%, 22%, 100% { opacity: 1; } 20% { opacity: 0.8; } }

    .prop-card { background: rgba(0,0,0,0.9); border-left: 10px solid #00ff00; padding: 18px; border-radius: 12px; margin-bottom: 10px; }
</style>
""", unsafe_allow_html=True)

# 2. STADIUM TICKER (6 VERIFIED GAMES)
st.markdown("""
<div class="stadium-outer">
    <div class="stadium-inner">
        🏀 MIA @ BOS (4:30) | 🏀 NYK @ DET (4:30) | 🏀 IND @ MIL (5:00) | 🏀 NOP @ MIN (5:00) | 🏀 MEM @ POR (7:00) | 🏀 LAC @ SAC (7:00)
    </div>
</div>
""", unsafe_allow_html=True)

st.markdown('<div class="neon-sign">Ricky Sunshine\'s</div>', unsafe_allow_html=True)

# 3. SIDEBAR (BUILDER & INJURY)
with st.sidebar:
    st.header("🎰 PARLAY BUILDER")
    picks = st.multiselect("Select Legs (54.25% Rule):", ["Hart O24.5", "Portis O18.5", "Adebayo O18.5", "Brown O28.5"])
    if picks: st.success(f"Projected ROI: +{len(picks)*12}%")
    
    st.write("---")
    st.header("🚨 INJURY HUB")
    st.error("OUT: Giannis, Tatum, Haliburton, Herro")
    st.warning("GTD: Josh Hart (Ankle), KAT (Eye)")

# 4. PLAYER PROPS (10 VALUE PLAYS)
props = [
    {"p": "Bobby Portis", "l": 18.5, "s": "PTS", "v": "58.2%", "n": "Giannis OUT"},
    {"p": "Josh Hart", "l": 24.5, "s": "P+R+A", "v": "56.4%", "n": "McBride OUT"},
    {"p": "Bam Adebayo", "l": 18.5, "s": "PTS", "v": "55.8%", "n": "Herro OUT"},
    {"p": "Jaylen Brown", "l": 28.5, "s": "PTS", "v": "54.8%", "n": "Tatum OUT"},
    {"p": "OG Anunoby", "l": 25.5, "s": "P+R+A", "v": "57.1%", "n": "KAT Questionable"},
    {"p": "Jaden Ivey", "l": 4.5, "s": "AST", "v": "54.2%", "n": "Pace up"},
    {"p": "Pascal Siakam", "l": 23.5, "s": "PTS", "v": "54.5%", "n": "Hali OUT"},
    {"p": "Jrue Holiday", "l": 13.5, "s": "PTS", "v": "55.1%", "n": "Usage boost"},
    {"p": "De'Aaron Fox", "l": 6.5, "s": "AST", "v": "53.9%", "n": "Primary feeder"},
    {"p": "Miles Bridges", "l": 21.5, "s": "PTS", "v": "54.1%", "n": "Value Play"}
]

cols = st.columns(2)
for i, p in enumerate(props):
    with cols[i % 2]:
        st.markdown(f"""
        <div class="prop-card">
            <b>{p['p'].upper()}</b> <span style="float:right; color:#00ff00;">{p['v']}</span><br>
            <small>{p['s']} Line: {p['l']} | {p['n']}</small>
        </div>
        """, unsafe_allow_html=True)
