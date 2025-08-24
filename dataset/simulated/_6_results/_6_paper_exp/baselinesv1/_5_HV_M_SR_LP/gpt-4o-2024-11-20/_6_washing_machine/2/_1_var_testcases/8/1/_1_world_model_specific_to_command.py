# The current code correctly models the relevant appliance features described in the user manual to achieve the user command.

# Sequence of features needed to achieve the user command:
# 1. "power_on_off" to power on the washer.
# 2. "select_program" to set the desired program, "Normal" in this case.
# 3. "adjust_load_size" to set the load size, "2---medium" in this case.
# 4. "adjust_wash_time" to set the wash time to 11 minutes.
# 5. "adjust_rinse_times" to set the rinse times to 2.
# 6. "adjust_spin_time" to set the spin time to 3 minutes.
# 7. "start_pause_cycle" to start the washing cycle.

# Relevant raw user manual text:
# 1. "Step 1: Power on your washer. Press the ON/OFF button to power your wash on."
# 2. "Press this button to select your desired washing program. Heavy, Gentle, Normal, Rapid, Soak."
# 3. "Press this button to set your washing load size. Your water level throughout all steps in the cycle."
# 4. "Continuously pressing the washing button to select washing time. (1-20 minutes, or no wash process)"
# 5. "Continuously pressing the rinse button to select rinse times. (1-3 times, or no rinse process)"
# 6. "Continuously pressing the spin button to select the spin time. (3-9 minutes or no spin process)"
# 7. "Step 5: Press the START/PAUSE button to start the washing cycle."

# Corresponding feature_list names:
# - "power_on_off"
# - "select_program"
# - "adjust_load_size"
# - "adjust_wash_time"
# - "adjust_rinse_times"
# - "adjust_spin_time"
# - "start_pause_cycle"

# Goal variable values to achieve this command:
# - variable_power_on_off = "on"
# - variable_program = "Normal"
# - variable_load_size = "2---medium"
# - variable_wash_time = 11
# - variable_rinse_times = 2
# - variable_spin_time = 3
# - variable_start_running = "on"

class ExtendedSimulator(Simulator): 
    pass