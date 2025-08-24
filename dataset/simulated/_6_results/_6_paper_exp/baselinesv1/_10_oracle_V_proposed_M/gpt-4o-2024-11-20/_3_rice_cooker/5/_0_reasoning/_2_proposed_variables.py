# Variable for starting the appliance
variable_start_running = DiscreteVariable(value_range=["on", "off"], current_value="off")

# Variable for cooking program selection
variable_cooking_program = DiscreteVariable(
    value_range=[
        "jasmine_rice", 
        "white_rice", 
        "brown_rice", 
        "glutinous_rice", 
        "clay_pot", 
        "soup_congee", 
        "quick_cooking_steam", 
        "slow_cook_stew", 
        "reheat"
    ], 
    current_value="jasmine_rice"
)

# Variable for timer adjustment
variable_timer = ContinuousVariable(value_ranges_steps=[(0, 1440, 1)], current_value=0)  # Timer in minutes, max 24 hours

# Variable for preset time adjustment
variable_preset_time = ContinuousVariable(value_ranges_steps=[(0, 1440, 1)], current_value=0)  # Preset time in minutes, max 24 hours

# Variable for keep warm functionality
variable_keep_warm = DiscreteVariable(value_range=["on", "off"], current_value="off")