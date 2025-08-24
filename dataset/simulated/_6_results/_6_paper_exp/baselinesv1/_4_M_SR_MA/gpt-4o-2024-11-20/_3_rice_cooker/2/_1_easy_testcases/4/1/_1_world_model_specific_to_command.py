# The provided simulator code correctly models the appliance features relevant to the user command.
# The process to set the mode to white rice, set a preset time for two hours, and start the appliance is accurately represented.

# Sequence of features to achieve this user command:
# 1. "select_cooking_mode" feature: Use the press_menu_cancel_button action to set variable_cooking_mode to "white rice".
# 2. "adjust_preset_timer" feature: Use the press_preset_time_time_button action to set variable_preset_timer to 120 minutes (2 hours).
# 3. "start_cooking" feature: Use the press_start_button action to set variable_start_running to "on".

# Relevant user manual text:
# - "Press Menu/Cancel to choose Fast cook, White rice, Congee, Soup, Cake, Keep warm."
# - "Press Preset/Timer to set the preset timer. The preset time is up to 24 hours."
# - "Press Start to start the cooking process."
#
# Feature list names in the given code:
# - "select_cooking_mode"
# - "adjust_preset_timer"
# - "start_cooking"

# Goal variable values to achieve this command:
# - Set variable_cooking_mode to "white rice".
# - Set variable_preset_timer to 120.
# - Set variable_start_running to "on".

class ExtendedSimulator(Simulator):
    pass