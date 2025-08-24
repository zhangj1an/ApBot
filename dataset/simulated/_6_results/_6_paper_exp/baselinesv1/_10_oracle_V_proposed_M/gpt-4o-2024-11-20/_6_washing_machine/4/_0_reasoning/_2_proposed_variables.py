# User manual: Press this button to switch power on and off. 
# The washing machine automatically switches off when operations are finished. 
# The washing machine also turns off automatically if it is not operated or no button is pressed for 20 minutes after the power has been turned on.
# Push this button a little longer than other buttons (around 1 second)
variable_power_on_off = DiscreteVariable(value_range=["on", "off"], current_value="off")

# User manual: Starts and pauses operation. When the washing machine is paused for over one hour and no operations are done, it turns off automatically.
variable_start_running = DiscreteVariable(value_range=["start", "pause"], current_value="pause")

# Different programs which can be chosen using the program button.
variable_program = DiscreteVariable(
    value_range=["P1 (Fuzzy)", "P2 (Powerful)", "P3 (Speedy)", "P4 (Fragrance)", 
                 "P5 (Soak)", "P6 (Tub Clean)", "P7 (Water Save)", 
                 "P8 (Energy Save)", "P9 (Small Load)"], 
    current_value="P1 (Fuzzy)"
)

# Adjusting water level
# User manual: You can set the amount of water each time you press the Water Level button in a range from 25 to 59 L.
variable_water_level = ContinuousVariable(
    value_ranges_steps=[(25, 59, 1)], 
    current_value=25
)

# Adjusting washing time
# User manual: Changes the washing time. The washing time can be set between 3 and 18 minutes.
variable_washing_time = ContinuousVariable(
    value_ranges_steps=[(0, 3, 3), (3, 18, 3)], 
    current_value=0
)

# Adjusting rinsing type
# User manual: You can set the number and type of rinses by pressing the Rinse button.
# Each time you press the Rinse button the setting changes in sequence, from Normal Rinse 2 times, 
# Water-Injection Rinse 2 times, no rinsing, Normal Rinse 1 time, Water-Injection Rinse 1 time.
variable_rinse_type = DiscreteVariable(
    value_range=["Normal Rinse 2 times", "Water-Injection Rinse 2 times", 
                 "No rinsing", "Normal Rinse 1 time", "Water-Injection Rinse 1 time"], 
    current_value="Normal Rinse 2 times"
)

# Adjusting spin time
# User manual: You can set the spin time each time you press the Spin button in a range of 1 to 9 minutes and no spinning.
variable_spin_time = ContinuousVariable(
    value_ranges_steps=[(0, 1, 1), (1, 9, 1)], 
    current_value=0
)

# Adjusting delay timer (time to finish washing)
# User manual: The delay time can be set between 3 and 12 hours.
variable_delay_timer = ContinuousVariable(
    value_ranges_steps=[(0, 3, 3), (3, 12, 1)], 
    current_value=0
)