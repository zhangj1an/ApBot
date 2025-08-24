# Python comment: The current code accurately models the relevant appliance features and variables necessary to achieve the user command:
# **Switch on the washer, use 'Rapid' program with a large load size. Set wash time to 8 minutes, rinse twice, and spin for 3 minutes. Start the cycle.**

# Sequence of features required:
# 1. "turn_power_on_off" to switch on the washer. (Feature list: "turn_power_on_off")
# 2. "set_program" to select 'Rapid' program. (Feature list: "set_program")
# 3. "set_load_size" to select a large load size. (Feature list: "set_load_size")
# 4. "adjust_wash_time" to set wash time to 8 minutes. (Feature list: "adjust_wash_time")
# 5. "adjust_rinse_times" to set rinse times to 2. (Feature list: "adjust_rinse_times")
# 6. "adjust_spin_time" to set spin time to 3 minutes. (Feature list: "adjust_spin_time")
# 7. "start_pause_operation" to start the cycle. (Feature list: "start_pause_operation")

# Quoted user manual text for relevant features:
# 1. "**Power on your washer:** Step 1: Press the ON/OFF button to power your wash on." (Feature: "turn_power_on_off")
# 2. "**Program selection:** Press this button to select your desired washing program. [Options: Heavy, Gentle, Normal, Rapid, Soak]." (Feature: "set_program")
# 3. "**Load size adjustment:** Press this button to set your washing load size. [Options: 1---small, 2---medium, 3---large]." (Feature: "set_load_size")
# 4. "**Wash time adjustment:** Continuously pressing the washing button to select washing time. (1-20 minutes, or no wash process)." (Feature: "adjust_wash_time")
# 5. "**Rinse times adjustment:** Continuously pressing the rinse button to select rinse times. (1-3 times, or no rinse process)." (Feature: "adjust_rinse_times")
# 6. "**Spin time adjustment:** Continuously pressing the spin button to select the spin time. (3-9 minutes or no spin process)." (Feature: "adjust_spin_time")
# 7. "**Start operation:** Step 5: Press the START/PAUSE button to start the washing cycle." (Feature: "start_pause_operation")

# Goal variable values to achieve the command:
# - variable_power_on_off: "on"
# - variable_program: "Rapid"
# - variable_load_size: "3---large"
# - variable_wash_time: 8
# - variable_rinse_times: 2
# - variable_spin_time: 3
# - variable_start_running: "on"

class ExtendedSimulator(Simulator): 
    pass