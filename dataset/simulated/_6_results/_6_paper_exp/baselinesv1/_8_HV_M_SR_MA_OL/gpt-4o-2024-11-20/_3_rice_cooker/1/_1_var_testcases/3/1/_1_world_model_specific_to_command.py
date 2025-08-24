# The current Simulator code accurately models the relevant appliance features to achieve the command: "Cook bean in the rice cooker, set cooking time to 1 hour and 20 minutes, then start."
# Sequence of features needed:
# 1. "set_cooking_mode" to select "Bean".
# 2. "adjust_cooking_time" to set cooking time to 1 hour and 20 minutes (variable_cooking_time_hr = 1 and variable_cooking_time_min = 20).
# 3. "start_appliance" to start cooking (variable_start_running = "on").

# Relevant raw user manual text describing the features:
# - "Press the 'Menu' button to select the desired function." (Describes "set_cooking_mode" feature).
# - "Press the 'Cooking time' button." -> "Press the 'Hr.' button to set the hour unit." -> "Press the 'Min.' button to set the minute unit." (Describes "adjust_cooking_time" feature for setting hour and minute values).
# - "Press the 'Start' button." (Describes "start_appliance" feature).

# Mapped feature_list names:
# - feature_list["set_cooking_mode"]: To set the cooking mode to "Bean".
# - feature_list["adjust_cooking_time"]: To adjust the cooking time to 1 hour and 20 minutes.
# - feature_list["start_appliance"]: To start the cooking process.

# Goal variable values to achieve the command:
# variable_cooking_mode = "Bean"
# variable_cooking_time_hr = 1
# variable_cooking_time_min = 20
# variable_start_running = "on"

class ExtendedSimulator(Simulator): 
    pass