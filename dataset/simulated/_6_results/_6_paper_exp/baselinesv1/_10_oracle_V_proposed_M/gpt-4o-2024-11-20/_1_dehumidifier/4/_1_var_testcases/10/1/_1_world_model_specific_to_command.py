# The current implementation for the appliance accurately models the features relevant to the user's command.
# Here is the sequence of features and goal variable values needed to achieve the command:

# Features required:
# 1. Feature: "power_on_off" (turn the appliance on).
#    User manual: "Press the (power) POWER button to turn on and the (power) POWER symbol light will illuminate."
#    Feature in code: "power_on_off"
# 2. Feature: "adjust_fan_speed" (change the fan speed to "medium").
#    User manual: "Press the (fan speed) FAN SPEED button repeatedly until the desired speed is illuminated on the control panel. There are 4 fan speeds: Low, Medium, High and Turbo."
#    Feature in code: "adjust_fan_speed"

# Goal variable values:
# - Set variable_power_on_off to "on".
# - Set variable_fan_speed to "medium".

class ExtendedSimulator(Simulator): 
    pass