# The current code correctly models the relevant appliance feature to achieve the user command.
# Sequence of features needed to achieve this command:
# 1. "select_cooking_mode": Set the mode to "soup" by adjusting the variable_cooking_mode.
# 2. "adjust_preset_timer": Adjust the preset timer to 4 hours (240 minutes) by modifying the variable_preset_timer.
# 3. "start_cooking": Start the machine by setting variable_start_running to "on".

# Raw user manual text describing the relevant features:
# 1. "Press Menu/Cancel to select Congee (bowl symbol) or Soup (steam symbol)."
# 2. "Choose a function you need. Press Preset/Timer to set the preset timer."
#    "→ The preset timer indicator blinks."
#    "→ With each press, the time increases by 15 minutes."
#    "→ Long press Preset/Timer to quickly adjust the time."
# 3. "Press Start to confirm. The rice cooker starts working at the selected mode."
#    "→ The preset timer indicator is on."
#    "→ The rice cooker starts countdown until the cooking process is finished."

# Relevant feature list names in the given code:
# 1. "select_cooking_mode"
# 2. "adjust_preset_timer"
# 3. "start_cooking"

# Goal variable values to achieve this command:
# - Set variable_cooking_mode to "soup".
# - Set variable_preset_timer to 240 (4 hours).
# - Set variable_start_running to "on".

class ExtendedSimulator(Simulator):
    pass