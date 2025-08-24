# Python comments:
# The generated code correctly models all the features required to execute the user command. 
# Here's the sequence of features needed to achieve the requested command, the user manual text supporting these features, and the feature_list where they are implemented:
#
# Sequence of features to execute:
# 1. Feature: "power_on_off" 
#    - Step: Turn on the washing machine.
#    - User manual: Step 1: Power on your washer. Press the ON/OFF button to power your wash on.
#    - Feature list: "power_on_off"
#
# 2. Feature: "select_program" 
#    - Step: Select a "Heavy" program.
#    - User manual: Press this button to select your desired washing program. Heavy, Gentle, Normal, Rapid, Soak.
#    - Feature list: "select_program"
#
# 3. Feature: "adjust_load_size" 
#    - Step: Select large load size.
#    - User manual: Press this button to set your washing load size. Your water level throughout all steps in the cycle.
#    - Feature list: "adjust_load_size"
#
# 4. Feature: "adjust_wash_time" 
#    - Step: Set wash time to 15 minutes.
#    - User manual: Continuously pressing the washing button to select washing time. (1-20 minutes, or no wash process).
#    - Feature list: "adjust_wash_time"
#
# 5. Feature: "adjust_rinse_times" 
#    - Step: Set rinse times to 2.
#    - User manual: Continuously pressing the rinse button to select rinse times. (1-3 times, or no rinse process).
#    - Feature list: "adjust_rinse_times"
#
# 6. Feature: "adjust_spin_time" 
#    - Step: Set spin time to 6 minutes.
#    - User manual: Continuously pressing the spin button to select the spin time. (3-9 minutes or no spin process).
#    - Feature list: "adjust_spin_time"
#
# 7. Feature: "start_pause_cycle" 
#    - Step: Start the cycle.
#    - User manual: Step 5: Press the START/PAUSE button to start the washing cycle.
#    - Feature list: "start_pause_cycle"

# The required goal variable values to achieve the command:
# 1. variable_power_on_off = "on"
# 2. variable_program = "Heavy"
# 3. variable_load_size = "3---large"
# 4. variable_wash_time = 15
# 5. variable_rinse_times = 2
# 6. variable_spin_time = 6
# 7. variable_start_running = "on"

class ExtendedSimulator(Simulator):
    pass