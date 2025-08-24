# The existing code already models the relevant features and variables for the requested user command.

# Sequence of features needed to achieve the command:
# 1. Feature: "power_on_off" - Action: "press_on_off_button" to turn on the appliance.
#    - User manual: "Press the ⏻ button to turn on/off the unit."
#    - Code feature: feature_list["power_on_off"]
#
# 2. Feature: "adjust_fan_speed" - Action: "press_speed_uv_button" to set the fan speed to AUTO.
#    - User manual: "Select the preferred fan speed (High, Medium, Low or Auto) by pressing the [Fan] button."
#    - Code feature: feature_list["adjust_fan_speed"]
#
# Goal variable values:
# - variable_power_on_off: "on"
# - variable_fan_speed: "AUTO"

class ExtendedSimulator(Simulator):
    pass