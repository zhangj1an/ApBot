# The given code correctly models the relevant appliance features for the user command.
# Sequence of features needed to achieve the command:
# 1. power_and_start_warming: Turn on the appliance and start warming.
#    - Relevant User Manual Text: "**ON/OFF:** Press this button to turn on the appliance and the light is on."
#    - Feature List Name: "power_and_start_warming".
# 2. select_bottle_type: Choose "Milk bag".
#    - Relevant User Manual Text: "| Milk bag | Room- 25℃ (77℉) | 1-3 fl- oz |".
#    - Feature List Name: "select_bottle_type".
# 3. select_initial_temperature: Choose "Frozen".
#    - Relevant User Manual Text: "| Silicone | Frozen- 0℃ (32℉) | 7+ fl- oz |".
#    - Feature List Name: "select_initial_temperature".
# 4. select_volume: Choose "4-6 fl-oz".
#    - Relevant User Manual Text: "| Plastic | Refrig- 4℃ (39.2℉) | 4-6 fl-oz |".
#    - Feature List Name: "select_volume".

# Goal variable values to achieve the command:
# - variable_power_on_off: "on"
# - variable_start_running: "on"
# - variable_bottle_type: "Milk bag"
# - variable_initial_temp: "Frozen"
# - variable_volume: "4-6 fl-oz"

class ExtendedSimulator(Simulator):
    pass