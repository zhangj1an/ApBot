# The provided user manual text and code provided sufficiently model the relevant appliance features needed for this command.
# Below is the sequence of features and the goal variable values to achieve the user command:
# - Feature: "drying_only_function"
#   - Action: "press_drying_only_button" to adjust `variable_drying_only_duration` to "30 minutes".
# - Feature: "storage_function"
#   - Action: "press_storage_button" to enable `variable_storage_mode` ("on").

# Relevant user manual text:
# - "Drying only function: Press this button once for 30 minutes drying, twice for 40 minutes drying and three times for 50 minutes drying."
# - "Storage function: Press this button alongside any of the functions above to allow items to be stored in the steriliser."

# Relevant feature from the existing feature list:
# - "drying_only_function"
# - "storage_function"

# Goal variable values:
# - `variable_drying_only_duration` = "30 minutes"
# - `variable_storage_mode` = "on"

class ExtendedSimulator(Simulator):
    pass