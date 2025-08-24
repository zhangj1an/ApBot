# The current code accurately models the relevant appliance features needed to achieve the user command.
# Sequence of features needed to achieve this command:
# 1. "set_upper_element_temperature"
# 2. "set_lower_element_temperature"
# 3. "set_function_dial"
# 4. "set_timer"

# Relevant user manual sections:
# **1. Temperature Dial for Upper Elements Only** – "Use this dial to set the temperature for Keep Warm, Bake, Broil, Toast or Rotisserie."
# (Models "set_upper_element_temperature")
# **2. Temperature Dial for Lower Elements Only** – "Use this dial to set the temperature for Keep Warm, Bake or Toast."
# (Models "set_lower_element_temperature")
# **3. Function Dial** – "Use this dial to set Convection, Rotisserie or Convection Rotisserie."
# (Models "set_function_dial")
# **4. Timer Dial** – "This dial must be set to a desired time to begin heating."
# (Models "set_timer")

# Feature list names in the current code:
# - "set_upper_element_temperature"
# - "set_lower_element_temperature"
# - "set_function_dial"
# - "set_timer"

# Goal variable values to achieve this command:
# - variable_upper_element_temperature set to "350"
# - variable_lower_element_temperature set to "450"
# - variable_function_dial set to "Convection"
# - variable_timer set to 30

class ExtendedSimulator(Simulator): 
    pass