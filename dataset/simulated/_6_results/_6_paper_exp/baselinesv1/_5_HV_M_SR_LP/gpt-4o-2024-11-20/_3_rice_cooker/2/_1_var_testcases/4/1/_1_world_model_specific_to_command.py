# The provided code seems to accurately model the required appliance features. The following operations from the user command can be mapped to the modeled features:
# 1. Set mode to white rice --> Feature: "select_cooking_mode", action: "press_menu_cancel_button".
# 2. Set timer for dinner in two hours --> Feature: "adjust_preset_timer", action: "press_preset_time_time_button".
# 3. Start the machine --> Feature: "start_cooking", action: "press_start_button".

# Relevant user manual text:
# - "Press Menu/Cancel to choose Fast cook, White rice, Congee, Soup, Cake, Keep warm." [Feature: select_cooking_mode]
# - "Choose a function you need, press Preset/Timer to set the preset time, timer up to 24 hours in 15-minute increments." [Feature: adjust_preset_timer]
# - "Press Start to start the cooking process." [Feature: start_cooking]

# Feature list names in the provided code:
# - "select_cooking_mode"
# - "adjust_preset_timer"
# - "start_cooking"

# Goal variable values to achieve this command:
# - Set `variable_cooking_mode` to "white rice".
# - Set `variable_preset_timer` to 120 (minutes for 2 hours).
# - Set `variable_start_running` to "on".

class ExtendedSimulator(Simulator): 
    pass