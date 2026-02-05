import streamlit as st
from streamlit_autorefresh import st_autorefresh
import datetime

# 1. CORE SYNC
st.set_page_config(page_title="Ricky's Basketball Suite", layout="wide")
st_autorefresh(interval=60000, key="flicker_sync")

# 2. THE RESTORED BASKETBALL BACKGROUND (V.95 STYLE)
# Using a direct basketball court image to bring back the rim and net feel
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Playball&family=Oswald:wght@700&display=swap');

    [data-testid="stAppViewContainer"] {
        background-image: linear-gradient(rgba(0,0,0,0.7), rgba(0,0,0,0.7)), 
        url('https://images.unsplash.com/photo-1504450758481-7338eba7524a?q=80&w=2669&auto=format&fit=crop');
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
    }

    /* RICKY'S FLICKER TITLE */
    .flicker-title {
        font-family: 'Playball', cursive; font-size: 5rem; text-align: center;
        color: #fff; text-shadow: 0 0 20px #00ff00; animation: blink 2s infinite;
    }
    @keyframes blink { 50% { opacity: 0.5; } }

    /* THE SCROLLING SCOREBOARD (TICKER) */
    .ticker-wrap { width: 100%; background: rgba(0,0,0,0.9); border-bottom: 3px solid #00ff00; padding: 10px; overflow: hidden; }
    .ticker { display: inline-block; white-space: nowrap; animation: ticker 40s linear infinite; color: #00ff00 !important; font-size: 1.2rem; font-weight: bold; }
    @keyframes ticker { 0% { transform: translateX(100%); } 100% { transform: translateX(-100%); } }

    /* READABILITY SHADOWS */
    h1, h2, h3, p, b, span { color: white !important; text-shadow: 2px 2px 8px #000 !important; }
</style>
""", unsafe_allow_html=True)

# 3. INTERFACE
st.markdown('<div class="ticker-wrap"><div class="ticker">🏀 FEB 5 INJURY REPORT: GIANNIS (OUT) | TRAE YOUNG (OUT) | WAGNER (OUT) | CUNNINGHAM (GTD)</div></div>', unsafe_allow_html=True)
st.markdown('<div class="flicker-title">Ricky Sunshine\'s</div>', unsafe_allow_html=True)

# LATE NIGHT TRANSITION (NIGHTOWL MODE)
now = datetime.datetime.now()
if now.hour >= 22 or now.hour < 6:
    st.success("🌙 **NIGHTOWL PROTOCOL**: West Coast final. Transitioning to tomorrow's slate.")
else:
    st.info("📡 **LIVE FEED**: Monitoring active boards.")

# 4. THE PROPS (NIGHTOWL STYLE)
st.markdown("### 🎯 THE BOARD")
st.write("---")
# Placeholder for your specific v.90-era prop board layout
st.markdown("""
<div style="background:rgba(0,0,0,0.6); padding:20px; border-radius:15px; border-left:10px solid #00ff00;">
    <b style="font-size:1.5rem;">GIANNIS ANTETOKOUNMPO</b><br>
    <span style="color:#ff4b4b;">STATUS: OUT (Right Calf)</span><br>
    <span>Projected Return: Mid-February</span>
</div>
""", unsafe_allow_html=True)
