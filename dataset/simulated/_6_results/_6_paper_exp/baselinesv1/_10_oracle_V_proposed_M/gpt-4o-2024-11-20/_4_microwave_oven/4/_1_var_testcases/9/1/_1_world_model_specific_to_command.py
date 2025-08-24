# The given code already correctly models the described appliance features and variables as per the user manual. 
# Below is the verification and justification against the user manual:

# Steps to achieve the user command:
# 1. Set the upper heater temperature to 110 °C --> Feature: "adjust_upper_heater_temperature".
#    User Manual Text: "Upper and lower heaters temperature knobs: Temperature range: 70 °C - 230 °C".
# 2. Set the lower heater temperature to 110 °C --> Feature: "adjust_lower_heater_temperature".
#    User Manual Text: "Upper and lower heaters temperature knobs: Temperature range: 70 °C - 230 °C".
# 3. Set the timer to 60 minutes --> Feature: "adjust_timer".
#    User Manual Text: "Timer: The electric oven beeps when the timer reaches '0'."
#    (Note: The value "60" is in the valid timer range as discussed in the feature list).
# 4. Select the lower heater function --> Feature: "select_function".
#    User Manual Text: "Function knob: □ Operates the lower heater."
# 5. Each step in the feature list correctly describes the actions required for the user command.

# Goal Variable Values:
# 1. variable_upper_heater_temperature: Set to "110".
# 2. variable_lower_heater_temperature: Set to "110".
# 3. variable_timer: Set to "60".
# 4. variable_function_knob: Set to "Lower Heater".

# The existing code is accurate, and no new variables or features need to be added.
class ExtendedSimulator(Simulator): 
    pass