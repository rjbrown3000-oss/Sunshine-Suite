# --- [SIMULATED SELENIUM DATA FEED] ---
# This section represents the data your Selenium script would push to the UI
live_feed = [
    {"name": "Josh Hart", "current": 24.5, "prev": 23.5, "change": "+1.0", "prob": "54%", "edge": "High"},
    {"name": "Bobby Portis", "current": 18.5, "prev": 16.5, "change": "+2.0", "prob": "58%", "edge": "Elite"},
    {"name": "Jaylen Brown", "current": 28.5, "prev": 28.5, "change": "0.0", "prob": "52%", "edge": "Neutral"}
]

# --- [UI DISPLAY IN TAB 2: LINE HISTORY] ---
with tab2:
    st.subheader("📡 Selenium Line Watch")
    for move in live_feed:
        if float(move['change']) != 0:
            st.warning(f"🚨 **{move['name']}** moved {move['change']} (Now {move['current']})")
        else:
            st.write(f"✅ {move['name']} remains stable at {move['current']}")
