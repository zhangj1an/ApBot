# The user command is to set the mode to soup, set timer to 6 hours, and start the machine.
# Based on the provided user manual, the relevant features and variables are already well-modeled 
# by the provided code.

# Here is the list of steps and features used for the command:
# 1. Set the mode to soup:
#    - Feature: "select_cooking_mode"
#      - Action: "press_menu_cancel_button"
#      - Variable: "variable_cooking_mode"
#      - User manual reference: "Press Menu/Cancel to choose... Soup (steam symbol)..."
#
# 2. Set timer to 6 hours:
#    - Feature: "adjust_preset_timer"
#      - Action: "press_preset_time_time_button"
#      - Variable: "variable_preset_timer"
#      - User manual reference: "Choose a function you need, press Preset/Timer to set the preset timer..."
#
# 3. Start the machine:
#    - Feature: "start_cooking"
#      - Action: "press_start_button"
#      - Variable: "variable_start_running"
#      - User manual reference: "Press Start to start cooking..."

# The provided code correctly models these features:
# - "select_cooking_mode"
# - "adjust_preset_timer"
# - "start_cooking"

# Goal variable values to achieve the command:
# - variable_cooking_mode: "soup"
# - variable_preset_timer: 360 (6 hours in minutes)
# - variable_start_running: "on"

class ExtendedSimulator(Simulator):
    pass