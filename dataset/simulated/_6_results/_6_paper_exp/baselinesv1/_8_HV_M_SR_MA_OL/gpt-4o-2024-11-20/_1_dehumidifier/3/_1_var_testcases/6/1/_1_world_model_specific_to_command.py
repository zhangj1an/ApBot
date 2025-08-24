# Power up the dehumidifier and engage the Sleep mode for quieter operation during the night.

# User Manual Relevant Features:
# 1. Power Button: Turn air purifier on and off (variable_power_on_off).
#    - Feature: "power_control"
#    - User Manual Quote: "Power Button: Turn air purifier on and off."
#    - Feature name in the given code: "power_control"

# 2. Fan Speed/Mode Button: Press Speed/Mode to cycle through fan modes including "Sleep."
#    - Feature: "adjust_fan_speed_mode"
#    - User Manual Quote: "Fan Speed/Mode Button: Press the Speed/Mode button to cycle between fan speeds 1, 2, 3, Turbo, Auto, and Sleep mode."
#    - Feature name in the given code: "adjust_fan_speed_mode"

# Sequence of Features:
# - First, activate the appliance by turning the power on (variable_power_on_off: set to "on").
# - Then, adjust the fan speed/mode to "Sleep" (variable_fan_speed_mode: set to "Sleep").

# Goal Variable Values:
# - Set `variable_power_on_off` to "on" (power on the appliance).
# - Set `variable_fan_speed_mode` to "Sleep" (for quiet operation at night).

class ExtendedSimulator(Simulator): 
    pass