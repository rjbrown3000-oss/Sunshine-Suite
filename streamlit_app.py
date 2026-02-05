import streamlit as st
import random

# 1. FORCE THE STATE
st.set_page_config(page_title="Nightowl Executive", layout="wide")

# 2. CACHE-BUSTING LEATHER THEME
# The random number at the end of the URL (?v=...) tells Chrome "this is a new image"
v = random.randint(1, 99999)
leather_url = f"https://images.unsplash.com/photo-1544911845-1f34a3eb46b1?auto=format&fit=crop&q=80&w=2670&v={v}"

st.markdown(f"""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Playball&family=Oswald:wght@700&display=swap');
    
    /* KILL THE MAROON & FORCE THE GRAIN */
    [data-testid="stAppViewContainer"], .stApp {{
        background: linear-gradient(rgba(0,0,0,0.85), rgba(0,0,0,0.85)), url('{leather_url}') !important;
        background-size: cover !important;
        background-attachment: fixed !important;
        background-color: #000 !important; /* Fallback to black if image fails */
    }}

    /* TEXT READABILITY (DROP SHADOWS) */
    h1, h2, h3, p, span, b, div {{ 
        color: white !important; 
        text-shadow: 3px 3px 12px rgba(0,0,0,1) !important; 
        font-family: 'Oswald', sans-serif;
    }}

    .flicker-title {{
        font-family: 'Playball', cursive; font-size: 5rem; text-align: center;
        color: #fff; text-shadow: 0 0 20px #00ff00; animation: blink 3s infinite;
    }}
    @keyframes blink {{ 50% {{ opacity: 0.7; }} }}

    /* THE SCOREBOARD TICKER */
    .ticker-wrap {{ width: 100%; background: rgba(0,0,0,0.95); border-bottom: 3px solid #00ff00; padding: 12px; overflow: hidden; }}
    .ticker {{ display: inline-block; white-space: nowrap; animation: ticker 40s linear infinite; color: #00ff00 !important; font-size: 1.2rem; font-weight: bold; }}
    @keyframes ticker {{ 0% {{ transform: translateX(100%); }} 100% {{ transform: translateX(-100%); }} }}
</style>
""", unsafe_allow_html=True)

# 3. INTERFACE
st.markdown('<div class="ticker-wrap"><div class="ticker">🏀 FEB 5: JOKIC ACTIVE | BRUNSON ACTIVE | WEMBY ACTIVE | SGA (OUT) | TATUM (OUT)</div></div>', unsafe_allow_html=True)
st.markdown('<div class="flicker-title">Ricky Sunshine\'s</div>', unsafe_allow_html=True)

st.success("🎯 **LEATHER THEME RESTORED**: If you see the grain, we are ready for props.")

if st.button("🚨 NUKE CACHE"):
    st.cache_data.clear()
    st.rerun()
