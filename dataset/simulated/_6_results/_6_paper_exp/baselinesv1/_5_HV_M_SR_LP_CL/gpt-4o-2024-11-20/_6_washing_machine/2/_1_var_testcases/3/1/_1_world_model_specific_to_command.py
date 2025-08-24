# Check against user manual description:
# After reading the user manual and comparing it with the provided code for the feature list, all necessary features to achieve the command are already correctly modeled:
# 1. Turning the machine on/off is modeled by "power_on_off".
# 2. Selecting "Normal" program for a small load is modeled by "select_program" and "adjust_load_size".
# 3. Setting washing time to 12 minutes is modeled by "adjust_wash_time".
# 4. Setting rinse times to 2 and spin time to 5 minutes are modeled by "adjust_rinse_times" and "adjust_spin_time" respectively.
# 5. Starting the cycle is modeled by "start_pause_cycle".

# Sequence of features to achieve the command:
# 1. "power_on_off" - Turn on the machine.
# 2. "select_program" - Set program to "Normal".
# 3. "adjust_load_size" - Set load size to "1---small" (small).
# 4. "adjust_wash_time" - Set washing time to 12 minutes.
# 5. "adjust_rinse_times" - Set rinse times to 2.
# 6. "adjust_spin_time" - Set spin time to 5 minutes.
# 7. "start_pause_cycle" - Start the washing cycle.

# Relevant user manual text and feature_list name:
# 1. Power: "Step 1: Power on your washer. Press the ON/OFF button to power your wash on." (Feature: "power_on_off")
# 2. Program: "Press this button to select your desired washing program. Heavy, Gentle, Normal, Rapid, Soak." (Feature: "select_program")
# 3. Load size: "Press this button to set your washing load size. Your water level throughout all steps in the cycle." (Feature: "adjust_load_size")
# 4. Wash time: "Continuously pressing the washing button to select washing time. (1-20 minutes, or no wash process)" (Feature: "adjust_wash_time")
# 5. Rinse times: "Continuously pressing the rinse button to select rinse times. (1-3 times, or no rinse process)" (Feature: "adjust_rinse_times")
# 6. Spin time: "Continuously pressing the spin button to select the spin time. (3-9 minutes or no spin process)" (Feature: "adjust_spin_time")
# 7. Start cycle: "Step 5: Press the START/PAUSE button to start the washing cycle." (Feature: "start_pause_cycle")

# Goal variable values:
# 1. variable_power_on_off: "on"
# 2. variable_program: "Normal"
# 3. variable_load_size: "1---small"
# 4. variable_wash_time: 12
# 5. variable_rinse_times: 2
# 6. variable_spin_time: 5
# 7. variable_start_running: "on"

class ExtendedSimulator(Simulator):
    pass