import streamlit as st
from streamlit_autorefresh import st_autorefresh
import random

# 1. FORCED REBOOT SETTINGS
st.set_page_config(page_title="Nightowl Executive", layout="wide")
st_autorefresh(interval=60000, key="nightowl_sync")

# 2. THE IRONCLAD LEATHER THEME
# The random number forces the browser to dump the 'balloons' and load the leather
cache_id = random.randint(1, 10000)
leather_url = f"https://images.unsplash.com/photo-1544911845-1f34a3eb46b1?q=80&w=2670&v={cache_id}"

st.markdown(f"""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Playball&family=Oswald:wght@700&display=swap');
    
    /* BACKGROUND FORCE */
    [data-testid="stAppViewContainer"], .stApp {{
        background: linear-gradient(rgba(0,0,0,0.85), rgba(0,0,0,0.85)), url('{leather_url}') !important;
        background-size: cover !important;
        background-attachment: fixed !important;
    }}

    /* TEXT READABILITY (DROP SHADOWS) */
    h1, h2, h3, p, span, b, div {{ 
        color: white !important; 
        text-shadow: 3px 3px 10px #000, -1px -1px 10px #000 !important; 
        font-family: 'Oswald', sans-serif;
    }}

    .flicker-title {{
        font-family: 'Playball', cursive; font-size: 4.5rem; text-align: center;
        color: #fff; text-shadow: 0 0 20px #00ff00; animation: blink 2s infinite;
    }}
    @keyframes blink {{ 50% {{ opacity: 0.6; }} }}

    /* SCOREBOARD TICKER */
    .ticker-wrap {{ width: 100%; background: rgba(0,0,0,0.9); border-bottom: 2px solid #00ff00; padding: 10px; overflow: hidden; white-space: nowrap; }}
    .ticker {{ display: inline-block; animation: ticker 35s linear infinite; color: #00ff00 !important; font-size: 1.1rem; }}
    @keyframes ticker {{ 0% {{ transform: translateX(100%); }} 100% {{ transform: translateX(-100%); }} }}
</style>
""", unsafe_allow_html=True)

# 3. INTERFACE
st.markdown('<div class="ticker-wrap"><div class="ticker">🏀 FEB 5: JOKIC ACTIVE | BRUNSON ACTIVE | SGA (OUT) | WEMBY ACTIVE | TATUM (OUT)</div></div>', unsafe_allow_html=True)
st.markdown('<div class="flicker-title">Ricky Sunshine\'s</div>', unsafe_allow_html=True)

st.success("📡 **SYSTEM REBOOT COMPLETE**: New Repository Active. Nightowl protocol initiated.")

tab1, tab2 = st.tabs(["🎯 BOARD", "📡 LIVE FEED"])

with tab1:
    st.markdown("### 🎯 THE EXECUTIVE BOARD")
    st.info("Loading Tomorrow's Transitions...")

with tab2:
    st.write("📡 Monitoring late-night West Coast finales.")
