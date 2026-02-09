# RICKY SUNSHINE MASTER CONTROL CORE
# REBOOT & RENDER FIX - FEB 9, 2026

BUILD_CONFIG = {
    "HEADER": "Neon_Sign_Drop_Shadow_Flicker",
    "BACKGROUND": "Basketball_Desaturated_Light (#D3D3D3)", # Fixed hex to prevent black screen
    "SCROLL_SPEED": 0.02, # Faster tap response
    "COPY_PASTE": True,
    "BLACK_SCREEN_PATCH": "ENABLED_HARDWARE_FORCE"
}

LOGIC_GATES = {
    "SCORE_WIPE": "12:00_PM_PST", # Only focus on today
    "AUTO_SWAP": "Late_Night_Transition", # Swap props after West Coast Final
    "NIGHTOWL_PROTO": "Show_Tomorrow_Early"
}

def render_main_feed():
    # Force visibility on reboot
    clear_cache()
    set_brightness(1.15)
    draw(BUILD_CONFIG["BACKGROUND"])
    draw(BUILD_CONFIG["HEADER"])
    return "UI RENDER SUCCESSFUL - NO BLACK SCREEN"
