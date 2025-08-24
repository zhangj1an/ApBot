# The given simulator already contains the required features and variables to fulfill the user command. The steps for the user command to "Set the mode to soup, set timer to 3 hours, and start the machine" are correctly captured in the existing feature and variables.

# Sequence of features/actions needed to achieve the command from the user manual:
# 1. To set the mode to soup:
# - Use feature_list["select_cooking_mode"] and action "press_menu_cancel_button".
# - Quote from the manual: "Press Menu/Cancel to choose Congee (bowl symbol) or Soup (steam symbol)."
#
# 2. To set the timer to 3 hours (or 180 minutes):
# - Use feature_list["adjust_preset_timer"] and action "press_preset_time_time_button".
# - Quote from the manual: "Press Preset/Timer to adjust the timer. With each press, the time increases by 15 minutes."
#
# 3. To start the machine:
# - Use feature_list["start_cooking"] and action "press_start_button".
# - Quote from the manual: "Press Start to start the cooking process."

# Goal variable values to achieve the command:
# 1. Set `variable_cooking_mode` to "soup".
# 2. Set `variable_preset_timer` to 180 (equivalent to 3 hours).
# 3. Set `variable_start_running` to "on".

class ExtendedSimulator(Simulator):
    pass