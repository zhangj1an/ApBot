# The given code seems to accurately model the appliance features needed for the user command.
# Sequence of features required to achieve the command:
# 1. "power_on_off" to turn the appliance on. 
#    - User manual: "Press the (power) POWER button to turn on and the (power) POWER symbol light will illuminate."
#    - Corresponding feature_list name in the given code: "power_on_off"
# 2. "adjust_fan_speed" to change the fan speed to "medium".
#    - User manual: "Press the (fan speed) FAN SPEED button repeatedly until the desired speed is illuminated on the control panel. There are 4 fan speeds: Low, Medium, High and Turbo."
#    - Corresponding feature_list name in the given code: "adjust_fan_speed"

# Goal variable values to achieve this command:
# - Set variable_power_on_off to "on"
# - Set variable_fan_speed to "medium"

class ExtendedSimulator(Simulator):
    pass