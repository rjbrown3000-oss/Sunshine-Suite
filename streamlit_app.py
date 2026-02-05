import streamlit as st
import datetime

# 1. CORE ENGINE
st.set_page_config(page_title="Nightowl Executive", layout="wide")

# 2. THE BULLETPROOF GRADIENT THEME (NO EXTERNAL LINKS)
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Playball&family=Oswald:wght@700&display=swap');
    
    /* This creates a "Leather-Look" texture using only CSS gradients */
    [data-testid="stAppViewContainer"], .stApp {
        background-color: #0e1117 !important;
        background-image: 
            radial-gradient(circle at 50% 50%, rgba(255,255,255,0.02) 1px, transparent 1px),
            linear-gradient(to bottom, #1a1a1a, #000000) !important;
        background-size: 4px 4px, 100% 100% !important;
        background-attachment: fixed !important;
    }

    /* TEXT READABILITY (DROP SHADOWS) */
    h1, h2, h3, p, span, b, div { 
        color: white !important; 
        text-shadow: 3px 3px 12px #000, 0px 0px 10px rgba(0,255,0,0.3) !important; 
        font-family: 'Oswald', sans-serif;
    }

    .flicker-title {
        font-family: 'Playball', cursive; font-size: 4.5rem; text-align: center;
        color: #fff; text-shadow: 0 0 20px #00ff00; animation: blinker 2s infinite;
        margin-top: 20px;
    }
    @keyframes blinker { 50% { opacity: 0.6; } }

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
        box-shadow: 5px 5px 15px rgba(0,0,0,0.5);
    }
</style>
""", unsafe_allow_html=True)

# 3. INTERFACE & INJURY REPORT
st.markdown('<div class="ticker-wrap"><div class="ticker">🏀 FEB 5 INJURY REPORT: GIANNIS (OUT - CALF) | TRAE YOUNG (OUT - KNEE) | FRANZ WAGNER (OUT - ANKLE) | CADE CUNNINGHAM (GTD)</div></div>', unsafe_allow_html=True)
st.markdown('<div class="flicker-title">Ricky Sunshine\'s</div>', unsafe_allow_html=True)

# LATE NIGHT TRANSITION CHECK
now = datetime.datetime.now()
if now.hour >= 22 or now.hour < 6:
    st.success("🌙 **NIGHTOWL MODE ACTIVE**: Showing tomorrow's early lines.")
else:
    st.info("📡 **LIVE FEED**: Monitoring today's active board.")

# 4. THE BOARD
col1, col2 = st.columns(2)
with col1:
    st.markdown("""<div class="prop-card">
        <b>GIANNIS ANTETOKOUNMPO</b><br>
        <span style="color:#ff4b4b;">STATUS: OUT (Right Calf Strain)</span><br>
        <small>Projected return: Mid-to-late February</small>
    </div>""", unsafe_allow_html=True)

with col2:
    st.markdown("""<div class="prop-card">
        <b>TRAE YOUNG</b><br>
        <span style="color:#ff4b4b;">STATUS: OUT (Right Knee)</span><br>
        <small>Hawks backcourt usage up for Dejounte Murray</small>
    </div>""", unsafe_allow_html=True)
