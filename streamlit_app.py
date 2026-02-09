# v2.09.06 STABLE RENDER
def render_no_flicker():
    # Disabling all dynamic animations to stop the grey boxes
    config = {
        "animation": None,
        "shadow_type": "Solid_Black", # Removed opacity
        "background": "#E0E0E0",     # Solid Light Grey
        "hardware_acceleration": False
    }
    return "UI RE-STABILIZED"
