# The given code correctly models the operation of setting the mode, adjusting the preset timer, and starting the machine. 
# Below are the relevant features, quoted from the user manual and the feature list:

# User Manual Raw Text Describing Features:
# - "Press Menu/Cancel to choose Fast cook, White rice, Congee, Soup, Cake, Keep warm." (Selecting Cooking Mode)
# - "Choose a function you need, Press Preset/Timer to set the preset timer. With each press, the time increases by 15 minutes." (Adjusting Preset Timer)
# - "Press Start to start the cooking process." (Start Cooking)

# Features from Code:
# - "select_cooking_mode": Enables setting the mode to Cake.
# - "adjust_preset_timer": Adjusts the timer to 7 hours (420 minutes via step increments).
# - "start_cooking": Starts the appliance.

# Feature List:
# - select_cooking_mode
# - adjust_preset_timer
# - start_cooking

# Goal Variable Values:
# - variable_cooking_mode: "cake"
# - variable_preset_timer: 420 (7 hours in minutes)
# - variable_start_running: "on"

class ExtendedSimulator(Simulator): 
    pass