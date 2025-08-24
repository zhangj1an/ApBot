# variable for the upper heater temperature knob
variable_upper_heater_temperature = ContinuousVariable(value_ranges_steps=[(0, 70, 70), (70, 230, 40)], current_value=0)

# variable for the lower heater temperature knob
variable_lower_heater_temperature = ContinuousVariable(value_ranges_steps=[(0, 70, 70), (70, 230, 40)], current_value=0)

# variable for the timer
variable_timer = DiscreteVariable(
    value_range=["0", "20", "40", "60", "100", "120", "Stay On"],
    current_value="0"
)

# variable for the function knob
variable_function_knob = DiscreteVariable(
    value_range=["Off", "Fermentation", "Convection", "Lower & Upper Heater", "Upper Heater"],
    current_value="Off"
)