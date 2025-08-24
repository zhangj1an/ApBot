# The user manual is correctly modeled in the existing code, and all required features and variables are already present to achieve the user command. 
# Below is the list of sequences of features needed to execute this command, along with the associated user manual text and feature names.

# Sequence of features:
# 1. Turn on the washing machine: Use the "turn_power_on_off" feature.
#    User manual text: "Step 1: Power on your washer. Press the ON/OFF button to power your wash on."
#    Feature name: "turn_power_on_off"
#
# 2. Choose the "Soak" program: Use the "set_program" feature.
#    User manual text: "Press this button to select your desired washing program. Heavy, Gentle, Normal, Rapid, Soak."
#    Feature name: "set_program"
#
# 3. Set the load size to "medium": Use the "set_load_size" feature.
#    User manual text: "Press this button to set your washing load size. Your water level throughout all steps in the cycle."
#    Feature name: "set_load_size"
#
# 4. Set the wash time to 20 minutes: Use the "adjust_wash_time" feature.
#    User manual text: "Continuously pressing the washing button to select washing time. (1-20 minutes, or no wash process)"
#    Feature name: "adjust_wash_time"
#
# 5. Set the rinse times to 3: Use the "adjust_rinse_times" feature.
#    User manual text: "Continuously pressing the rinse button to select rinse times. (1-3 times, or no rinse process)"
#    Feature name: "adjust_rinse_times"
#
# 6. Set the spin time to 9 minutes: Use the "adjust_spin_time" feature.
#    User manual text: "Continuously pressing the spin button to select the spin time. (3-9 minutes or no spin process)"
#    Feature name: "adjust_spin_time"
#
# 7. Start the washing cycle: Use the "start_pause_operation" feature.
#    User manual text: "Step 5: Press the START/PAUSE button to start the washing cycle."
#    Feature name: "start_pause_operation"

# Goal variable values:
# - Set variable_power_on_off to "on".
# - Set variable_program to "Soak".
# - Set variable_load_size to "2---medium".
# - Set variable_wash_time to 20.
# - Set variable_rinse_times to 3.
# - Set variable_spin_time to 9.
# - Set variable_start_running to "on".

class ExtendedSimulator(Simulator):
    pass