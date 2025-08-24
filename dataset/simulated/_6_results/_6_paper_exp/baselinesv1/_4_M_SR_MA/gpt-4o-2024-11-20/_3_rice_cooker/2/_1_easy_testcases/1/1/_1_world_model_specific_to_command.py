# Python Comments:
# The current code seems to adequately model the requested user command. The features for selecting the cooking mode, adjusting the preset timer, and starting the appliance are present.
# Sequence of features to achieve the command:
# 1. Use "select_cooking_mode" to set variable_cooking_mode to "congee".
# 2. Use "adjust_preset_timer" to set variable_preset_timer to 480 minutes (8 hours for tomorrow morning).
# 3. Use "start_cooking" to set variable_start_running to "on".
# 
# Relevant raw user manual text:
# Raw text on selecting mode: "Press **Menu/Cancel** to choose Fast cook, White rice, Congee, Soup, Cake, Keep warm."
# Raw text on adjusting preset time: "Press Preset/Timer to adjust the time. ↳ The preset timer indicator blinks. ↳ The rice cooker starts countdown until the cooking process is finished."
# Raw text on starting cooking: "Press **Start** to start the cooking process."
# 
# Features from provided code:
# Feature "select_cooking_mode"
# Feature "adjust_preset_timer"
# Feature "start_cooking"
# 
# Goal variable values to achieve the command:
# - variable_cooking_mode = "congee"
# - variable_preset_timer = 480 (minutes)
# - variable_start_running = "on"

class ExtendedSimulator(Simulator): 
    pass