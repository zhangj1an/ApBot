# The current code accurately models the features described in the user manual. 
# Based on the user command, here are the sequence of features needed:
# 
# 1. Feature: "power_on_off" from feature_list
# User Manual: Step 1: Power on your washer. Press the ON/OFF button to power your wash on.
#
# 2. Feature: "select_program" from feature_list
# User Manual: Press this button to select your desired washing program. Heavy, Gentle, Normal, Rapid, Soak.
#
# 3. Feature: "adjust_load_size" from feature_list
# User Manual: Press this button to set your washing load size. Your water level throughout all steps in the cycle. 
#
# 4. Feature: "adjust_wash_time" from feature_list
# User Manual: Continuously pressing the washing button to select washing time. (1-20 minutes, or no wash process).
#
# 5. Feature: "adjust_rinse_times" from feature_list
# User Manual: Continuously pressing the rinse button to select rinse times. (1-3 times, or no rinse process).
#
# 6. Feature: "adjust_spin_time" from feature_list
# User Manual: Continuously pressing the spin button to select the spin time. (3-9 minutes or no process).
#
# 7. Feature: "start_pause_cycle" from feature_list
# User Manual: Step 5: Press the START/PAUSE button to start the washing cycle.
#
# The goal variable values to achieve this command:
# variable_power_on_off: "on"
# variable_program: "Normal"
# variable_load_size: "2---medium"
# variable_wash_time: 11
# variable_rinse_times: 2
# variable_spin_time: 3
# variable_start_running: "on"

class ExtendedSimulator(Simulator): 
    pass