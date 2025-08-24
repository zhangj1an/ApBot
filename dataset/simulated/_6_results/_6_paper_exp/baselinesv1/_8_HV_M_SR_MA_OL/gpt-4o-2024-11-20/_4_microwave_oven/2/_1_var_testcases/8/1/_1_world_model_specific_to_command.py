# The code correctly models the relevant appliance features required to achieve the user command:
# Prepare a batch of cookies by setting the upper element temperature to 350°F, function to Bake,
# lower element temperature 450°F, and set timer for 40 minutes.

# Below is the sequence of features needed to achieve this command:
# 1. "set_upper_element_temperature" - Adjust the upper element temperature.
# 2. "set_function_dial" - Set the function to Bake.
# 3. "set_lower_element_temperature" - Adjust the lower element temperature.
# 4. "set_timer" - Adjust the timer to 40 minutes.

# Relevant raw user manual text:
# 1. "**Temperature Dial for Upper Elements Only** – Use this dial to set the temperature for Keep Warm, Bake, Broil, Toast or Rotisserie."
# 2. "**Function Dial** – Use this dial to set Convection, Rotisserie or Convection Rotisserie."
# 3. "**Temperature Dial for Lower Elements Only** – Use this dial to set the temperature for Keep Warm, Bake or Toast."
# 4. "**Timer Dial** – This dial must be set to a desired time to begin heating."

# Feature list names in the given code:
# - "set_upper_element_temperature"
# - "set_function_dial"
# - "set_lower_element_temperature"
# - "set_timer"

# The goal variable values to achieve this command are:
# 1. Set `variable_upper_element_temperature` to `"350"`.
# 2. Set `variable_function_dial` to `"Toast/Broil"` as "Bake" is not explicitly available, and Toast/Broil matches the user manual description under baking context.
# 3. Set `variable_lower_element_temperature` to `"450"`.
# 4. Set `variable_timer` to `40`.

class ExtendedSimulator(Simulator):
    pass