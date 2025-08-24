# The code provided already models the features accurately based on the user manual.
# Below is the sequence of actions and the relevant feature list names from the given code to achieve the user command.

# User command: Switch on the washer, use 'Rapid' program with a large load size. 
# Set wash time to 8 minutes, rinse twice, and spin for 3 minutes. Start the cycle.

# Sequence of features needed:
# 1. "power_on_off" to switch the washer on.
# 2. "select_program" to set the program to 'Rapid'.
# 3. "adjust_load_size" to set the load size to large (3---large).
# 4. "adjust_wash_time" to set the wash time to 8 minutes.
# 5. "adjust_rinse_times" to set the rinse times to 2.
# 6. "adjust_spin_time" to set the spin time to 3 minutes.
# 7. "start_pause_cycle" to start the cycle.

# Relevant user manual text:
# 1. Step 1: Power on your washer. Press the ON/OFF button to power your wash on.
#    -> Feature: "power_on_off"
# 2. Press this button to select your desired washing program. Heavy, Gentle, Normal, Rapid, Soak.
#    -> Feature: "select_program"
# 3. Press this button to set your washing load size. Your water level throughout all steps in the cycle.
#    -> Feature: "adjust_load_size"
# 4. Continuously pressing the washing button to select washing time. (1-20 minutes, or no wash process).
#    -> Feature: "adjust_wash_time"
# 5. Continuously pressing the rinse button to select rinse times. (1-3 times, or no rinse process).
#    -> Feature: "adjust_rinse_times"
# 6. Continuously pressing the spin button to select the spin time. (3-9 minutes or no spin process).
#    -> Feature: "adjust_spin_time"
# 7. Press the START/PAUSE button to start the washing cycle.
#    -> Feature: "start_pause_cycle"

# Feature list names in the given code:
# 1. "power_on_off"
# 2. "select_program"
# 3. "adjust_load_size"
# 4. "adjust_wash_time"
# 5. "adjust_rinse_times"
# 6. "adjust_spin_time"
# 7. "start_pause_cycle"

# Goal variable values to achieve the command:
variable_power_on_off.set_current_value("on")          # Power the washer on.
variable_program.set_current_value("Rapid")            # Program: Rapid.
variable_load_size.set_current_value("3---large")      # Load size: Large.
variable_wash_time.set_current_value(8)                # Wash time: 8 minutes.
variable_rinse_times.set_current_value(2)              # Rinse 2 times.
variable_spin_time.set_current_value(3)                # Spin for 3 minutes.
variable_start_running.set_current_value("on")         # Start the washer.

class ExtendedSimulator(Simulator): 
    pass