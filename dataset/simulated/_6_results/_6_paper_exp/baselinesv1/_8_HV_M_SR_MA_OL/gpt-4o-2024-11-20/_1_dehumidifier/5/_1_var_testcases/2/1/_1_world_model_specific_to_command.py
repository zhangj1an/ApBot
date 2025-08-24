# The user manual clearly describes these features in straightforward steps. The current code already models "power_control" to turn the appliance on/off and "control_ion_generator" to toggle the ion generator. These features match the user command.

# Sequence of features needed to achieve the command:
# 1. "power_control" to turn on the appliance: achieved by the action "press_power_button".
# 2. "control_ion_generator" to toggle the ion generator to "on": achieved by the action "press_ion_button".

# User manual text:
# 1. Turning the unit on/off: "Turns the unit on and off."
# 2. Controlling the Ion Generator: "Turns the negative Ion generator on and off."

# Corresponding feature_list names in the current code:
# Feature 1: "power_control"
# Feature 2: "control_ion_generator"

# Goal variable values to achieve this command:
# - Set variable_power_on_off to "on".
# - Set variable_ion_generator to "on".

class ExtendedSimulator(Simulator): 
    pass