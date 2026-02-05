import streamlit as st
import datetime
from streamlit_autorefresh import st_autorefresh

# 1. CORE SYNC & REFRESH (Keep flicker alive)
st.set_page_config(page_title="Ricky's Basketball Suite", layout="wide")
st_autorefresh(interval=60000, key="nightowl_refresh")

# 2. THE STABLE BASKETBALL COURT THEME
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Playball&family=Oswald:wght@700&display=swap');

    [data-testid="stAppViewContainer"] {
        background-image: linear-gradient(rgba(0,0,0,0.75), rgba(0,0,0,0.75)), 
        url('https://images.unsplash.com/photo-1504450758481-7338eba7524a?q=80&w=2669&auto=format&fit=crop');
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
    }

    /* RICKY'S NEON FLICKER */
    .flicker-title {
        font-family: 'Playball', cursive; font-size: 4.5rem; text-align: center;
        color: #fff; text-shadow: 0 0 20px #00ff00, 0 0 30px #00ff00;
        animation: blink 2.5s infinite;
        margin-bottom: 10px;
    }
    @keyframes blink { 
        0%, 18%, 22%, 25%, 53%, 57%, 100% { opacity: 1; }
        20%, 24%, 55% { opacity: 0.4; }
    }

    /* THE SCOREBOARD TICKER */
    .ticker-wrap { width: 100%; background: rgba(0,0,0,0.95); border-bottom: 3px solid #00ff00; padding: 12px 0; overflow: hidden; }
    .ticker { display: inline-block; white-space: nowrap; animation: ticker 45s linear infinite; color: #00ff00 !important; font-size: 1.2rem; font-weight: bold; }
    @keyframes ticker { 0% { transform: translateX(100%); } 100% { transform: translateX(-100%); } }

    /* PROP CARDS */
    .prop-card {
        background: rgba(255, 255, 255, 0.05);
        border-left: 10px solid #00ff00;
        padding: 20px;
        border-radius: 15px;
        margin-bottom: 15px;
        box-shadow: 5px 5px 15px rgba(0,0,0,0.6);
    }
    h1, h2, h3, b, p, span { color: white !important; text-shadow: 2px 2px 10px #000 !important; }
</style>
""", unsafe_allow_html=True)

# 3. THE TICKER (FEB 5-6 UPDATES)
st.markdown('<div class="ticker-wrap"><div class="ticker">🏀 FEB 5-6: GIANNIS (OUT - CALF) | TRAE YOUNG (OUT) | WAGNER (OUT) | CUNNINGHAM (GTD) | BRUNSON (ACTIVE - 27.2 PPG)</div></div>', unsafe_allow_html=True)
st.markdown('<div class="flicker-title">Ricky Sunshine\'s</div>', unsafe_allow_html=True)

# 4. NIGHTOWL LOGIC (AUTO-SWAP PROPS)
now = datetime.datetime.now()
is_nightowl = now.hour >= 22 or now.hour < 6

if is_nightowl:
    st.success("🌙 **LATE NIGHT TRANSITION**: Today's games finalized. Loading Tomorrow's Early Props.")
    # Tomorrow's Early Value (Feb 6)
    props = {
        "Michael Porter Jr.": ["24.5", "PTS", "BKN", "1629008"],
        "Kelly Oubre Jr.": ["14.5", "PTS", "PHI", "1626162"]
    }
else:
    st.info("📡 **LIVE BOARD**: Tracking today's active rotations.")
    props = {
        "Jalen Brunson": ["27.5", "PTS", "NYK", "1628973"],
        "Jalen Duren": ["11.5", "REB", "DET", "1631105"]
    }

# 5. THE BOARD
cols = st.columns(len(props))
for i, (player, data) in enumerate(props.items()):
    with cols[i]:
        img = f"https://cdn.nba.com/headshots/nba/latest/1040x760/{data[3]}.png"
        st.markdown(f"""
        <div class="prop-card">
            <img src="{img}" style="width:100px; border-radius:50%; border:2px solid #00ff00; background:#000;">
            <h3>{player.upper()}</h3>
            <b style="color:#00ff00; font-size:1.3rem;">{data[2]} | {data[1]}: Over {data[0]}</b>
        </div>
        """, unsafe_allow_html=True)
