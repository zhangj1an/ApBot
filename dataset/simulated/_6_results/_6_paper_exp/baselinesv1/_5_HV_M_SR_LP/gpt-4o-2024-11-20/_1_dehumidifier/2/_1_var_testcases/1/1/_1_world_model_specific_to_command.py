# The given code for the Simulator correctly models the relevant appliance features to achieve the user command
# of powering on the dehumidifier and adjusting the fan speed to HIGH.

# According to the user manual:
# To power on/off the device: "Press the ⏻ button to turn on/off the unit."
# To adjust the fan speed: "Select the preferred fan speed (High, Medium, Low or Auto) by pressing the Fan Speed Control."

# The corresponding implemented feature_list from the given code for these functionalities:
# Feature: Power On/Off
# feature_list["power_on_off"] = [
#     {"step": 1, "actions": ["press_on_off_button"], "variable": "variable_power_on_off"}
# ]
# Feature: Set Fan Speed
# feature_list["set_fan_speed"] = [
#     {"step": 1, "actions": ["press_speed_uv_button"], "variable": "variable_fan_speed"}
# ]

# Sequence of features needed:
# 1. "power_on_off": Use "press_on_off_button" to toggle power.
# 2. "set_fan_speed": Use "press_speed_uv_button" to change fan speed to "HIGH".

# Goal variable values:
# variable_power_on_off: "on"
# variable_fan_speed: "HIGH"

class ExtendedSimulator(Simulator): 
    pass