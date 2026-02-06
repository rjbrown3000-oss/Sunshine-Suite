# --- [RE-ANCHORED BACKGROUND & STADIUM BOARD] ---
st.markdown("""
<style>
    [data-testid="stAppViewContainer"] {
        background: linear-gradient(rgba(255,255,255,0.2), rgba(255,255,255,0.2)), 
        url('https://images.unsplash.com/photo-1544919982-b61976f0ba43?q=80&w=2622&auto=format&fit=crop');
        background-size: cover; background-position: center; background-attachment: fixed !important;
    }
    .stadium-wrapper { perspective: 1200px; background: #000; border-bottom: 5px solid #00ff00; padding: 15px 0; }
    .stadium-ticker { 
        display: flex; white-space: nowrap; font-family: 'Inter', sans-serif; 
        color: #00ff00; font-weight: 900; font-size: 1.6rem; 
        animation: stadium-spin 22s linear infinite; 
    }
    @keyframes stadium-spin { 0% { transform: rotateY(-10deg) translateX(100%); } 100% { transform: rotateY(10deg) translateX(-100%); } }
</style>
<div class="stadium-wrapper">
    <div class="stadium-ticker">
        🏀 NYK @ DET (4:30) | 🏀 MIA @ BOS (4:30) | 🏀 IND @ MIL (5:00) | 🏀 NOP @ MIN (5:00) | 🏀 MEM @ POR (7:00)
        <span style="margin: 0 40px;"></span>
        🚨 VEGAS ALERT: JOSH HART UNDER 24.5 PRA IS JUICED TO -145 (59% PROBABILITY)
    </div>
</div>
""", unsafe_allow_html=True)

tab2, tab3 = st.tabs(["📡 LIVE FEED", "🎰 PP BUILDER"])

with tab2:
    st.subheader("📡 Live Market Discrepancy Feed")
    st.info("🕒 **12:22 PM PST:** Selenium Scan Complete. Found 3 'Stale' lines on PrizePicks.")
    st.error("🚨 **STALE LINE:** Bobby Portis (18.5 PTS) - Vegas has moved to 20.5. Hit the OVER now.")
    st.success("🔄 **CORRELATION:** Giannis OUT -> Portis Usage +8.8% -> Lillard AST Over (Correlation 0.72)")

with tab3:
    st.subheader("🎰 ROI Parlay Builder")
    colA, colB = st.columns(2)
    with colA:
        picks = st.multiselect("Select Slips:", ["Josh Hart O24.5", "Bobby Portis O18.5", "Jaylen Brown O28.5"])
    with colB:
        # Payout Math for 5-Pick Flex
        st.metric("Implied Odds per Leg", "-119", delta="+EV", delta_color="normal")
        st.write("**Strategy Note:** 5-Pick Flexes are the mathematically 'correct' play on PrizePicks.")
    
    if len(picks) > 0:
        st.button("🔥 GENERATE OPTIMIZED SLIP")
