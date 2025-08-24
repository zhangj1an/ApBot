# The current code accurately models the appliance's features as described in the user manual. 
# Here is the explanation of the sequence of features needed to achieve the user command:
# 
# **User Command**: Turn on the microwave to make a quick toast. Set the upper heater temperature to 150 °C, the lower heater temperature to 150 °C, the timer to 60 minutes, and use the upper heater function.
#
# **Sequence of Features**:
# 1. Adjust the function knob to select the "Upper Heater" mode:
#    - Raw user manual text: "Function knob: □ Operates the upper heater".
#    - Feature in feature_list: `set_function_knob`.
#    - Goal variable value: `variable_function_knob = "Upper Heater"`
# 2. Adjust the upper heater temperature to 150 °C:
#    - Raw user manual text: "Upper heater temperature knob: Temperature range: 70 °C - 230 °C".
#    - Feature in feature_list: `adjust_upper_heater_temperature`.
#    - Goal variable value: `variable_upper_heater_temperature = 150`
# 3. Adjust the lower heater temperature to 150 °C:
#    - Raw user manual text: "Lower heater temperature knob: Temperature range: 70 °C - 230 °C".
#    - Feature in feature_list: `adjust_lower_heater_temperature`.
#    - Goal variable value: `variable_lower_heater_temperature = 150`
# 4. Set the timer to 60 minutes:
#    - Raw user manual text: "Timer: The electric oven beeps when the timer reaches '0'."
#    - Feature in feature_list: `set_timer`.
#    - Goal variable value: `variable_timer = "60"`

# The current code provides suitable features and variables to match the user's requirements. 
# The goal variable values to achieve this task are:
# - `variable_function_knob = "Upper Heater"`
# - `variable_upper_heater_temperature = 150`
# - `variable_lower_heater_temperature = 150`
# - `variable_timer = "60"`

class ExtendedSimulator(Simulator): 
    pass