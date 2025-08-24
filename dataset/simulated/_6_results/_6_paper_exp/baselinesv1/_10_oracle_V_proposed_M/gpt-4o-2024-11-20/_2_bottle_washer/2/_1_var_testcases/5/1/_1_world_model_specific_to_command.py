# Raw User Manual Text:
# 1. "Press this button to turn on the appliance and the light is on. Press again to turn it off and the light is off."
# 2. "| Select bottle | Select initial temp | Select Volume |
#      |--------------|---------------------|---------------|
#      | Milk bag     | Room- 25℃ (77℉)    | 1-3 fl- oz    |
#      | Plastic      | Refrig- 4℃ (39.2℉) | 4-6 fl- oz    |
#      | Silicone     | Frozen- 0℃ (32℉)   | 7+ fl- oz     |"

# The given code correctly covers all steps and variables required for the user command:
# Features required:
# 1. "power_toggle_or_start_warming": To turn on the appliance.
# 2. "adjust_bottle_type": To select "Plastic" bottle type.
# 3. "adjust_initial_temp": To set the initial temperature to "Room" (25℃).
# 4. "adjust_volume": To set the volume to "1-3 fl-oz."

# Relevant feature_list names: 
# - "power_toggle_or_start_warming"
# - "adjust_bottle_type"
# - "adjust_initial_temp"
# - "adjust_volume"

# Goal variable values to achieve the command:
# - variable_power_on_off: "on"
# - variable_bottle_type: "Plastic"
# - variable_initial_temp: "Room"
# - variable_volume: "1-3 fl-oz"

class ExtendedSimulator(Simulator): 
    pass