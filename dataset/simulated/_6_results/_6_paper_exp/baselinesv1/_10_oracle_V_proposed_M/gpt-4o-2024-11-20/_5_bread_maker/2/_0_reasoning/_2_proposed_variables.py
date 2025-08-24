# Defining variables for the breadmaker appliance based on the user manual

# Variable for crust color
variable_crust_color = DiscreteVariable(value_range=["light", "medium", "dark"], current_value="light")

# Variable for loaf size
variable_loaf_size = DiscreteVariable(value_range=["1.5lb", "2lb"], current_value="1.5lb")

# Variable for menu selection
variable_menu_index = DiscreteVariable(value_range=[
    "1 Basic white", 
    "2 French", 
    "3 Wholewheat", 
    "4 Quick", 
    "5 Sweet", 
    "6 Fastbake I", 
    "7 Fastbake II", 
    "8 Dough", 
    "9 Jam", 
    "10 Cake", 
    "11 Sandwich", 
    "12 Extra bake"
], current_value="1 Basic white")

# Variable for timer delay (continuous adjustment in 10-minute increments)
variable_timer_delay = ContinuousVariable(
    value_ranges_steps=[(0, 780, 10)],  # Maximum is 13 hours, converted to minutes
    current_value=0
)

# Variable for baking time for menu 12 (Extra bake) with default time of 1 hour
variable_menu_setting_12_extra_bake_time = ContinuousVariable(
    value_ranges_steps=[(60, 60, 10)],  # Default is 1 hour, counts down in 10-minute intervals
    current_value=60
)

# Start/Stop button needs to be pressed to start or terminate operation
variable_start_running = DiscreteVariable(value_range=["off", "on"], current_value="off")