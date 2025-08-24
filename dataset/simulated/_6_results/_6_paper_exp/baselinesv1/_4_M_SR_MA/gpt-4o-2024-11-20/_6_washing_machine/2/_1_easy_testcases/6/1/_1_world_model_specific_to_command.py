# The sequence of features needed to accomplish the user command:
# 1. Turn on the washer using the "power_on_off" feature.
#    - User manual: "Step 1: Power on your washer. Press the ON/OFF button to power your wash on."
#    - Relevant feature: "power_on_off"
# 2. Select 'Heavy' program using the "select_program" feature.
#    - User manual: "Press this button to select your desired washing program. Heavy, Gentle, Normal, Rapid, Soak."
#    - Relevant feature: "select_program"
# 3. Set the load size to 'small' using the "adjust_load_size" feature.
#    - User manual: "Press this button to set your washing load size. Your water level throughout all steps in the cycle."
#    - Relevant feature: "adjust_load_size"
# 4. Adjust wash time to 5 minutes using the "adjust_wash_time" feature.
#    - User manual: "Continuously pressing the washing button to select washing time. (1-20 minutes, or no wash process)."
#    - Relevant feature: "adjust_wash_time"
# 5. Set rinse to 1 time using the "adjust_rinse_times" feature.
#    - User manual: "Continuously pressing the rinse button to select rinse times. (1-3 times, or no rinse process)."
#    - Relevant feature: "adjust_rinse_times"
# 6. Set spin time to 8 minutes using the "adjust_spin_time" feature.
#    - User manual: "Continuously pressing the spin button to select the spin time. (3-9 minutes or no spin process)."
#    - Relevant feature: "adjust_spin_time"
# 7. Start the washer using the "start_pause_cycle" feature.
#    - User manual: "Step 5: Press the START/PAUSE button to start the washing cycle."
#    - Relevant feature: "start_pause_cycle"

# Goal variable values for the command:
# - variable_power_on_off = "on"
# - variable_program = "Heavy"
# - variable_load_size = "1---small"
# - variable_wash_time = 5
# - variable_rinse_times = 1
# - variable_spin_time = 8
# - variable_start_running = "on"

class ExtendedSimulator(Simulator): 
    pass