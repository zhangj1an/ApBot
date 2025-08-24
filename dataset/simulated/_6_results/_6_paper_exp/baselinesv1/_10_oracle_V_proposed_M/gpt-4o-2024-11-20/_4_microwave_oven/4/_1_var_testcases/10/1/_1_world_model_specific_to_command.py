# The current code accurately models the relevant appliance features as per the user manual.
# Below we list the sequence of features needed to achieve the command and the corresponding user manual text and feature_list names.

# Sequence of Features:
# 1. "adjust_upper_heater_temperature" - Set upper heater temperature to 190 °C.
# 2. "adjust_lower_heater_temperature" - Set lower heater temperature to 190 °C.
# 3. "adjust_timer" - Set timer to 20 minutes.
# 4. "select_function" - Select the upper heater function.

# Relevant User Manual Text:
# - "Upper and lower heaters temperature knobs: Temperature range: 70 °C - 230 °C"
# - "Timer: The electric oven beeps when the timer reaches '0'..."
# - "Function knob: □ Operates the upper heater"

# Relevant Feature_List Names:
# - "adjust_upper_heater_temperature"
# - "adjust_lower_heater_temperature"
# - "adjust_timer"
# - "select_function"

# Goal Variable Values:
# variable_upper_heater_temperature = 190
# variable_lower_heater_temperature = 190
# variable_timer = "20"
# variable_function_knob = "Upper Heater"

class ExtendedSimulator(Simulator): 
    pass