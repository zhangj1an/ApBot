# The supplied code correctly models the relevant appliance features as described in the user manual:
# - To achieve the given user command, the following sequence of features is needed:
#   1. "set_function_knob"
#   2. "adjust_upper_heater_temperature"
#   3. "adjust_lower_heater_temperature"
#   4. "set_timer"
# - The corresponding goal variable values are:
#   - variable_function_knob = "Lower & Upper Heater"
#   - variable_upper_heater_temperature = 230
#   - variable_lower_heater_temperature = 230
#   - variable_timer = "40"

class ExtendedSimulator(Simulator): 
    pass