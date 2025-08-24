# User command: Turn the dehumidifier on and adjust the fan speed to 'high.'

# The code correctly models the relevant appliance features according to the user manual.

# Sequence of features needed to achieve this command:
# 1. "power_control" to turn the dehumidifier on.
#    - User manual: "Turns the unit on and off."
#    - feature_list: "power_control"
# 2. "adjust_fan_speed" to adjust the fan speed to 'high.'
#    - User manual: "Fan/Air Speed (SPEED): 1. Low 2. Mid 3. High"
#    - feature_list: "adjust_fan_speed"

# Goal variable values:
# - Set variable_power_on_off to "on"
# - Set variable_fan_speed to "3" (high)

class ExtendedSimulator(Simulator): 
    pass