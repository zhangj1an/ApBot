# The provided code correctly models the appliance's relevant features and variables to achieve the user command.
# Below are the sequence of features needed to achieve the command, relevant raw user manual text, and feature_list names.

# Sequence of features needed:
# 1. Turn on the washing machine.
#    Feature: "power_on_off"
#    Action: "press_power_button"
#    User manual: Press this button to switch power on and off.

# 2. Set the washing machine to the "Energy Save" program.
#    Feature: "adjust_program"
#    Action: "press_program_button"
#    User manual: Selects programs. The program changes each time the button is pressed.
#    Programs: P8. Energy Save

# 3. Set the water level to 30L.
#    Feature: "adjust_water_level"
#    Action: "press_water_level_button"
#    User manual: You can set the amount of water each time you press the Water Level button in a range from 25 to 59 L.

# 4. Set the wash time to 9 minutes.
#    Feature: "adjust_wash_time"
#    Action: "press_wash_button"
#    User manual: Changes the washing time. The washing time can be set between 3 and 18 minutes.

# 5. Set the spin time to 6 minutes.
#    Feature: "adjust_spin_time"
#    Action: "press_spin_button"
#    User manual: You can set the spin time each time you press the Spin button in a range of 1 to 9 minutes.

# 6. Set the rinse type to "Normal Rinse 2 times".
#    Feature: "adjust_rinse_type"
#    Action: "press_rinse_button"
#    User manual: You can set the number and type of rinses by pressing the Rinse button.
#    Options: Normal Rinse 2 times, Water-Injection Rinse 2 times, no rinsing, Normal Rinse 1 time, Water-Injection Rinse 1 time.

# 7. Start the machine running.
#    Feature: "start_pause"
#    Action: "press_start_pause_button"
#    User manual: Starts and pauses operation.

# Goal variable values to achieve the user command:
# - variable_power_on_off: "on"
# - variable_program: "P8 (Energy Save)"
# - variable_water_level: 30
# - variable_washing_time: 9
# - variable_spin_time: 6
# - variable_rinse_type: "Normal Rinse 2 times"
# - variable_start_running: "start"

class ExtendedSimulator(Simulator): 
    pass