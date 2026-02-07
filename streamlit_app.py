import streamlit as st
from streamlit_autorefresh import st_autorefresh

# 1. THE FOUNDATION
st.set_page_config(page_title="Ricky's Executive Suite v156", layout="wide")
st_autorefresh(interval=30000, key="v156_sync")

st.markdown("""
<style>
    /* ANCHORED LIGHT COURT BACKGROUND */
    [data-testid="stAppViewContainer"] {
        background: linear-gradient(rgba(255,255,255,0.25), rgba(255,255,255,0.25)), 
        url('https://images.unsplash.com/photo-1544919982-b61976f0ba43?q=80&w=2622&auto=format&fit=crop');
        background-size: cover; background-position: center; background-attachment: fixed !important;
    }

    /* CYLINDRICAL STADIUM TICKER (ULTRA FAST) */
    .stadium-outer { perspective: 1200px; background: #000; overflow: hidden; border-bottom: 5px solid #00ff00; }
    .stadium-inner {
        display: flex; white-space: nowrap; font-family: 'Inter', sans-serif;
        color: #00ff00; font-weight: 900; font-size: 1.8rem;
        animation: stadium-spin 10s linear infinite;
        transform-style: preserve-3d;
    }
    @keyframes stadium-spin {
        0% { transform: rotateY(-15deg) translateX(100%); }
        100% { transform: rotateY(15deg) translateX(-150%); }
    }

    /* NEON SIGN */
    .neon-sign {
        font-family: 'Playball', cursive; font-size: 5.8rem; text-align: center; color: #e0ffe0;
        text-shadow: 4px 4px 15px rgba(0,0,0,0.95), 0 0 25px rgba(0,255,0,0.7);
        margin: 20px 0;
    }

    .prop-card { background: rgba(0,0,0,0.92); border-left: 10px solid #00ff00; padding: 20px; border-radius: 12px; margin-bottom: 12px; box-shadow: 0 4px 15px rgba(0,0,0,0.5); }
    .stButton>button { width: 100%; background-color: #00ff00 !important; color: black !important; font-weight: 900 !important; }
</style>
""", unsafe_allow_html=True)

# 2. THE STADIUM TICKER (TODAY'S 10 GAMES ONLY)
st.markdown("""
<div class="stadium-outer">
    <div class="stadium-inner">
        🏀 WAS@BKN | 🏀 HOU@OKC | 🏀 UTA@ORL | 🏀 CHA@ATL | 🏀 DAL@SAS | 🏀 DEN@CHI | 🏀 PHI@CLE | 🏀 PHX@SAC | 🏀 GSW@LAL | 🏀 MEM@POR
    </div>
</div>
""", unsafe_allow_html=True)

st.markdown('<div class="neon-sign">Ricky Sunshine\'s</div>', unsafe_allow_html=True)

# 3. SIDEBAR (BUILDER)
with st.sidebar:
    st.title("🎰 PP BUILDER")
    picks = st.multiselect("Select Value Props:", ["LeBron O22.5", "Wemby O11.5", "Avdija O22.5", "Jerome 15+", "Williams O16.5"])
    if len(picks) >= 5:
        st.success("🔥 5-PICK FLEX ROI: 25X")
    st.write("---")
    st.header("🚨 TODAY'S OUTS")
    st.error("LUKA DONCIC | STEPH CURRY | SGA | TYRESE HALIBURTON")

# 4. PROPS BOARD
cols = st.columns(2)
for i, p in enumerate(props_data): # props_data populated from the table above
    with cols[i % 2]:
        st.markdown(f"""
        <div class="prop-card">
            <span style="color:#00ff00; font-weight:900; float:right;">{p['Vegas Prob']}</span>
            <b style="font-size:1.4rem; color:white;">{p['Player'].upper()}</b><br>
            <span style="color:#aaa;">{p['Prop Line']} | {p['Why It’s Value']}</span>
        </div>
        """, unsafe_allow_html=True)
        if st.button(f"COPY {p['Player']}", key=f"btn_{i}"):
            st.toast(f"Copied {p['Player']} to clipboard!")
