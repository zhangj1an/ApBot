# Upper element temperature dial variable
variable_upper_element_temperature = DiscreteVariable(
    value_range=["OFF", "Keep Warm", "150", "250", "350", "450"],
    current_value="OFF"
)

# Lower element temperature dial variable
variable_lower_element_temperature = DiscreteVariable(
    value_range=["OFF", "Keep Warm", "150", "250", "350", "450"],
    current_value="OFF"
)

# Function dial variable
variable_function_dial = DiscreteVariable(
    value_range=["OFF", "Toast/Broil", "Convection", "Rotisserie", "Convection Rotisserie"],
    current_value="OFF"
)

# Timer dial variable
variable_timer = ContinuousVariable(
    value_ranges_steps=[[0, 60, 10]],
    current_value=0
)