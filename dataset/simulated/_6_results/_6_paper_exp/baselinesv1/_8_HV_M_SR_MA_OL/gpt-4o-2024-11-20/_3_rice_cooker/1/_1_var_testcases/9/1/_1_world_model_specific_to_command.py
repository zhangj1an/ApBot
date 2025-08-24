# Based on the user manual, the current code accurately models the relevant tasks for using the appliance, as described in the given Simulator class and feature list. 
# Following is the sequence of features and steps needed to achieve the user command: 
# Command: "Set to cook bean for 1 hour and 10 minutes, then start."

# Sequence of Features:
# 1. "set_cooking_mode" to select "Bean" mode.
# 2. "adjust_cooking_time" to set cooking time to 1 hour and 10 minutes.
# 3. "start_appliance" to start the cooking process.

# Relevant referenced raw user manual text:
# - "Press the 'Menu' button to select the desired function."
# - "Press the 'Cooking time' button to adjust cooking time."
# - "Press the 'Start' button to begin cooking."
# - The manual specifies the process of setting hours and minutes for cooking time.
# - The described button mappings and their outcomes align with the existing feature_list provided.

# Associated feature names in current `feature_list`:
# - "set_cooking_mode"
# - "adjust_cooking_time"
# - "start_appliance"

# Goal variable values to achieve this command:
# - Set `variable_cooking_mode` to "Bean".
# - Set `variable_cooking_time_hr` to 1.
# - Set `variable_cooking_time_min` to 10.
# - Set `variable_start_running` to "on".

class ExtendedSimulator(Simulator):
    pass