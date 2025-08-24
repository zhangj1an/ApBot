# The provided code accurately models the features described in the user manual. 
# Here are the relevant user manual texts, the corresponding features in the code, and the explanation:

# User Command: Turn on the washer, use 'Soak' program for a medium load. Set wash to 14 minutes, rinse twice, and spin for 5 minutes. Start it.

# Sequence of Features Needed to Achieve This Command:
# 1. "power_on_off": Turn on the washer by pressing the ON/OFF button.
#    - User Manual: "Press the ON/OFF button to power your wash on."
#    - Feature: feature_list["power_on_off"]
# 2. "select_program": Select 'Soak' as the program using the program button.
#    - User Manual: "Press this button to select your desired washing program."
#    - Feature: feature_list["select_program"]
# 3. "adjust_load_size": Adjust load size to 'Medium' using the load size button.
#    - User Manual: "Press this button to set your washing load size."
#    - Feature: feature_list["adjust_load_size"]
# 4. "adjust_wash_time": Set washing time to 14 minutes using the wash button.
#    - User Manual: "Continuously pressing the washing button to select washing time."
#    - Feature: feature_list["adjust_wash_time"]
# 5. "adjust_rinse_times": Set rinse times to 2 using the rinse button.
#    - User Manual: "Continuously pressing the rinse button to select rinse times."
#    - Feature: feature_list["adjust_rinse_times"]
# 6. "adjust_spin_time": Set spin time to 5 minutes using the spin button.
#    - User Manual: "Continuously pressing the spin button to select the spin time."
#    - Feature: feature_list["adjust_spin_time"]
# 7. "start_pause_cycle": Start the cycle by pressing the START/PAUSE button.
#    - User Manual: "Press the START/PAUSE button to start the washing cycle."
#    - Feature: feature_list["start_pause_cycle"]

# Goal Variable Values:
# - Set variable_power_on_off to "on".
# - Set variable_program to "Soak".
# - Set variable_load_size to "2---medium".
# - Set variable_wash_time to 14.
# - Set variable_rinse_times to 2.
# - Set variable_spin_time to 5.
# - Set variable_start_running to "on".

class ExtendedSimulator(Simulator): 
    pass