# The provided user command asks to perform the actions which are already accurately implemented in the existing
# code model. Below is the explanation and confirmation of relevant features and goal variables.

# The sequence of features needed to achieve the command:

# 1. Use "set_function_knob" to adjust and set the lower heater function.
#    - **Relevant user manual text:** "Function knob: □ Operates the lower heater."
#    - **Feature name in the code:** "set_function_knob"

# 2. Use "adjust_upper_heater_temperature" to adjust and set the upper heater temperature to 70 °C.
#    - **Relevant user manual text:** "Upper and lower heaters temperature knobs: Temperature range: 70 °C - 230 °C."
#    - **Feature name in the code:** "adjust_upper_heater_temperature"

# 3. Use "adjust_lower_heater_temperature" to adjust and set the lower heater temperature to 70 °C.
#    - **Relevant user manual text:** "Upper and lower heaters temperature knobs: Temperature range: 70 °C - 230 °C."
#    - **Feature name in the code:** "adjust_lower_heater_temperature"

# 4. Use "set_timer" and adjust the timer to 20 minutes.
#    - **Relevant user manual text:** "Timer: To set the baking time less than 20 minutes, turn up the knob beyond 40 minutes, then return to the desired time."
#    - **Feature name in the code:** "set_timer"

# Since no additional features or modifications are required, the provided command can already be executed successfully.

# Goal variable values to achieve this:
variable_function_knob.set_current_value("Lower Heater")
variable_upper_heater_temperature.set_current_value(70)
variable_lower_heater_temperature.set_current_value(70)
variable_timer.set_current_value("20")

# As the implementation in the provided code is accurate, no modifications are needed.

class ExtendedSimulator(Simulator):
    pass