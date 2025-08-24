# The following user command can already be achieved with the existing code.
# Sequence of features needed to achieve this command:
# 1. "power_on_off": Turn on the washer.
# 2. "select_program": Use 'Soak' program.
# 3. "adjust_load_size": Set to medium load.
# 4. "adjust_wash_time": Set wash time to 14 minutes.
# 5. "adjust_rinse_times": Set rinse to twice.
# 6. "adjust_spin_time": Set spin to 5 minutes.
# 7. "start_pause_cycle": Start the washer.

# Relevant user manual text:
# - Step 1: Power on your washer. Press the ON/OFF button to power your wash on.
# - Press this button to select your desired washing program. Heavy, Gentle, Normal, Rapid, Soak.
# - Press this button to set your washing load size. Your water level throughout all steps in the cycle.
# - Continuously pressing the washing button to select washing time. (1-20 minutes, or no wash process)
# - Continuously pressing the rinse button to select rinse times. (1-3 times, or no rinse process)
# - Continuously pressing the spin button to select the spin time. (3-9 minutes or no wash process)
# - Step 5: Press the START/PAUSE button to start the washing cycle.

# feature_list references in given code:
# 1. "power_on_off"
# 2. "select_program"
# 3. "adjust_load_size"
# 4. "adjust_wash_time"
# 5. "adjust_rinse_times"
# 6. "adjust_spin_time"
# 7. "start_pause_cycle"

# Goal variable values for the user command:
# - variable_power_on_off: "on"
# - variable_program: "Soak"
# - variable_load_size: "2---medium"
# - variable_wash_time: 14
# - variable_rinse_times: 2
# - variable_spin_time: 5
# - variable_start_running: "on"

class ExtendedSimulator(Simulator):
    pass