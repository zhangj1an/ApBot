# User manual: Press the (power) POWER button to turn on and the (power) POWER symbol light will illuminate.
variable_power_on_off = DiscreteVariable(value_range=["on", "off"], current_value="off")

# User manual: The Microbe Shield™ and Night Modes utilize the same button on the control panel. Pressing the (microbe shield) Microbe Shield™/NIGHT MODE button will cycle through these two settings.
variable_microbe_shield_night_mode = DiscreteVariable(value_range=["microbe_shield", "night_mode", "off"], current_value="off")

# User manual: Press the (fan speed) FAN SPEED button repeatedly until the desired speed is illuminated on the control panel. There are 4 fan speeds: Low, Medium, High and Turbo.
variable_fan_speed = DiscreteVariable(value_range=["low", "medium", "high", "turbo"], current_value="low")

# User manual: The air purifier can be set to operate for timed intervals of 2 hours, 4 hours and 8 hours, stopping automatically when the selected operating time has elapsed.
variable_timer = DiscreteVariable(value_range=["2H", "4H", "8H", "off"], current_value="off")