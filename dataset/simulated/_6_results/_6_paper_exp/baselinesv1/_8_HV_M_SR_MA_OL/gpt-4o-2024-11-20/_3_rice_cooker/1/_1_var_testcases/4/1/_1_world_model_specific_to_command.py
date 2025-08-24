# Checking the user command against the given code and user manual:
# The user command is: "Prepare glutinous rice. Set the preset timer to 3 hours, then start."
# Based on the user manual and the given feature list, the command can be broken into these steps:
# 1. Select "Glutinous rice" cooking mode (feature: "set_cooking_mode").
# 2. Set the preset timer to 3 hours (feature: "set_preset_time").
# 3. Start the appliance (feature: "start_appliance").
# All necessary features and actions are already implemented in the provided code.
# User manual confirmations:
# To "Prepare glutinous rice":
# User manual mentions: "Select the Glutinous Rice function by pressing the Menu button (fig. 9)."
# The corresponding feature is modeled as "set_cooking_mode" in the code.
# To "Set the preset timer to 3 hours":
# User manual mentions: "To preset time for delayed cooking, press the Preset timer button."
# The corresponding feature is modeled as "set_preset_time" in the code.
# To "Start":
# User manual mentions: "Press the 'Start' button to start cooking."
# The corresponding feature is modeled as "start_appliance" in the code.
# Therefore, the code correctly models the relevant appliance features needed for this command.

# Sequence of features:
# 1. "set_cooking_mode": Use the "press_menu_button" to select "Glutinous rice".
# 2. "set_preset_time": Set the preset time to 3 hours using the "press_hr_button".
# 3. "start_appliance": Press the "Start" button to start cooking.

# Goal Variable Values:
# - variable_cooking_mode: "Glutinous rice"
# - variable_preset_time_hr: 3
# - variable_preset_time_min: 0
# - variable_start_running: "on"

class ExtendedSimulator(Simulator): 
    pass