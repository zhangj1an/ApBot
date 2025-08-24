# The given code accurately models the appliance features needed to fulfill the command:
# "Turn on the washing machine and select a 'Heavy' program with a large load. 
# Set wash time to 15 minutes, rinse twice, and spin for 6 minutes. Start the cycle."

# Below is a breakdown of user commands and their corresponding features:
# 1. Turn on the washing machine:
#    Raw User Manual Text: "Step 1: Power on your washer. Press the ON/OFF button to power your wash on."
#    Feature Name in Code: "turn_power_on_off"
#    Variables Adjusted: variable_power_on_off, target value="on"

# 2. Select a "Heavy" program:
#    Raw User Manual Text: "Press this button to select your desired washing program. Heavy, Gentle, Normal, Rapid, Soak."
#    Feature Name in Code: "set_program"
#    Variables Adjusted: variable_program, target value="Heavy"

# 3. Select a large load size:
#    Raw User Manual Text: "Press this button to set your washing load size. Your water level throughout all steps in the cycle."
#    Feature Name in Code: "set_load_size"
#    Variables Adjusted: variable_load_size, target value="3---large"

# 4. Set wash time to 15 minutes:
#    Raw User Manual Text: "Continuously pressing the washing button to select washing time. (1-20 minutes, or no wash process)"
#    Feature Name in Code: "adjust_wash_time"
#    Variables Adjusted: variable_wash_time, target value=15

# 5. Set rinse times to 2:
#    Raw User Manual Text: "Continuously pressing the rinse button to select rinse times. (1-3 times, or no rinse process)"
#    Feature Name in Code: "adjust_rinse_times"
#    Variables Adjusted: variable_rinse_times, target value=2

# 6. Set spin time to 6 minutes:
#    Raw User Manual Text: "Continuously pressing the spin button to select the spin time. (3-9 minutes or no spin process)"
#    Feature Name in Code: "adjust_spin_time"
#    Variables Adjusted: variable_spin_time, target value=6

# 7. Start the cycle:
#    Raw User Manual Text: "Step 5: Press the START/PAUSE button to start the washing cycle."
#    Feature Name in Code: "start_pause_operation"
#    Variables Adjusted: variable_start_running, target value="on"

# Goal Variable Values:
# variable_power_on_off: "on"
# variable_program: "Heavy"
# variable_load_size: "3---large"
# variable_wash_time: 15
# variable_rinse_times: 2
# variable_spin_time: 6
# variable_start_running: "on"

class ExtendedSimulator(Simulator):
    pass