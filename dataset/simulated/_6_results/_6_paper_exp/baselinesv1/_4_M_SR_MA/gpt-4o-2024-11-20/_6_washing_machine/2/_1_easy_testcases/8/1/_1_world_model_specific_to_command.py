# The user command is as follows:
# Switch on the washer manual, set 'Normal' program with a medium load. Set wash to 11 minutes, rinse two times, and spin for 3 minutes. Get it going.
# 
# After carefully reviewing the provided code and user manual, I confirm that the existing code models all the features correctly based on the user manual instructions. Each required feature and step is properly included, and no variables or features are omitted.
# 
# The sequence of features required to achieve the user command is as follows:
# 1. "power_on_off" to turn on the washer.
# - User manual: "Step 1: Power on your washer. Press the ON/OFF button to power your wash on."
# - Feature: feature_list["power_on_off"]
#
# 2. "select_program" to set 'Normal' program.
# - User manual: "Press this button to select your desired washing program. Heavy, Gentle, Normal, Rapid, Soak."
# - Feature: feature_list["select_program"]
# 
# 3. "adjust_load_size" to set the load size to 'medium'.
# - User manual: "Press this button to set your washing load size. Your water level throughout all steps in the cycle."
# - Feature: feature_list["adjust_load_size"]
# 
# 4. "adjust_wash_time" to set wash time to 11 minutes.
# - User manual: "Continuously pressing the washing button to select washing time. (1-20 minutes, or no wash process)"
# - Feature: feature_list["adjust_wash_time"]
# 
# 5. "adjust_rinse_times" to set rinse times to 2.
# - User manual: "Continuously pressing the rinse button to select rinse times. (1-3 times, or no rinse process)"
# - Feature: feature_list["adjust_rinse_times"]
# 
# 6. "adjust_spin_time" to set spin time to 3 minutes.
# - User manual: "Continuously pressing the spin button to select the spin time. (3-9 minutes or no spin process)"
# - Feature: feature_list["adjust_spin_time"]
# 
# 7. "start_pause_cycle" to start the washing process.
# - User manual: "Press the START/PAUSE button to start the washing cycle."
# - Feature: feature_list["start_pause_cycle"]
#
# Final goal variable values to achieve the user command:
# - variable_power_on_off: "on"
# - variable_program: "Normal"
# - variable_load_size: "2---medium"
# - variable_wash_time: 11
# - variable_rinse_times: 2
# - variable_spin_time: 3
# - variable_start_running: "on"

class ExtendedSimulator(Simulator): 
    pass