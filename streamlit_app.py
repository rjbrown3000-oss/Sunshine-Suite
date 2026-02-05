import streamlit as st
import random

# 1. NEW STATE
st.set_page_config(page_title="Background Test", layout="wide")

# 2. THE TEST CSS (NO IMAGES, JUST COLOR)
st.markdown("""
<style>
    /* Targeting every possible Streamlit container to kill the balloons */
    [data-testid="stAppViewContainer"], 
    .stApp, 
    .main, 
    .st-emotion-cache-1v064yh {
        background-color: #800000 !important; /* SOLID MAROON */
        background-image: none !important;    /* KILLS BALLOONS */
    }

    /* Kills the top decoration bar */
    [data-testid="stDecoration"] {
        display: none !important;
    }

    /* FORCED WHITE TEXT WITH SHADOWS */
    h1, h2, h3, p, span, b, div {
        color: white !important;
        text-shadow: 2px 2px 4px #000 !important;
    }
</style>
""", unsafe_allow_html=True)

# 3. VISUAL CHECK
st.markdown("# 🚨 IF YOU SEE MAROON, THE CODE IS WORKING")
st.write("If you still see the sky/balloons, the server is stuck on an old version.")

if st.button("RESET CACHE"):
    st.cache_data.clear()
    st.rerun()
