# The current code already models all the required appliance features correctly to achieve the command. 
# Below is the sequence of features needed to execute the user command:

# 1. **Set the function knob to "Lower & Upper Heater"**:
#    - User Manual: "The function knob operates the lower heater, upper heater, or both lower & upper heater at the same time."
#    - Relevant feature_list name: `set_function_knob`.

# 2. **Set the upper heater temperature to 110°C**:
#    - User Manual: "Upper and lower heaters temperature knobs: Temperature range: 70 °C - 230 °C."
#    - Relevant feature_list name: `adjust_upper_heater_temperature`.

# 3. **Set the lower heater temperature to 110°C**:
#    - User Manual: "Upper and lower heaters temperature knobs: Temperature range: 70 °C - 230 °C."
#    - Relevant feature_list name: `adjust_lower_heater_temperature`.

# 4. **Set the timer to 20 minutes**:
#    - User Manual: "Timer: To set baking time less than 20 minutes, turn up the knob beyond 40 minutes then return to the desired time."
#    - Relevant feature_list name: `set_timer`.

# The goal variable values to achieve this command are:
# - `variable_function_knob` = "Lower & Upper Heater"
# - `variable_upper_heater_temperature` = 110
# - `variable_lower_heater_temperature` = 110
# - `variable_timer` = "20"

class ExtendedSimulator(Simulator): 
    pass