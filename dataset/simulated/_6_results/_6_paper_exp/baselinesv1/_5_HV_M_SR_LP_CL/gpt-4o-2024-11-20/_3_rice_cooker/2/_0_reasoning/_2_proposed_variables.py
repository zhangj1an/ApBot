# variable to start running the appliance
variable_start_running = DiscreteVariable(value_range=["on", "off"], current_value="off")

# variable to select cooking mode
variable_cooking_mode = DiscreteVariable(
    value_range=["fast cook", "white rice", "congee", "soup", "cake", "keep warm"],
    current_value="fast cook"
)

# variable to control the preset timer for delayed cooking
variable_preset_timer = ContinuousVariable(
    value_ranges_steps=[(0, 1440, 15)],  # in minutes, up to 24 hours
    current_value=0
)