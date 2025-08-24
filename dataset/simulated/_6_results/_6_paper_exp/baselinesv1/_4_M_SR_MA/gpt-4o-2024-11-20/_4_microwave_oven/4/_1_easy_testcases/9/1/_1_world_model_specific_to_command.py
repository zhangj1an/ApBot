# The provided code is already correct to execute the user's command. Here's the explanation:

# Sequence of features needed to achieve the command:
# 1. Adjust the function knob to "Lower Heater".
#    - User manual text describes: "Function knob ... □ Operates the lower heater".
#    - Feature name in provided code: "set_function_knob".
# 2. Set the upper heater temperature to 110°C.
#    - User manual text describes: "**Upper and lower heaters temperature knobs:** Temperature range: 70°C - 230°C".
#    - Feature name in provided code: "adjust_upper_heater_temperature".
# 3. Set the lower heater temperature to 110°C.
#    - User manual text describes: "**Upper and lower heaters temperature knobs:** Temperature range: 70°C - 230°C".
#    - Feature name in provided code: "adjust_lower_heater_temperature".
# 4. Set the timer to 60 minutes.
#    - User manual text describes: "**Timer:** The electric oven beeps when the timer reaches '0'. ..."
#    - Feature name in provided code: "set_timer".

# Goal variable values to achieve the command:
# - Set variable_function_knob to "Lower Heater".
# - Set variable_upper_heater_temperature to "110".
# - Set variable_lower_heater_temperature to "110".
# - Set variable_timer to "60".

class ExtendedSimulator(Simulator):
    pass