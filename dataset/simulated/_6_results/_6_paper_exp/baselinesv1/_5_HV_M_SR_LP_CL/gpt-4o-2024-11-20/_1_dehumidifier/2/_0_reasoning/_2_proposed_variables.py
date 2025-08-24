# User manual: Press the ⏻ button to turn on/off the unit.
variable_power_on_off = DiscreteVariable(value_range=["on", "off"], current_value="off")

# Operating Modes
variable_mode = DiscreteVariable(value_range=["COOL", "DRY", "FAN", "SMART"], current_value="COOL")

# Temperature setting, 18°C to 32°C with default of 18°C, continuous.
variable_temperature_setting = ContinuousVariable(value_ranges_steps=[(18, 32, 1)], current_value=18)

# Fan speed settings
variable_fan_speed = DiscreteVariable(value_range=["HIGH", "MEDIUM", "LOW", "AUTO"], current_value="HIGH")

# Timer from 1 to 24 hours in 1-hour increments.
variable_timer_setting = ContinuousVariable(value_ranges_steps=[(1, 24, 1)], current_value=1)

# Sleep mode, can be on or off.
variable_sleep_mode = DiscreteVariable(value_range=["on", "off"], current_value="off")