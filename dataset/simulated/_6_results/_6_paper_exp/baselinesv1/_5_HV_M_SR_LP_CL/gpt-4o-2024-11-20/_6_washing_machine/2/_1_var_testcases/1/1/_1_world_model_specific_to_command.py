# The sequence of features needed to achieve the command:
# 1. power_on_off
# 2. select_program
# 3. adjust_load_size
# 4. adjust_wash_time
# 5. adjust_rinse_times
# 6. adjust_spin_time
# 7. start_pause_cycle

# Raw user manual text describing the relevant features:
# Power On: "Step 1: Power on your washer. Press the ON/OFF button to power your wash on."
# Select Program: "Press this button to select your desired washing program. Heavy, Gentle, Normal, Rapid, Soak."
# Adjust Load Size: "Press this button to set your washing load size."
# Adjust Wash Time: "Continuously pressing the washing button to select washing time. (1-20 minutes, or no wash process)"
# Adjust Rinse Times: "Continuously pressing the rinse button to select rinse times. (1-3 times, or no rinse process)"
# Adjust Spin Time: "Continuously pressing the spin button to select the spin time. (3-9 minutes or no spin process)"
# Start Cycle: "Step 5: Press the START/PAUSE button to start the washing cycle."

# Feature List Names in the Given Code:
# - power_on_off
# - select_program
# - adjust_load_size
# - adjust_wash_time
# - adjust_rinse_times
# - adjust_spin_time
# - start_pause_cycle

# Goal variable values to achieve the command:
# - variable_power_on_off: "on"
# - variable_program: "Heavy"
# - variable_load_size: "3---large"
# - variable_wash_time: 15
# - variable_rinse_times: 2
# - variable_spin_time: 6
# - variable_start_running: "on"

class ExtendedSimulator(Simulator): 
    pass