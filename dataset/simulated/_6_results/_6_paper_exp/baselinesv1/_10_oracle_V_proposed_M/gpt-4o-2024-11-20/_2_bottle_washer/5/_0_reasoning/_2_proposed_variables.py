# User manual: Press this button to switch the steriliser on and off.
variable_power_on_off = DiscreteVariable(value_range=["on", "off"], current_value="off")

# Variable for Auto Mode time cycles
variable_auto_mode = DiscreteVariable(value_range=["35_minutes", "60_minutes"], current_value="35_minutes")

# Variable for Sterilise Only time
variable_sterilise_only_time = DiscreteVariable(value_range=["10_minutes", "35_minutes"], current_value="10_minutes")

# Variable for Drying Only time
variable_drying_only_time = DiscreteVariable(value_range=["30_minutes", "40_minutes", "50_minutes"], current_value="30_minutes")

# Variable for Storage mode
variable_storage_mode = DiscreteVariable(value_range=["off", "on"], current_value="off")