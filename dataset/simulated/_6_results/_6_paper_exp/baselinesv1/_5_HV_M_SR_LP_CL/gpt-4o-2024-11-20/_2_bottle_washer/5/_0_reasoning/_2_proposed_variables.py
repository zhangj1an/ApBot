# User manual: Press this button to switch the steriliser on and off.
variable_power_on_off = DiscreteVariable(value_range=["on", "off"], current_value="off")

# Sterilise only function
variable_sterilise_only_duration = DiscreteVariable(value_range=["10 minutes", "35 minutes"], current_value="10 minutes")

# Drying only function
variable_drying_only_duration = DiscreteVariable(value_range=["30 minutes", "40 minutes", "50 minutes"], current_value="30 minutes")

# Auto mode
variable_auto_mode_duration = DiscreteVariable(value_range=["35 minutes", "60 minutes"], current_value="35 minutes")

# Storage function
variable_storage_mode = DiscreteVariable(value_range=["off", "on"], current_value="off")

# Button sound
variable_button_sound = DiscreteVariable(value_range=["on", "off"], current_value="on")