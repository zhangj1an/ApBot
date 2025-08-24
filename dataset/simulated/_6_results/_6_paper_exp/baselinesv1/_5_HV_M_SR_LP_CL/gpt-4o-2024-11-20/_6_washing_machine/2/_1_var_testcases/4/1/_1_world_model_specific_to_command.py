# The given code properly includes all features and variables explicitly mentioned in the user manual to achieve the command.
# User manual and relevant quoted text:
# - "Step 1: Power on your washer. Press the ON/OFF button to power your wash on." - (feature_list["power_on_off"])
# - "Press this button to select your desired washing program." - (feature_list["select_program"])
# - "Press this button to set your washing load size." - (feature_list["adjust_load_size"])
# - "Continuously pressing the washing button to select washing time. (1-20 minutes, or no wash process)" - (feature_list["adjust_wash_time"])
# - "Continuously pressing the rinse button to select rinse times. (1-3 times, or no rinse process)" - (feature_list["adjust_rinse_times"])
# - "Continuously pressing the spin button to select the spin time. (3-9 minutes or no spin process)" - (feature_list["adjust_spin_time"])
# - "Step 5: Press the START/PAUSE button to start the washing cycle." - (feature_list["start_pause_cycle"])

# Sequence of features required to achieve the command:
# 1. power_on_off: Switch on the washer by setting variable_power_on_off to "on".
# 2. select_program: Select "Rapid" program by setting variable_program to "Rapid".
# 3. adjust_load_size: Adjust the load size to "3---large" (large) by setting variable_load_size.
# 4. adjust_wash_time: Set wash time to 8 minutes by setting variable_wash_time.
# 5. adjust_rinse_times: Set rinse times to 2 by setting variable_rinse_times.
# 6. adjust_spin_time: Set spin time to 3 minutes by setting variable_spin_time.
# 7. start_pause_cycle: Start the cycle by setting variable_start_running to "on".

# Goal variable values to achieve the command:
# variable_power_on_off = "on"
# variable_program = "Rapid"
# variable_load_size = "3---large"
# variable_wash_time = 8
# variable_rinse_times = 2
# variable_spin_time = 3
# variable_start_running = "on"

class ExtendedSimulator(Simulator):
    pass