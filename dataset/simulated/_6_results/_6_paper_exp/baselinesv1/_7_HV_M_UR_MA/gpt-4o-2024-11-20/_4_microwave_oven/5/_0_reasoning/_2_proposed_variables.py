# Variable for function dial
variable_function_dial = DiscreteVariable(
    value_range=["Off", "Convection", "Rotisserie", "Rotisserie & Convection"],
    current_value="Off"
)

# Variable for temperature dial
variable_temperature_dial = DiscreteVariable(
    value_range=["Off", "100°C", "150°C", "200°C", "250°C"],
    current_value="Off"
)

# Variable for selector dial
variable_selector_dial = DiscreteVariable(
    value_range=["Off", "Top Heating", "Bottom Heating", "Top & Bottom Heating"],
    current_value="Off"
)

# Variable for timer dial
variable_timer_dial = DiscreteVariable(
    value_range=["Off", "10 minutes", "20 minutes", "30 minutes", "40 minutes"],
    current_value="Off"
)