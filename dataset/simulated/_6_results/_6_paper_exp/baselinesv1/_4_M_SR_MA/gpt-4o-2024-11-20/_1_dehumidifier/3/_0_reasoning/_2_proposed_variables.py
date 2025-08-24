# User manual: Power Button: Turn air purifier on and off.
variable_power_on_off = DiscreteVariable(value_range=["on", "off"], current_value="off")

# Timer Button: Time can be selected from 1, 2, 4, and 8 hours.
variable_timer = DiscreteVariable(value_range=["0", "1H", "2H", "4H", "8H"], current_value="0")

# UV/UV Reset Button: Press UV button once to turn on the UV light; Press UV button again, the UV light will turn off.
variable_uv_light = DiscreteVariable(value_range=["on", "off"], current_value="off")

# Ionizer/Filter Reset: Press Ionizer button once to turn the ionizer on; Press Ionizer button again, the ionizer will turn off.
variable_ionizer = DiscreteVariable(value_range=["on", "off"], current_value="off")

# Fan Speed/Mode Button: Press the Speed/Mode button to cycle between fan speeds 1, 2, 3, Turbo and Auto mode, and Sleep mode.
variable_fan_speed_mode = DiscreteVariable(value_range=["1", "2", "3", "Turbo", "Auto", "Sleep"], current_value="1")