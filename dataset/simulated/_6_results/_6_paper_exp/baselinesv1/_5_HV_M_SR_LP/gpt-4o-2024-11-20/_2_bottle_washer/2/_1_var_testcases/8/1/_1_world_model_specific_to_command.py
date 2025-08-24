# User command: Turn on the bottle washer and use a plastic bottle at room temperature (25℃) with 7+ fl-oz.
# Checking features in the code against the user manual.

# The current code models all features needed to achieve the command described:
# 1) Turning on the bottle washer (relevant feature: "power_and_start_warming")
# 2) Selecting bottle type as plastic (relevant feature: "select_bottle_type")
# 3) Setting the initial temperature to room (relevant feature: "select_initial_temperature")
# 4) Setting the volume to 7+ fl-oz (relevant feature: "select_volume")

# The exact features in the code, mapped to the user manual:
# 1. From user manual: "**ON/OFF:** Press this button to turn on the appliance and the light is on. Press again to turn it off and the light is off."
#    Feature in the code: "power_and_start_warming"
#    Variable: `variable_power_on_off`
#
# 2. From user manual: "| Milk bag | Room- 25℃ (77℉) | 1-3 fl-oz |"
#    Feature in the code: "select_bottle_type" (for selecting plastic), "select_initial_temperature" (for room temperature), "select_volume" (for 7+ fl oz)
#    Variables: `variable_bottle_type`, `variable_initial_temp`, `variable_volume`

# Based on the analysis, the current code correctly models all relevant features for this user command.

# Sequence of features needed to achieve this command:
# 1) Use feature "power_and_start_warming" to turn on the appliance.
# 2) Use feature "select_bottle_type" to set the bottle type to 'Plastic'.
# 3) Use feature "select_initial_temperature" to set the initial temperature to 'Room'.
# 4) Use feature "select_volume" to set the volume to '7+ fl-oz'.

# Goal variable values:
# - `variable_power_on_off` = "on"
# - `variable_bottle_type` = "Plastic"
# - `variable_initial_temp` = "Room"
# - `variable_volume` = "7+ fl-oz"

class ExtendedSimulator(Simulator): 
    pass