# The provided code already accurately models the functions for the described command.

# As per the user command:
# "Set the mode to soup, starting four hours from now, and start the machine."
# The sequence of features needed is as follows:
# 1. Feature "select_cooking_mode": Use the action "press_menu_cancel_button" to set "variable_cooking_mode" to "soup".
# 2. Feature "adjust_preset_timer": Use the action "press_preset_time_time_button" to adjust "variable_preset_timer" to 240 minutes (4 hours).
# 3. Feature "start_cooking": Use the action "press_start_button" to set "variable_start_running" to "on".

# Relevant user manual text:
# 1. "Press Menu/Cancel to choose Fast cook (symbol for fast cook), White rice (symbol for white rice), Congee (symbol for congee), Soup (symbol for soup), etc." is captured in the feature "select_cooking_mode".
# 2. "Choose a function you need, Press Preset/Timer to set the preset timer. The preset time is up to 24 hours." is captured in the feature "adjust_preset_timer".
# 3. "Press Start to start the cooking process" is captured in the feature "start_cooking".

# Mapped features in the provided code:
# - Feature "select_cooking_mode" models setting "variable_cooking_mode".
# - Feature "adjust_preset_timer" models setting "variable_preset_timer".
# - Feature "start_cooking" models setting "variable_start_running".

# Goal variable values:
# - Set "variable_cooking_mode" to "soup".
# - Set "variable_preset_timer" to 240.
# - Set "variable_start_running" to "on".

class ExtendedSimulator(Simulator):
    pass