# The given code already correctly models all features and variable adjustments necessary to accomplish the user command. 
# For the user command, the following sequence of actions is required:

# 1. Set the function knob to "Convection"
#    Relevant user manual text: "Set the function knob: ⌛ Convection (Lower & upper heater heating)"
#    Feature: "set_function_knob"

# 2. Adjust the upper heater temperature to 190 °C
#    Relevant user manual text: "The Upper and lower heater temperature knobs must be set to the same temperature at the same time."
#    Feature: "adjust_upper_heater_temperature"

# 3. Adjust the lower heater temperature to 190 °C
#    Relevant user manual text: "The Upper and lower heater temperature knobs must be set to the same temperature at the same time."
#    Feature: "adjust_lower_heater_temperature"

# 4. Set the timer to 20 minutes
#    Relevant user manual text: "Set baking time less than 20 minutes, turn up the knob beyond 40 minutes then return to the desired time."
#    Feature: "set_timer"

# Goal variable values to achieve the command:
# - variable_function_knob = "Convection"
# - variable_upper_heater_temperature = 190
# - variable_lower_heater_temperature = 190
# - variable_timer = "20"

class ExtendedSimulator(Simulator): 
    pass