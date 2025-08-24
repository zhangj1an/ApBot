# Python comment
# The current code accurately models the relevant appliance feature to achieve the requested user command.
# Sequence of relevant features needed to achieve the user command:
# 1. "power_and_start_warming": This feature models toggling the appliance power state to "on".
# 2. "select_bottle_type": This feature models cycling through bottle types to select "Milk bag".
# 3. "select_initial_temperature": This feature models cycling through initial temperatures to select "Frozen".
# 4. "select_volume": This feature models cycling through volume options to select "4-6 fl-oz".
#
# Raw text from the user manual describing the relevant features: 
# - **ON/OFF:** Press this button to turn on the appliance and the light is on. Press again to turn it off and the light is off.
# - | Select bottle | Select initial temp       | Select Volume |
#   |---------------|---------------------------|---------------|
#   | Milk bag      | Room- 25℃ (77℉)           | 1-3 fl- oz    |
#   | Plastic       | Refrig- 4℃ (39.2℉)        | 4-6 fl- oz    |
#   | Silicone      | Frozen- 0℃ (32℉)          | 7+ fl- oz     |
#
# Feature list needed from the current code:
# - "power_and_start_warming": Sets "variable_power_on_off" to "on" and "variable_start_running" to "on".
# - "select_bottle_type": Adjusts "variable_bottle_type" to "Milk bag".
# - "select_initial_temperature": Adjusts "variable_initial_temp" to "Frozen".
# - "select_volume": Adjusts "variable_volume" to "4-6 fl-oz".
#
# Goal Variable Values:
# - variable_power_on_off: "on"
# - variable_start_running: "on"
# - variable_bottle_type: "Milk bag"
# - variable_initial_temp: "Frozen"
# - variable_volume: "4-6 fl-oz"

class ExtendedSimulator(Simulator):
    pass