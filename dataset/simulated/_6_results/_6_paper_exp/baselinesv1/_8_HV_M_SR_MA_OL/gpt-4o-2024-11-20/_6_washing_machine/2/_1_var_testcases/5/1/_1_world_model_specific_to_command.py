# Python comments regarding accuracy of the current code:
# The given code correctly models all the appliance variables and features required to achieve the user command.
# The sequence of features needed is as follows:
# 1. Turn the appliance on: Feature is "power_on_off", modeled in feature_list["power_on_off"].
#    - User manual text: "Step 1: Press the ON/OFF button to power your wash on."
# 2. Select the 'Soak' program: Feature is "select_program", modeled in feature_list["select_program"].
#    - User manual text: "Press this button to select your desired washing program. Heavy, Gentle, Normal, Rapid, Soak."
# 3. Set the load size to medium: Feature is "adjust_load_size", modeled in feature_list["adjust_load_size"].
#    - User manual text: "Press this button to set your washing load size. It will determine water level throughout all steps in the cycle."
# 4. Set washing time to 20 minutes: Feature is "adjust_wash_time", modeled in feature_list["adjust_wash_time"].
#    - User manual text: "Continuously pressing the washing button to select washing time. (1-20 minutes, or no wash process)"
# 5. Set rinse times to 3: Feature is "adjust_rinse_times", modeled in feature_list["adjust_rinse_times"].
#    - User manual text: "Continuously pressing the rinse button to select rinse times. (1-3 times, or no rinse process)"
# 6. Set spin time to 9 minutes: Feature is "adjust_spin_time", modeled in feature_list["adjust_spin_time"].
#    - User manual text: "Continuously pressing the spin button to select the spin time. (3-9 minutes or no wash process)"
# 7. Start the washing process: Feature is "start_pause_cycle", modeled in feature_list["start_pause_cycle"].
#    - User manual text: "Press the START/PAUSE button to start the washing cycle."

# Goal variable values to achieve the command:
# variable_power_on_off = "on"
# variable_program = "Soak"
# variable_load_size = "2---medium"
# variable_wash_time = 20
# variable_rinse_times = 3
# variable_spin_time = 9
# variable_start_running = "on"

class ExtendedSimulator(Simulator): 
    pass