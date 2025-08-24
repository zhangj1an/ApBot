# The current code provided already models the required appliance features accurately.
# To achieve the user command: "Set the rice cooker in glutinous rice mode with a preset time of 6 hours. Then start the machine."
# The following sequence of features is needed:

# 1. "select_cooking_program":
#    Actions: ["press_glutinous_rice_button"]
#    User manual text: "Cooking PROGRAM - Select cooking modes like jasmine rice, white rice, brown rice, glutinous rice, and so on."
#    Corresponding feature list: feature_list["select_cooking_program"]

# 2. "adjust_preset_time":
#    Actions: ["press_preset_button"]
#    User manual text: "Preset - When the cooking program is chosen, press the 'Preset' button to set the time for finishing cooking."
#    Corresponding feature list: feature_list["adjust_preset_time"]

# 3. "start_appliance":
#    Actions: ["press_start_button"]
#    User manual text: "Press 'Start' to begin cooking."
#    Corresponding feature list: feature_list["start_appliance"]

# Goal variable values to achieve this command:
# - Set variable_cooking_program to "glutinous_rice".
# - Set variable_preset_time to 360 minutes (6 hours in minutes).
# - Set variable_start_running to "on".

class ExtendedSimulator(Simulator): 
    # No additional features or variables are needed; the provided code already covers all requirements.
    pass