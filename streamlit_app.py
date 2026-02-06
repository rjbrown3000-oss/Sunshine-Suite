import streamlit as st
import datetime
from streamlit_autorefresh import st_autorefresh

# 1. CORE ENGINE SYNC
st.set_page_config(page_title="Ricky's Executive Suite", layout="wide")
st_autorefresh(interval=60000, key="prizepicks_builder_v132")

# 2. UI STYLING (LOCKED COURT BACKGROUND)
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Playball&family=Oswald:wght@700&family=Orbitron:wght@700&display=swap');

    [data-testid="stAppViewContainer"] {
        background-image: linear-gradient(rgba(0,0,0,0.75), rgba(0,0,0,0.75)), 
        url('https://images.unsplash.com/photo-1504450758481-7338eba7524a?q=80&w=2669&auto=format&fit=crop');
        background-size: cover; background-position: center; background-attachment: fixed;
    }

    .led-ticker { background: #000; border-bottom: 3px solid #00ff00; padding: 10px 0; color: #00ff00; font-family: 'Orbitron'; overflow: hidden; white-space: nowrap; }
    .ricky-title { font-family: 'Playball', cursive; font-size: 4.5rem; text-align: center; color: #fff; text-shadow: 0 0 20px #00ff00; margin-top:10px;}
    .prop-card { background: rgba(0,0,0,0.85); border-left: 10px solid #00ff00; padding: 15px; border-radius: 12px; margin-bottom: 10px; }
    .meter-bg { background: rgba(255,255,255,0.1); border-radius: 8px; height: 8px; margin: 5px 0; }
    .meter-fill { background: #00ff00; height: 100%; border-radius: 8px; box-shadow: 0 0 8px #00ff00; }
    h1, h2, h3, b, p, span { color: white !important; }
</style>
""", unsafe_allow_html=True)

# 3. DATA LOAD (LATEST FEB 5-6 PROJECTIONS)
# Updated: Brunson OUT, Duren (Ankle)
all_props = [
    {"name": "Isaiah Collier", "line": 11.5, "stat": "AST", "prob": 88, "tier": "High Value"},
    {"name": "Jalen Johnson", "line": 19.5, "stat": "PTS", "prob": 85, "tier": "High Value"},
    {"name": "Oso Ighodaro", "line": 4.5, "stat": "REB", "prob": 82, "tier": "High Value"},
    {"name": "VJ Edgecombe", "line": 13.5, "stat": "PTS", "prob": 79, "tier": "Medium"},
    {"name": "Luka Doncic", "line": 32.5, "stat": "PTS", "prob": 74, "tier": "Medium"},
    {"name": "Cooper Flagg", "line": 21.5, "stat": "PTS", "prob": 71, "tier": "Medium"},
    {"name": "Michael Porter Jr.", "line": 24.5, "stat": "PTS", "prob": 68, "tier": "Value"},
    {"name": "Immanuel Quickley", "line": 5.5, "stat": "REB", "prob": 65, "tier": "Value"},
    {"name": "Mark Williams", "line": 11.5, "stat": "PTS", "prob": 62, "tier": "Value"},
    {"name": "Paolo Banchero", "line": 8.5, "stat": "REB", "prob": 59, "tier": "Value"}
]

# 4. LED & HEADER
st.markdown('<div class="led-ticker">🚨 GIANNIS (OUT) | TRAE YOUNG (OUT) | JALEN BRUNSON (OUT) | DUREN (DOUBTFUL) | COLLIER PROJECTED 12+ AST</div>', unsafe_allow_html=True)
st.markdown('<div class="ricky-title">Ricky Sunshine\'s</div>', unsafe_allow_html=True)

tab1, tab2, tab3 = st.tabs(["🎯 THE BOARD", "📡 LIVE FEED", "📈 PP PARLAY BUILDER"])

with tab1:
    for p in all_props:
        col1, col2 = st.columns([4, 1])
        with col1:
            st.markdown(f"""
            <div class="prop-card">
                <b>{p['name'].upper()}</b> ({p['tier']})<br>
                <span>{p['stat']} Line: {p['line']}</span>
                <div class="meter-bg"><div class="meter-fill" style="width: {p['prob']}%;"></div></div>
                <small style="color:#00ff00;">Hit Probability: {p['prob']}%</small>
            </div>
            """, unsafe_allow_html=True)
        with col2:
            st.code(f"{p['name']} O{p['line']} {p['stat']}", language="text")

with tab2:
    st.subheader("📡 Live Intel")
    st.info("• Isaiah Collier (Utah) usage is peaking with Keyonte George out. Proj: 14.1 AST.")
    st.info("• VJ Edgecombe (76ers) showing 22% edge vs Lakers defense (ranked 24th).")

with tab3:
    st.subheader("🎰 PrizePicks Parlay Simulator")
    selected_players = st.multiselect("Select Players for your slip:", [p['name'] for p in all_props])
    
    if selected_players:
        total_prob = 100
        st.write("### Current Slip:")
        for name in selected_players:
            p_data = next(item for item in all_props if item["name"] == name)
            total_prob *= (p_data['prob'] / 100)
            st.write(f"✅ **{name}**: {p_data['prob']}% Win Probability")
        
        final_calc = round(total_prob, 2)
        st.divider()
        st.metric("Total Slip Probability", f"{final_calc}%")
        
        if len(selected_players) >= 5:
            st.success("🔥 This is a high-risk Flex Play. Win rate above 54.25% per leg is needed for long-term profit.")
        
        st.write("---")
        st.write("📋 **Copy Full Slip:**")
        full_slip_text = " + ".join([name for name in selected_players])
        st.code(full_slip_text, language="text")
