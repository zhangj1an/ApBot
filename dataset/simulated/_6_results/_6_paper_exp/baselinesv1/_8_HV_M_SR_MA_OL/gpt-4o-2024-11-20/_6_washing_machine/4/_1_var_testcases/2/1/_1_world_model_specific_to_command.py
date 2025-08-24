# The relevant features and variables exist suitably for the user command according to the provided user manual and code.
# Below is the sequence of features needed to achieve the command, the corresponding features as per the feature_list, and the goal variable values.

# Sequence of features needed:
# 1. Turn on the washing machine (Feature: "power_on_off").
# 2. Set the washing program to Speedy (Feature: "adjust_program").
# 3. Adjust the water level to 35 L (Feature: "adjust_water_level").
# 4. Set the washing time to 6 minutes (Feature: "adjust_wash_time").
# 5. Set no rinse type (Feature: "adjust_rinse_type").
# 6. Start the washing machine (Feature: "start_pause").

# Relevant user manual excerpts:
# - Power On/Off: "Press this button to switch power on and off."
# - Program Selection: "Selects programs. The program changes each time the button is pressed."
# - Water Level: "You can set the amount of water each time you press the Water Level button in a range from 25 to 59 L."
# - Washing Time: "The washing time can be set between 3 and 18 minutes."
# - Rinse Type: "Each time you press the Rinse button the setting changes in sequence, from Normal Rinse 2 times, Water-Injection Rinse 2 times, no rinsing, Normal Rinse 1 time, Water-Injection Rinse 1 time."
# - Start/Pause: "Starts and pauses operation."

# Goal variable values:
# variable_power_on_off = "on"
# variable_program = "P3 (Speedy)"
# variable_water_level = 35
# variable_washing_time = 6
# variable_rinse_type = "No rinsing"
# variable_start_running = "start"

class ExtendedSimulator(Simulator):
    pass