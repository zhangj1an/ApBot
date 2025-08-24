# The given code correctly models the relevant features required to fulfill the user command.
# Features in sequence to achieve this command:
# 1. "turn_power_on_off": Toggle the washer power to "on".
# 2. "set_program": Set the washing program to "Normal".
# 3. "set_load_size": Adjust the load size to "medium".
# 4. "adjust_wash_time": Set the wash time to 11 minutes.
# 5. "adjust_rinse_times": Set the rinse times to 2.
# 6. "adjust_spin_time": Set the spin time to 3 minutes.
# 7. "start_pause_operation": Start the washing operation by pressing "start".

# Relevant user manual text references:
# - "Step 1: Power on your washer. Press the ON/OFF button to power your wash on." - Feature: "turn_power_on_off".
# - "Press this button to select your desired washing program. Heavy, Gentle, Normal, Rapid, Soak." - Feature: "set_program".
# - "Press this button to set your washing load size. Your water level throughout all steps in the cycle." - Feature: "set_load_size".
# - "Continuously pressing the washing button to select washing time. (1-20 minutes, or no wash process)" - Feature: "adjust_wash_time".
# - "Continuously pressing the rinse button to select rinse times. (1-3 times, or no rinse process)" - Feature: "adjust_rinse_times".
# - "Continuously pressing the spin button to select the spin time. (3-9 minutes or no spin process)" - Feature: "adjust_spin_time".
# - "Step 5: Press the START/PAUSE button to start the washing cycle." - Feature: "start_pause_operation".

# Goal variable values to achieve this command:
# - Set variable_power_on_off to "on".
# - Set variable_program to "Normal".
# - Set variable_load_size to "2---medium".
# - Set variable_wash_time to 11 minutes.
# - Set variable_rinse_times to 2 times.
# - Set variable_spin_time to 3 minutes.
# - Set variable_start_running to "on".

class ExtendedSimulator(Simulator):
    pass