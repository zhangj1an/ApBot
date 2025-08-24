# The current code accurately models the features and variables necessary to fulfill the user command.
# The sequence of features needed to achieve the user command is:
# 1. "adjust_function_dial"
# 2. "adjust_temperature_dial"
# 3. "adjust_selector_dial"
# 4. "adjust_timer_dial"

# Relevant user manual text:
# - "Turn the Function dial clockwise to the desired operation."
# - "Turn the Temperature dial clockwise to the desired cooking temperature."
# - "Turn the Selector dial clockwise to select top heating, bottom heating or both."
# - "Turn the Timer dial clockwise to the desired cooking duration." 

# Relevant feature_list names in the given code:
# - "adjust_function_dial"
# - "adjust_temperature_dial"
# - "adjust_selector_dial"
# - "adjust_timer_dial"

# Goal variable values to achieve this command:
# - Set `variable_function_dial` to "Convection".
# - Set `variable_temperature_dial` to "250°C".
# - Set `variable_selector_dial` to "Top & Bottom Heating".
# - Set `variable_timer_dial` to "40 minutes".

class ExtendedSimulator(Simulator): 
    pass