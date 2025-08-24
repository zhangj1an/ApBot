# The current code correctly models the relevant appliance features to achieve the user command.
# Sequence of features needed to achieve the command:
# 1. Use the "power_on_off" feature to turn on the appliance.
# 2. Use the "adjust_fan_speed" feature to set the fan speed to 'low'.

# Raw user manual text quote for "power_on_off":
# User manual: Press the (power) POWER button to turn on and the (power) POWER symbol light will illuminate.
# Feature in the given code: "power_on_off"

# Raw user manual text quote for "adjust_fan_speed":
# User manual: Press the (fan speed) FAN SPEED button repeatedly until the desired speed is illuminated on the control panel. There are 4 fan speeds: Low, Medium, High and Turbo.
# Feature in the given code: "adjust_fan_speed"

# Goal variable values to achieve the command:
# 1. Set variable_power_on_off to "on"
# 2. Set variable_fan_speed to "low"

class ExtendedSimulator(Simulator): 
    pass