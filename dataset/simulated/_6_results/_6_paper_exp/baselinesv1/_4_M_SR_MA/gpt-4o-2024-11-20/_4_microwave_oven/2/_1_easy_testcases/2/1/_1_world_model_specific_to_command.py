# The user manual indicates all necessary features modeled for the user command are present.
# Here are the sequences of features needed to achieve the command:

# 1. Adjust upper element temperature to 450°F.
#    User manual: "**Temperature Dial for Upper Elements Only** – Use this dial to set the temperature…." 
#    Feature list name: "set_upper_element_temperature"

# 2. Set function dial to Toast/Broil.
#    User manual: "**Function Dial** – Use this dial to set Convection, Rotisserie, or Convection Rotisserie…"
#    Feature list name: "set_function_dial"

# 3. Adjust lower element temperature to 450°F.
#    User manual: "**Temperature Dial for Lower Elements Only** – Use this dial to set the temperature…."
#    Feature list name: "set_lower_element_temperature"

# 4. Set the timer to 10 minutes.
#    User manual: "**Timer Dial** – This dial must be set to a desired time to begin heating…."
#    Feature list name: "set_timer"

# Goal variable values:
# - variable_upper_element_temperature: "450"
# - variable_function_dial: "Toast/Broil"
# - variable_lower_element_temperature: "450"
# - variable_timer: 10

class ExtendedSimulator(Simulator): 
    pass