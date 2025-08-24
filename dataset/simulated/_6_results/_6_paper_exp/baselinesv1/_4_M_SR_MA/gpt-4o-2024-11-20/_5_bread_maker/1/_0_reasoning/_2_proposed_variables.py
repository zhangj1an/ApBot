# variable for menu selection 
variable_menu_index = DiscreteVariable(
    value_range=[
        "Basic", 
        "French", 
        "Whole Wheat", 
        "Quick", 
        "Sweet", 
        "Gluten Free", 
        "Rapid Bake", 
        "Dough", 
        "Jam", 
        "Cake", 
        "Sandwich", 
        "Bake"
    ], 
    current_value="Basic"
)

# variable for crust color selection
variable_crust_color = DiscreteVariable(
    value_range=[
        "Light", 
        "Medium", 
        "Dark"
    ], 
    current_value="Light"
)

# variable for loaf size selection
variable_loaf_size = DiscreteVariable(
    value_range=[
        "1.5LB", 
        "2.0LB"
    ], 
    current_value="1.5LB"
)

# variable for time setting via delay
variable_delay_time = ContinuousVariable(
    value_ranges_steps=[(0, 780, 10), (780, 780, 0)], # 780 mins corresponds to the max delay time of 13 hours
    current_value=0
)

# variable for starting the bread maker
variable_start_running = DiscreteVariable(
    value_range=["on", "off"], 
    current_value="off"
)