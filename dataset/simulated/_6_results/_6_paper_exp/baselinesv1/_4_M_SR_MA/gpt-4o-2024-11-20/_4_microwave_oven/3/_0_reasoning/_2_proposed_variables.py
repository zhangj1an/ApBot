# Variable: variable_upper_tube_temperature
variable_upper_tube_temperature = ContinuousVariable(value_ranges_steps=[(0, 70, 70), (70, 230, 40)], current_value=0)

# Variable: variable_function_selection
variable_function_selection = DiscreteVariable(value_range=["off", "lower_tube", "upper_tube", "upper_and_lower_tubes", 
                                                            "upper_and_lower_tubes_with_convection", "upper_tube_with_rotisserie"], 
                                                current_value="off")

# Variable: variable_lower_tube_temperature
variable_lower_tube_temperature = ContinuousVariable(value_ranges_steps=[(0, 70, 70), (70, 230, 40)], current_value=0)

# Variable: variable_time_adjustment
variable_time_adjustment = ContinuousVariable(value_ranges_steps=[(0, 10, 10), (10, 60, 10)], current_value=0)

# Variable: variable_start_running
# User manual: When "Stay On" gear is selected, the electric oven is in a continuous working state and the power indicator light is lit; to end the work, manually turn the time knob back to the "OFF" gear.
variable_start_running = DiscreteVariable(value_range=["on", "off"], current_value="off")