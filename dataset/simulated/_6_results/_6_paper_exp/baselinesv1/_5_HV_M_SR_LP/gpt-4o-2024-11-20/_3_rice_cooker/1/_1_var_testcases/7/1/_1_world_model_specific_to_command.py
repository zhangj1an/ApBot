# Based on the user command, the given code already correctly models the relevant features.
# The sequence of features needed to achieve this command is as follows:
# 1. "set_cooking_mode" to select the "Reheat" mode using `press_menu_button`. 
#    User manual states: "Select the Reheat function by pressing the Menu button."
# 2. "adjust_cooking_time" to set the cooking time to 30 minutes using `press_min_button` and optionally `press_cooking_time_button`. 
#    User manual states: "Press the 'Cooking Time' button and adjust the time with the 'Minute' button."
# 3. "start_appliance" to start the rice cooker using `press_start_button`.
#    User manual states: "Press the Start button to start cooking."

# Features in code:
# - "set_cooking_mode" covers the selection of "Reheat" via the `press_menu_button`.
# - "adjust_cooking_time" allows configuring cooking hours and minutes via `press_cooking_time_button`, `press_hr_button`, and `press_min_button`.
# - "start_appliance" implements starting the appliance by pressing the `press_start_button`.

# Goal:
# - Set `variable_cooking_mode` to "Reheat".
# - Set `variable_cooking_time_hr` to 0.
# - Set `variable_cooking_time_min` to 30.
# - Set `variable_start_running` to "on".

class ExtendedSimulator(Simulator): 
    pass