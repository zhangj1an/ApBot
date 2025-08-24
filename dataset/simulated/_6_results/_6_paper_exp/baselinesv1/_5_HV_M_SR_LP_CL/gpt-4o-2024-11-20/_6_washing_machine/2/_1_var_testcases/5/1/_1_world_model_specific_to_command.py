# User command: Turn the washing machine on, choose 'Soak' program with a medium size load. 
# Set wash to 20 minutes, rinse three times, and spin for 9 minutes. Begin process.

# Raw user manual text relevant to this command:
# 1. Power on your washer: "Step 1: Power on your washer. Press the ON/OFF button to power your wash on."
# 2. Choose desired program: "Press this button to select your desired washing program. Heavy, Gentle, Normal, Rapid, Soak."
# 3. Set load size: "Press this button to set your washing load size. Your water level throughout all steps in the cycle."
# 4. Adjust wash time: "Continuously pressing the washing button to select washing time. (1-20 minutes, or no wash process)"
# 5. Adjust rinse times: "Continuously pressing the rinse button to select rinse times. (1-3 times, or no rinse process)"
# 6. Adjust spin time: "Continuously pressing the spin button to select the spin time. (3-9 minutes or no spin process)"
# 7. Start the cycle: "Step 5: Press the START/PAUSE button to start the washing cycle."

# The sequence of features needed to achieve this command:
# 1. "power_on_off" - Toggle power to "on".
# 2. "select_program" - Set the washing program to 'Soak'.
# 3. "adjust_load_size" - Set washing load size to '2---medium'.
# 4. "adjust_wash_time" - Set washing time to 20 minutes.
# 5. "adjust_rinse_times" - Set rinse times to 3.
# 6. "adjust_spin_time" - Set spin time to 9 minutes.
# 7. "start_pause_cycle" - Start the washing cycle by pressing start.
#
# All steps correctly modeled in the existing codebase, and the provided feature list aligns with the user manual.

# Goal variable values to achieve this command:
# variable_power_on_off -> "on"
# variable_program -> "Soak"
# variable_load_size -> "2---medium"
# variable_wash_time -> 20
# variable_rinse_times -> 3
# variable_spin_time -> 9
# variable_start_running -> "on"

class ExtendedSimulator(Simulator): 
    pass