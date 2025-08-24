# The given code correctly models the relevant appliance features described in the user manual.
# For the requested user command, the relevant features are:
# 1. Power Control: Turn on the washing machine.
#    User manual: "Press this button to switch power on and off."
#    Feature: feature_list["power_control"]
# 2. Select Program: Set to Soak mode.
#    User manual: "Selects programs. The program changes each time the button is pressed."
#    Feature: feature_list["select_program"]
# 3. Adjust Washing Time: Set washing time to 18 minutes.
#    User manual: "Changes the washing time. The washing time can be set between 3 and 18 minutes."
#    Feature: feature_list["adjust_washing_time"]
# 4. Adjust Water Level: Set water level to 30 L.
#    User manual: "You can set the amount of water each time you press the Water Level button in a range from 25 to 59 L."
#    Feature: feature_list["adjust_water_level"]
# 5. Adjust Spin Time: Spin for 3 minutes.
#    User manual: "You can set the spin time each time you press the Spin button in a range of 1 to 9 minutes."
#    Feature: feature_list["adjust_spin_time"]
# 6. Adjust Rinse Type: Set rinse type to "Normal Rinse 2 times."
#    User manual: "You can set the number and type of rinses by pressing the Rinse button."
#    Feature: feature_list["adjust_rinse_type"]
# 7. Start Machine Running: Start the machine running.
#    User manual: "Starts and pauses operation."
#    Feature: feature_list["start_pause_control"]

# The code models all the corresponding variables and features required for the task:
# - variable_power_on_off
# - variable_program
# - variable_washing_time
# - variable_water_level
# - variable_spin_time
# - variable_rinse_type
# - variable_start_running

# Sequence of features needed to achieve this command:
# 1. feature_list["power_control"]: Turn the washing machine on.
# 2. feature_list["select_program"]: Set the program to "P5 (Soak)."
# 3. feature_list["adjust_washing_time"]: Set the washing time to 18 minutes.
# 4. feature_list["adjust_water_level"]: Adjust the water level to 30 L.
# 5. feature_list["adjust_spin_time"]: Adjust the spin time to 3 minutes.
# 6. feature_list["adjust_rinse_type"]: Set the rinse type to "Normal Rinse 2 times."
# 7. feature_list["start_pause_control"]: Start the machine running.

# The following goal variable values achieve this command:
# - variable_power_on_off = "on"
# - variable_program = "P5 (Soak)"
# - variable_washing_time = 18
# - variable_water_level = 30
# - variable_spin_time = 3
# - variable_rinse_type = "Normal Rinse 2 times"
# - variable_start_running = "start"

class ExtendedSimulator(Simulator):
    pass