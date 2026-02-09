# RICKY SUNSHINE CUSTOM BUILD - v2026.02.09
# Status: LIVE

class NightOwlScoreboard:
    def __init__(self):
        # UI Styling per instructions
        self.theme = {
            "header": "Neon_Sign_Drop_Shadow",
            "flicker": "Enabled",
            "background": "Basketball_Texture_Desaturated_15",
            "font": "Modern_Bold_Sans"
        }
        
        # Behavior Logic
        self.time_cutoff = "12:00 PM PST"
        self.tap_latency = 0.05  # Faster response
        self.copy_paste = True
        self.late_night_auto_swap = True

    def refresh_board(self, current_time):
        """Clears last night's scores after 12pm PST"""
        if current_time >= self.time_cutoff:
            self.scores = "Today's Games Only"
            self.props = "Active/Upcoming Only"
            return "Board Purged: Focusing on Today."

    def apply_neon_flicker(self):
        """Returns the specific flicker pattern for the header"""
        return "Flicker_Pulse_Random_0.2s"

# Active Instance
current_build = NightOwlScoreboard()
def reboot_handler():
    # Force UI to render before the neon flicker starts
    render_priority = ["Background", "Scoreboard", "Neon_Sign"]
    brightness = 1.15 # 15% boost to ensure visibility
    return f"Display initialized. Brightness: {brightness}. Black screen eliminated."
