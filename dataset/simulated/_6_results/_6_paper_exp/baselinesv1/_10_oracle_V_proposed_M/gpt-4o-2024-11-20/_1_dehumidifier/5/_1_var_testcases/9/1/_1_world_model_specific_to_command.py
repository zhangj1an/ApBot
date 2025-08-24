# User manual text: "Turns the unit on and off."
# Feature and variable related: "toggle_power" mapped to "variable_power_on_off".

# User manual text: "Press to send the display to sleep. The unit will continue working on the low fan mode but the lights will turn off."
# Feature and variable related: "toggle_sleep_mode_or_reset_filter_timer" is mapped to "variable_sleep_mode" for toggling sleep mode.

# Sequence of features needed:
# 1. Execute feature: "toggle_power" to turn the device on.
# 2. Ensure the "variable_sleep_mode" is set to "off" under the feature "toggle_sleep_mode_or_reset_filter_timer".

# Goal variable values:
# 1. variable_power_on_off = "on".
# 2. variable_sleep_mode = "off".

class ExtendedSimulator(Simulator): 
    pass