# The current code sufficiently models all the relevant appliance features needed for the provided user command.

# Sequence of Features to Achieve User Command:
# 1. "power_on_off" - Switch ON the washer.
#    User manual: Step 1: Power on your washer. Press the ON/OFF button to power your wash on.
#    Feature list: feature_list["power_on_off"].
# 2. "select_program" - Select the "Heavy" washing program.
#    User manual: Press this button to select your desired washing program. Heavy, Gentle, Normal, Rapid, Soak.
#    Feature list: feature_list["select_program"].
# 3. "adjust_load_size" - Set load size to "1---small".
#    User manual: Press this button to set your washing load size. Your water level throughout all steps in the cycle.
#    Feature list: feature_list["adjust_load_size"].
# 4. "adjust_wash_time" - Set washing time to "5".
#    User manual: Continuously pressing the washing button to select washing time. (1-20 minutes, or no wash process).
#    Feature list: feature_list["adjust_wash_time"].
# 5. "adjust_rinse_times" - Set rinse times to "1".
#    User manual: Continuously pressing the rinse button to select rinse times. (1-3 times, or no rinse process).
#    Feature list: feature_list["adjust_rinse_times"].
# 6. "adjust_spin_time" - Set spin time to "8".
#    User manual: Continuously pressing the spin button to select the spin time. (3-9 minutes or no spin process).
#    Feature list: feature_list["adjust_spin_time"].
# 7. "start_pause_cycle" - Start the washing cycle.
#    User manual: Step 5: Press the START/PAUSE button to start the washing cycle.
#    Feature list: feature_list["start_pause_cycle"].

# Goal Variable Values:
# - variable_power_on_off: "on" (Washer is ON)
# - variable_program: "Heavy" (Heavy washing program)
# - variable_load_size: "1---small" (Small load size)
# - variable_wash_time: 5 (Washing for 5 minutes)
# - variable_rinse_times: 1 (Rinse one time)
# - variable_spin_time: 8 (Spin for 8 minutes)
# - variable_start_running: "on" (Start the washing cycle)

class ExtendedSimulator(Simulator): 
    pass