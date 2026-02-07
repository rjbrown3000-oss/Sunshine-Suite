# --- [V158.0 INTERFACE SYNC] ---
st.markdown('<div class="neon-sign">Ricky Sunshine\'s</div>', unsafe_allow_html=True)

with st.sidebar:
    st.header("🎰 ROI BUILDER")
    # Dynamically tracking the "Power Vacuum" plays
    selections = st.multiselect("Select Legs:", ["Wemby O11.5 REB", "Reaves O28.5 P+A", "Sheppard U2.5 AST", "Williams O16.5 PRA"])
    if len(selections) >= 5:
        st.success("🔥 OPTIMAL 5-PICK FLEX DETECTED")

    st.write("---")
    st.header("🚨 ROSTER MOVES")
    st.error("KUMINGA -> Hawks (OUT)")
    st.success("ALVARADO -> Knicks (ACTIVE)")
