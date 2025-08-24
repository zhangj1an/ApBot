# The current code accurately models the necessary features to achieve the user command.
# Sequence of features needed to achieve the command:
# 1. "set_cooking_mode": Set the cooking mode to "Bean".
# 2. "adjust_cooking_time": Adjust the cooking time to 1 hour and 20 minutes.
# 3. "start_appliance": Start the appliance.

# Raw user manual text describing the relevant features:
# - "6: Press the 'Cooking time' button. 7: Press the 'Menu' button to select the desired function."
# - "Press the 'Start' button."
# - "Cooking function / Estimated cooking time: Bean / 90 minutes ... Time regulation: 40 minutes - 2 hours."

# Feature list names corresponding to the described features:
# - "set_cooking_mode"
# - "adjust_cooking_time"
# - "start_appliance"

# Goal variable values to achieve this command:
# - Set `variable_cooking_mode` to "Bean".
# - Set `variable_cooking_time_hr` to 1.
# - Set `variable_cooking_time_min` to 20.
# - Set `variable_start_running` to "on".

class ExtendedSimulator(Simulator): 
    pass