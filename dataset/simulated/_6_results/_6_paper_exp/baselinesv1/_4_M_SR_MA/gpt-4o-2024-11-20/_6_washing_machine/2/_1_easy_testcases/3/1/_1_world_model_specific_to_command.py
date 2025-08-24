# User command: Activate the machine, select a 'Normal' program for a small load. 
# Set washing time to 12 minutes, rinse twice, and spin for 5 minutes. Start it.

# The sequence of features needed to achieve this command are:
# 1. "power_on_off": Activate the machine.
# 2. "select_program": Select a 'Normal' program.
# 3. "adjust_load_size": Set the load size to 'small'.
# 4. "adjust_wash_time": Set washing time to 12 minutes.
# 5. "adjust_rinse_times": Set rinse times to 2.
# 6. "adjust_spin_time": Set spin time to 5 minutes.
# 7. "start_pause_cycle": Start the washing process.

# Relevant user manual text:
# - "Step 1: Power on your washer. Press the ON/OFF button to power your wash on."
# - "Press this button to select your desired washing program. Heavy, Gentle, Normal, Rapid, Soak."
# - "Press this button to set your washing load size. Your water level throughout all steps in the cycle. Load size values: 1---small, 2---medium, 3---large."
# - "Continuously pressing the washing button to select washing time. (1-20 minutes, or no wash process)."
# - "Continuously pressing the rinse button to select rinse times. (1-3 times, or no rinse process)."
# - "Continuously pressing the spin button to select the spin time. (3-9 minutes or no spin process)."
# - "Step 5: Press the START/PAUSE button to start the washing cycle."

# Feature list used in generated code:
# - feature_list["power_on_off"]
# - feature_list["select_program"]
# - feature_list["adjust_load_size"]
# - feature_list["adjust_wash_time"]
# - feature_list["adjust_rinse_times"]
# - feature_list["adjust_spin_time"]
# - feature_list["start_pause_cycle"]

# The goal variable values to achieve this command:
# - variable_power_on_off: "on"
# - variable_program: "Normal"
# - variable_load_size: "1---small"
# - variable_wash_time: 12
# - variable_rinse_times: 2
# - variable_spin_time: 5
# - variable_start_running: "on"

class ExtendedSimulator(Simulator): 
    pass