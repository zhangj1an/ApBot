# The code correctly models all the appliance features and variables related to the user's command based on the user manual.

# Sequence of features needed to achieve the command:
# 1. "power_on_off": Turn on the air purifier to enable its operation.
#    - User manual: "Press the (power) POWER button to turn on and the (power) POWER symbol light will illuminate."
#    - Feature list in the code: "power_on_off".
#
# 2. "adjust_fan_speed": Adjust the fan speed to "high".
#    - User manual: "Press the (fan speed) FAN SPEED button repeatedly until the desired speed is illuminated on the control panel. There are 4 fan speeds: Low, Medium, High and Turbo."
#    - Feature list in the code: "adjust_fan_speed".

# Goal variable values to achieve the command:
# - Set `variable_power_on_off` to "on".
# - Set `variable_fan_speed` to "high".

class ExtendedSimulator(Simulator): 
    pass