# The provided code already includes features and variables that can correctly model the requested user command:
# 1. Turn on the washing machine.
#    Raw user manual text: "Step 1: Power on your washer. Press the ON/OFF button to power your wash on."
#    Feature: feature_list["power_on_off"]
# 2. Select the 'Heavy' program.
#    Raw user manual text: "Press this button to select your desired washing program. Heavy, Gentle, Normal, Rapid, Soak."
#    Feature: feature_list["select_program"]
# 3. Select a large load.
#    Raw user manual text: "Press this button to set your washing load size. Your water level throughout all steps in the cycle."
#    Feature: feature_list["adjust_load_size"]
# 4. Set wash time to 15 minutes.
#    Raw user manual text: "Continuously pressing the washing button to select washing time. (1-20 minutes, or no wash process)."
#    Feature: feature_list["adjust_wash_time"]
# 5. Set rinse twice.
#    Raw user manual text: "Continuously pressing the rinse button to select rinse times. (1-3 times, or no rinse process)."
#    Feature: feature_list["adjust_rinse_times"]
# 6. Set spin for 6 minutes.
#    Raw user manual text: "Continuously pressing the spin button to select the spin time. (3-9 minutes or no spin process)."
#    Feature: feature_list["adjust_spin_time"]
# 7. Start the cycle.
#    Raw user manual text: "Press the START/PAUSE button to start the washing cycle."
#    Feature: feature_list["start_pause_cycle"]

# The goal variable values to achieve this user command are as follows:
# - Set variable_power_on_off to "on".
# - Set variable_program to "Heavy".
# - Set variable_load_size to "3---large".
# - Set variable_wash_time to 15.
# - Set variable_rinse_times to 2.
# - Set variable_spin_time to 6.
# - Set variable_start_running to "on".

class ExtendedSimulator(Simulator): 
    pass