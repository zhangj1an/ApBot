# The current code already models the necessary features to fulfill the user command "Defrost using time defrost for 20 minutes with 100% power, then start the appliance."
# Below is the relevant sequence of features needed, along with the related manual text, features, and goal variable values.

# Features sequence to achieve the command:
# 1. Use the "time_defrost" feature to set the defrost time and adjust the power level.
# 2. Use the "press_start_plus_30sec_button" to start the appliance.

# Relevant user manual text for "time_defrost":
# """
# 1. Press "TIME DEFROST", screen will display "dEF2".
# 2. Press number pads to input defrosting time. The effective time range is 00:01~99:99
# 3. The default microwave power is power level 3. If you want to change the power level, press "POWER" once, and the screen will display "PL 3", then press the number pad of the power level you wanted.
# 4. Press "START/+30SEC." to start defrosting. The remaining cooking time will be displayed.
# """
# Corresponds to feature_list["time_defrost"]

# Relevant user manual text for "start":
# """
# When cooking finishes, buzzer sounds five times and then turns back to waiting state.
# """
# Corresponds to feature_list["add_30_seconds"] for the start action.

# Feature list in the provided code:
# feature_list["time_defrost"] = [
#     {"step": 1, "actions": ["press_time_defrost_button"]},
#     {"step": 2, "actions": meta_actions_on_number, "variable": "variable_time_defrost", "comment": "requires parsing from variable_input_string"},
#     {"step": 3, "actions": ["press_power_button"]},
#     {"step": 4, "actions": meta_actions_on_number, "variable": "variable_power"},
#     {"step": 5, "actions": ["press_start_plus_30sec_button"]}
# ]
# feature_list["add_30_seconds"] = [
#     {"step": 1, "actions": ["press_start_plus_30sec_button"], "variable": "variable_time_cook_time", "comment": "Each press adds 30 seconds to the remaining cooking time"}
# ]

# Goal variable values for this command:
# 1. `variable_time_defrost` = "00:20:00" (20 minutes)
# 2. `variable_power` = "PL10" (100% power)
# 3. `variable_start_running` = "on" (Start the appliance)

class ExtendedSimulator(Simulator): 
    pass