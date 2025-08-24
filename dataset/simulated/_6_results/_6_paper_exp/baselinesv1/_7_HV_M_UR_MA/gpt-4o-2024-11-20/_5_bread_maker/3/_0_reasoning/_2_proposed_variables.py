# Variable start running after all the settings. 
variable_start_running = DiscreteVariable(value_range=["on", "off"], current_value="off")

# Variable for selecting cycle
# User manual: Press CYCLE button to select your desired cycle. The corresponding cycle number is shown on the display.
variable_cycle = DiscreteVariable(
    value_range=["Basic", "French", "Gluten-Free", "Quick", "Sweet", 
                 "1.5lb. Express", "2.0lb. Express", "Dough", "Jam", 
                 "Cake", "Whole Grain", "Bake"], 
    current_value="Basic"
)

# Variable for selecting crust color
# User manual: Press CRUST button to move the arrow to desired setting: Light, Medium, or Dark crust. (Crust is not adjustable in Cycles 6, 7, 8, 9, and 10.)
variable_crust_color = DiscreteVariable(
    value_range=["Light", "Medium", "Dark"],
    current_value="Medium"
)

# Variable for selecting loaf size
# User manual: Press the LOAF SIZE button to move the arrow to 1.5- or 2-lb. loaf size. (Loaf size is not an option in Cycles 6, 7, 8, 9, 10, and 11.)
variable_loaf_size = DiscreteVariable(
    value_range=["1.5lb", "2.0lb"],
    current_value="1.5lb"
)

# Variable for setting delay timer
# User manual: Use the Delay Timer feature to start the breadmaker at a later time. Press the + and – buttons to increase the cycle time shown on the display. Add up to 13 hours including the delay time and breadmaking cycle.
variable_delay_timer = ContinuousVariable(
    value_ranges_steps=[(0, 780, 1)],  # Delay timer ranges from 0 minutes to 13 hours (780 minutes) with a step of 1 minute.
    current_value=0
)