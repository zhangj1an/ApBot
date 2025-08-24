# The current code does not include any feature or variable related to toggling the appliance on or off,
# meaning that the appliance cannot be "turned on" or "turned off" as required by the user command.
# The user manual does not provide such a feature explicitly, so we do not add this non-existent feature.

# The current code has appropriately modeled the relevant appliance features to adjust the heater temperatures,
# select a timer, and choose a function knob. Quoting the relevant user manual text:

# 1. **Upper and lower heater temperature control (Variable: variable_upper_heater_temperature, variable_lower_heater_temperature)**:
#    - "Upper and lower heaters temperature knobs: Temperature range: 70°C - 230°C",
#    - Feature modeled: "adjust_upper_heater_temperature" and "adjust_lower_heater_temperature".

# 2. **Timer adjustment (Variable: variable_timer)**:
#    - "Timer: The electric oven beeps when the timer reaches '0'. Tips: to set baking time less than 20 minutes, turn up the knob beyond 40 minutes then return to the desired time."
#    - Feature modeled: "adjust_timer".

# 3. **Function knob adjustment (Variable: variable_function_knob)**:
#    - "Function knob: □ Operates the lower heater □ Operates the upper heater □ Operates the lower & upper heater at the same time ⌛ Convection".
#    - Feature modeled: "select_function".

# Therefore, the appropriate sequence of features to achieve the user's command is:
# Feature sequence:
# 1. "adjust_upper_heater_temperature" to set variable_upper_heater_temperature to "70 °C".
# 2. "adjust_lower_heater_temperature" to set variable_lower_heater_temperature to "70 °C".
# 3. "adjust_timer" to set variable_timer to "80" (Note: The timer's variable must have "80" added as an intermediate value).
# 4. "select_function" to set variable_function_knob to "Lower & Upper Heater".

# Updated Variables and Features required:
# The timer variable currently does not have the intermediate value "80" modeled. Thus, we need to append this value to its range.

# Extend the Simulator class and add the adjusted feature list and timer value range to match the user's command:

updated_variable_timer = DiscreteVariable(
    value_range=["0", "20", "40", "60", "80", "100", "120", "Stay On"],  # Added "80" for customization
    current_value="0"
)

updated_feature_list = feature_list
updated_feature_list["adjust_timer"] = [
    {"step": 1, "actions": ["turn_time_dial_clockwise", "turn_time_dial_anticlockwise"], "variable": "variable_timer"}
]

class ExtendedSimulator(Simulator):
    def reset(self):
        # Initialize features and updated variables
        super().reset()

        # Override feature list with modified version
        self.feature = Feature(feature_list=updated_feature_list, current_value=("empty", 1))

        # Override variable_timer to include "80" as a valid value
        self.variable_timer = updated_variable_timer

# This command can now be achieved by setting the following variables to the goal state:
# Goal Variable Values:
# - variable_upper_heater_temperature: 70°C
# - variable_lower_heater_temperature: 70°C
# - variable_timer: "80"
# - variable_function_knob: "Lower & Upper Heater"