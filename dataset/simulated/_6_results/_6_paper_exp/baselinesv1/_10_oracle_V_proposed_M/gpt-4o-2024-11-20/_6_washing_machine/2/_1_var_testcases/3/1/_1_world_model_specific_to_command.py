# The user manual correctly describes the features relevant to the command.
# The given code models each step with suitable variables and actions, enabling the command to be executed as intended.
# Sequence of features needed to achieve this command:
# 1. "turn_power_on_off" to turn on the machine.
# 2. "set_program" to select the 'Normal' program.
# 3. "set_load_size" to select a small load size.
# 4. "adjust_wash_time" to set washing time to 12 minutes.
# 5. "adjust_rinse_times" to set rinse times to two.
# 6. "adjust_spin_time" to set spin time to 5 minutes.
# 7. "start_pause_operation" to start the operation.

# Relevant user manual excerpts:
# 1. "Step 1: Power on your washer. Press the ON/OFF button to power your wash on."
#    Feature: "turn_power_on_off"
# 2. "Press this button to select your desired washing program. Heavy, Gentle, Normal, Rapid, Soak."
#    Feature: "set_program"
# 3. "Press this button to set your washing load size. Your water level throughout all steps in the cycle."
#    Feature: "set_load_size"
# 4. "Continuously pressing the washing button to select washing time. (1-20 minutes, or no wash process)"
#    Feature: "adjust_wash_time"
# 5. "Continuously pressing the rinse button to select rinse times. (1-3 times, or no rinse process)"
#    Feature: "adjust_rinse_times"
# 6. "Continuously pressing the spin button to select the spin time. (3-9 minutes or no spin process)"
#    Feature: "adjust_spin_time"
# 7. "Step 5: Press the START/PAUSE button to start the washing cycle."
#    Feature: "start_pause_operation"

# Goal variable values for the command:
# variable_power_on_off = "on"
# variable_program = "Normal"
# variable_load_size = "1---small"
# variable_wash_time = 12
# variable_rinse_times = 2
# variable_spin_time = 5
# variable_start_running = "on"

class ExtendedSimulator(Simulator):
    pass