# The given code accurately represents the required features and variables from the user manual to achieve the user command. 
# The relevant features to achieve the command are:
# 1. Select the cooking program for glutinous rice: This corresponds to "select_cooking_program" from feature_list.
#    User manual text: "Press 'Glutinous Rice' button to select glutinous rice cooking program."
# 2. Set a preset time of 6 hours: This corresponds to "adjust_preset_time" from feature_list.
#    User manual text: "Press the 'Preset' button to set the time for finishing cooking."
# 3. Start the rice cooker: This corresponds to "start_running" from feature_list.
#    User manual text: "Press 'Start' button to start the rice cooker."

# Goal variable values to achieve this command:
# - Set variable_cooking_program to "glutinous_rice".
# - Set variable_preset_time to 360 (6 hours in minutes).
# - Set variable_start_running to "on".

class ExtendedSimulator(Simulator):
    pass