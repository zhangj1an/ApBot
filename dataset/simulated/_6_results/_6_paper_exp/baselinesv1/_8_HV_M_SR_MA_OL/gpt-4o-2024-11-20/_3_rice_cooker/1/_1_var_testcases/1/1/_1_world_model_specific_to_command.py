# According to the user manual, the given implementation correctly models the relevant appliance feature. 
# To execute the command "Cook bean for 40 minutes, starting now", the sequence of features needed is:
# 1. Set the cooking mode to "Bean" using the feature "set_cooking_mode".
# 2. Set the cooking time to 40 minutes using the feature "adjust_cooking_time".
# 3. Start the appliance using the feature "start_appliance".
# These features correspond to "set_cooking_mode", "adjust_cooking_time", and "start_appliance" in the feature_list.

# Relevant user manual text:
# - Step 6, 7: "Press the 'Menu' button to select the desired function."
# - Step 8: "Press the 'Cooking time' button. Adjust the time by pressing 'Hr.' and 'Min.'"
# - Step 8: "Press the 'Start' button to begin cooking."

# Goal variable values:
# - Set variable_cooking_mode to "Bean".
# - Set variable_cooking_time_hr to 0 and variable_cooking_time_min to 40.
# - Set variable_start_running to "on".

class ExtendedSimulator(Simulator):
    pass