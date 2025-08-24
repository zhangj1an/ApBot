# Python comments stating the sequence of features and goal variable values

# Sequence of features needed to achieve this command:
# 1. "power_toggle_or_start_warming": Turn on the appliance.
#    Raw user manual text: "**ON/OFF:** Press this button to turn on the appliance and the light is on. Press again to turn it off and the light is off."
# 2. "adjust_bottle_type": Set the bottle type to "Plastic".
#    Raw user manual text: "| Milk bag | Plastic | Silicone |"
# 3. "adjust_initial_temp": Set the initial temperature to "Refrig (4°C)".
#    Raw user manual text: "| Room | Refrig (4°C) | Frozen (0°C) |"
# 4. "adjust_volume": Set the volume to "4-6 fl-oz".
#    Raw user manual text: "| 1-3 fl-oz | 4-6 fl-oz | 7+ fl-oz |"
# 5. "power_toggle_or_start_warming": Start warming.
#    Raw user manual text: "3. Press the power button after selection and the device will start warming."

# Goal variable values:
# variable_power_on_off = "on"
# variable_bottle_type = "Plastic"
# variable_initial_temp = "Refrig"
# variable_volume = "4-6 fl-oz"
# variable_start_running = "on"

class ExtendedSimulator(Simulator): 
    pass