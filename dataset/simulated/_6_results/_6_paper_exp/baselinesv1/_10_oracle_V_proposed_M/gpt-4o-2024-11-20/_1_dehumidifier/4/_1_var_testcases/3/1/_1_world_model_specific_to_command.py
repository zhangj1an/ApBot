# The user manual describes starting the appliance and adjusting fan speed, which involves two features: "power_on_off" and "adjust_fan_speed".
# The given code correctly models both features required to achieve the user command. 
# The relevant features are:
# 1. "power_on_off": Allows toggling the appliance power on and off.
# User manual: "Press the (power) POWER button to turn on and the (power) POWER symbol light will illuminate."
# Corresponding feature: feature_list["power_on_off"]

# 2. "adjust_fan_speed": Allows setting the fan speed to "low", "medium", "high", or "turbo".
# User manual: "Press the (fan speed) FAN SPEED button repeatedly until the desired speed is illuminated on the control panel. There are 4 fan speeds: Low, Medium, High and Turbo."
# Corresponding feature: feature_list["adjust_fan_speed"]

# To achieve the given command:
# First, use the "power_on_off" feature to turn on the appliance, setting `variable_power_on_off` to "on".
# Second, use the "adjust_fan_speed" feature to set the fan speed to "medium", setting `variable_fan_speed` to "medium".

# Achieving the command involves:
# 1. Selecting the "power_on_off" feature and setting `variable_power_on_off = "on"`.
# 2. Selecting the "adjust_fan_speed" feature and setting `variable_fan_speed = "medium"`.

class ExtendedSimulator(Simulator): 
    pass