# The current code accurately models the described user command based on the user manual. 
# To achieve the command, we need the following sequence of features: 
# 1. "select_cooking_program" with the goal of setting `variable_cooking_program` to "jasmine_rice".
# 2. "adjust_preset_time" with the goal of setting `variable_preset_time` to 240 minutes (4 hours).
# 3. "start_running" with the goal of setting `variable_start_running` to "on".

# Relevant user manual text:
# - "Press [Cooking Program] buttons directly (e.g., Jasmine Rice, White Rice, etc.) to select the cooking program."
# - "Press 'Preset' button to adjust the time for finishing cooking. Set the time in minutes, up to 24 hours."
# - "Press 'Start' button to start cooking."

# Corresponding feature list:
# - feature_list["select_cooking_program"]
# - feature_list["adjust_preset_time"]
# - feature_list["start_running"]

# Goal variable values:
# - `variable_cooking_program`: "jasmine_rice"
# - `variable_preset_time`: 240
# - `variable_start_running`: "on"

class ExtendedSimulator(Simulator):
    pass