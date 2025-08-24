# Python comments below explain the validity of the current code and the list of features needed to achieve this command.

# The current code correctly models the appliance features as per the user manual.
# It includes variables for setting the upper and lower heater temperatures, the timer, and the function knob.
# These are the relevant features mentioned in the user manual:
# ● Adjusting upper and lower heater temperatures is modeled as "adjust_upper_heater_temperature"
# and "adjust_lower_heater_temperature".
# ● Setting the timer is modeled as "adjust_timer".
# ● Selecting the function (including "Upper Heater" function) is modeled as "select_function".
# All these features are accurate for achieving the user command.

# Sequence of features needed:
# 1. Feature "adjust_upper_heater_temperature" to set the upper heater temperature to 150 °C.
# 2. Feature "adjust_lower_heater_temperature" to set the lower heater temperature to 150 °C.
# 3. Feature "adjust_timer" to set the timer to 60 minutes.
# 4. Feature "select_function" to set the function knob to "Upper Heater".

# Relevant user manual texts:
# - "● Upper and lower heaters temperature knobs: Temperature range: 70 °C - 230 °C."
# - "● Timer: The electric oven beeps when the timer reaches '0'."
# - "● Function knob: Select the proper function for heating, such as 'Lower & Upper heater at the same time' or 'Upper Heater heating'."

# The feature_list names in the given code are:
# - "adjust_upper_heater_temperature"
# - "adjust_lower_heater_temperature"
# - "adjust_timer"
# - "select_function"

# Goal variable values to achieve the command:
# - Set variable_upper_heater_temperature to 150.
# - Set variable_lower_heater_temperature to 150.
# - Set variable_timer to "60".
# - Set variable_function_knob to "Upper Heater".

class ExtendedSimulator(Simulator): 
    pass