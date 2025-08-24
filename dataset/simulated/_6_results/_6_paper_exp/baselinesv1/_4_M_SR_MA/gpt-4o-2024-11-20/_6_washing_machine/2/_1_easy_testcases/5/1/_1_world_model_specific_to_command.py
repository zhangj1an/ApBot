# User command: Turn the washing machine on, choose 'Soak' program with a medium size load. 
# Set wash to 20 minutes, rinse three times, and spin for 9 minutes. Begin process.

# The sequence of features needed to execute this command:
# 1. "power_on_off" to turn the washing machine on.
#    User manual: "Step 1: Power on your washer. Press the ON/OFF button to power your wash on."
#    Feature: "power_on_off".
#
# 2. "select_program" to choose 'Soak' program.
#    User manual: "Press this button to select your desired washing program."
#    Feature: "select_program".
#
# 3. "adjust_load_size" to set the load size to "medium".
#    User manual: "Press this button to set your washing load size. Your water level throughout all steps in the cycle."
#    Feature: "adjust_load_size".
#
# 4. "adjust_wash_time" to set wash time to 20 minutes.
#    User manual: "Continuously pressing the washing button to select washing time (1-20 minutes, or no wash process)."
#    Feature: "adjust_wash_time".
#
# 5. "adjust_rinse_times" to set rinse times to 3.
#    User manual: "Continuously pressing the rinse button to select rinse times (1-3 times, or no rinse process)."
#    Feature: "adjust_rinse_times".
#
# 6. "adjust_spin_time" to set spin time to 9 minutes.
#    User manual: "Continuously pressing the spin button to select the spin time (3-9 minutes or no spin process)."
#    Feature: "adjust_spin_time".
#
# 7. "start_pause_cycle" to begin the process.
#    User manual: "Step 5: Press the START/PAUSE button to start the washing cycle."
#    Feature: "start_pause_cycle".

# Goal variable values to achieve this command:
# variable_power_on_off = "on"
# variable_program = "Soak"
# variable_load_size = "2---medium"
# variable_wash_time = 20
# variable_rinse_times = 3
# variable_spin_time = 9
# variable_start_running = "on"

class ExtendedSimulator(Simulator):
    pass