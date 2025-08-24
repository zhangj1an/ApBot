# variable_power_on_off
# User manual: Step 1: Power on your washer. Press the ON/OFF button to power your wash on.
variable_power_on_off = DiscreteVariable(value_range=["on", "off"], current_value="off")

# variable_program
# User manual: Press this button to select your desired washing program. Heavy, Gentle, Normal, Rapid, Soak.
variable_program = DiscreteVariable(value_range=["Heavy", "Gentle", "Normal", "Rapid", "Soak"], current_value="Heavy")

# variable_load_size
# User manual: Press this button to set your washing load size. Your water level throughout all steps in the cycle.
# Load size values: 1---small, 2---medium, 3---large.
variable_load_size = DiscreteVariable(value_range=["1---small", "2---medium", "3---large"], current_value="1---small")

# variable_start_running
# User manual: Step 5: Press the START/PAUSE button to start the washing cycle.
variable_start_running = DiscreteVariable(value_range=["on", "off"], current_value="off")

# variable_wash_time
# User manual: Continuously pressing the washing button to select washing time. (1-20 minutes, or no wash process)
variable_wash_time = ContinuousVariable(value_ranges_steps=[(0, 20, 1)], current_value=0)

# variable_rinse_times
# User manual: Continuously pressing the rinse button to select rinse times. (1-3 times, or no rinse process)
variable_rinse_times = ContinuousVariable(value_ranges_steps=[(0, 3, 1)], current_value=0)

# variable_spin_time
# User manual: Continuously pressing the spin button to select the spin time. (3-9 minutes or no spin process)
variable_spin_time = ContinuousVariable(value_ranges_steps=[(0, 9, 1)], current_value=0)