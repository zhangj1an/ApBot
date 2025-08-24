# The current code correctly models the appliance features as per the user command.
# Relevant features based on the user manual:
# 1. To turn the dehumidifier (air purifier) on:
#    - The feature_list["power_on_off"] is relevant.
#    - User manual text: "Press the (power) POWER button to turn on and the (power) POWER symbol light will illuminate."
# 2. To change the fan speed to 'medium':
#    - The feature_list["adjust_fan_speed"] is relevant.
#    - User manual text: "Press the (fan speed) FAN SPEED button repeatedly until the desired speed is illuminated on the control panel. There are 4 fan speeds: Low, Medium, High and Turbo."
# Sequence of features to achieve the user command:
# 1. "power_on_off" -> Ensure the device is turned on.
# 2. "adjust_fan_speed" -> Set the fan speed to "medium."
# Goal variable values:
# - Set variable_power_on_off to "on".
# - Set variable_fan_speed to "medium".

class ExtendedSimulator(Simulator):
    pass