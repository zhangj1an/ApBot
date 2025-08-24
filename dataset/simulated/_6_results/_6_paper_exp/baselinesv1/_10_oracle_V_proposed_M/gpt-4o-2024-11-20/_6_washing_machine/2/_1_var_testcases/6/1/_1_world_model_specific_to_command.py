# The provided code already models the necessary appliance features and variables accurately to achieve the given command.
# Below are the steps needed to achieve the command with the corresponding features.

# 1. Power up the washer: This corresponds to feature 'turn_power_on_off'.
#    User manual: Step 1: Power on your washer. Press the ON/OFF button to power your wash on.
#    Feature list: "turn_power_on_off"

# 2. Select washing program 'Heavy': This corresponds to feature 'set_program'.
#    User manual: Press the program button to select your desired washing program. Heavy, Gentle, Normal, Rapid, Soak.
#    Feature list: "set_program"

# 3. Set load size to small: This corresponds to feature 'set_load_size'.
#    User manual: Press this button to set your washing load size. Load size values: 1---small, 2---medium, 3---large.
#    Feature list: "set_load_size"

# 4. Set wash time to 5 minutes: This corresponds to feature 'adjust_wash_time'.
#    User manual: Continuously pressing the washing button to select washing time. (1-20 minutes, or no wash process)
#    Feature list: "adjust_wash_time"

# 5. Set rinse to 1 time: This corresponds to feature 'adjust_rinse_times'.
#    User manual: Continuously pressing the rinse button to select rinse times. (1-3 times, or no rinse process)
#    Feature list: "adjust_rinse_times"

# 6. Set spin time to 8 minutes: This corresponds to feature 'adjust_spin_time'.
#    User manual: Continuously pressing the spin button to select the spin time. (3-9 minutes or no wash process)
#    Feature list: "adjust_spin_time"

# 7. Start the washing process: This corresponds to feature 'start_pause_operation'.
#    User manual: Step 5: Press the START/PAUSE button to start the washing cycle.
#    Feature list: "start_pause_operation"

# Setting the goal variable values for the command:
# - Set variable_power_on_off to "on"
# - Set variable_program to "Heavy"
# - Set variable_load_size to "1---small"
# - Set variable_wash_time to 5
# - Set variable_rinse_times to 1
# - Set variable_spin_time to 8
# - Set variable_start_running to "on"

class ExtendedSimulator(Simulator): 
    pass