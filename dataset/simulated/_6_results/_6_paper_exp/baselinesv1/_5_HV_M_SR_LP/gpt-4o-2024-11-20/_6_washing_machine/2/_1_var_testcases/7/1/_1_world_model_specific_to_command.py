# User command is to turn the machine on, select 'Gentle' for a large load size, set wash time to 18 minutes, rinse 3 times, spin for 7 minutes, and start the cycle.

# The sequence of features required is as follows:
# 1. "power_on_off": Turn the machine on.
# 2. "select_program": Select the 'Gentle' washing program.
# 3. "adjust_load_size": Adjust the load size to '3---large'.
# 4. "adjust_wash_time": Set the wash time to 18 minutes.
# 5. "adjust_rinse_times": Set rinse to 3 times.
# 6. "adjust_spin_time": Set spin time to 7 minutes.
# 7. "start_pause_cycle": Start the washing cycle.

# Quoting relevant user manual descriptions:
# - "Step 1: Power on your washer. Press the ON/OFF button to power your wash on."
# - "Press this button to select your desired washing program. Heavy, Gentle, Normal, Rapid, Soak."
# - "Press this button to set your washing load size. Your water level throughout all steps in the cycle."
# - "Continuously pressing the washing button to select washing time. (1-20 minutes, or no wash process)"
# - "Continuously pressing the rinse button to select rinse times. (1-3 times, or no rinse process)"
# - "Continuously pressing the spin button to select the spin time. (3-9 minutes or no spin process)."
# - "Step 5: Press the START/PAUSE button to start the washing cycle."

# The provided feature_list already models these steps accurately:
# - "power_on_off": Models turning the machine on.
# - "select_program": Models selecting washing programs (e.g., 'Gentle').
# - "adjust_load_size": Models selecting load sizes (e.g., '3---large').
# - "adjust_wash_time": Models adjusting wash time (e.g., 18 minutes).
# - "adjust_rinse_times": Models adjusting rinse times (e.g., 3 times).
# - "adjust_spin_time": Models adjusting spin time (e.g., 7 minutes).
# - "start_pause_cycle": Models starting the cycle.

# The corresponding goal variable values to achieve the command are as follows:
# - variable_power_on_off: "on"
# - variable_program: "Gentle"
# - variable_load_size: "3---large"
# - variable_wash_time: 18
# - variable_rinse_times: 3
# - variable_spin_time: 7
# - variable_start_running: "on"

class ExtendedSimulator(Simulator): 
    pass