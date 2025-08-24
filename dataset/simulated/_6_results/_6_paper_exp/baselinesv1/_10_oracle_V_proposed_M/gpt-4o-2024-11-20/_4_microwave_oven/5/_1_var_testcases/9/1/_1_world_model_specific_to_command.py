# The current code does not include features that explicitly start the microwave after setting all variables, as well as a feature to handle "variable_start_running".
# According to the user manual, there's an implicit need for the timer to automatically start heating when adjusted.

# Following the user manual:
# "Heating will commence immediately."
# This indicates the action to set the timer automatically begins the heating process (variable_start_running: set to "on").

# Below is the updated feature list to overwrite the "adjust_timer_dial" feature:
# It contains the required functionality for starting the microwave and setting timers along with the necessary variables and actions.

# Updated code to achieve the user command:
# Features updated and include starting the microwave operation alongside setting the timer.

updated_feature_list = feature_list

# Overwrite "adjust_timer_dial" with an updated implementation to incorporate the auto-start functionality
updated_feature_list["adjust_timer_dial"] = [
    {"step": 1, "actions": ["turn_timer_dial_clockwise", "turn_timer_dial_anticlockwise"], 
     "variable": "variable_timer_dial",
     "comment": "value always triggers heating (auto-start when dial is set)"}
]

# Adding the variable that governs whether the microwave starts running
variable_start_running = DiscreteVariable(
    value_range=["on", "off"],
    current_value="off"
)

class ExtendedSimulator(Simulator): 
    def reset(self):
        super().reset()
        self.feature = Feature(feature_list=updated_feature_list, current_value=("empty", 1)) 
        self.variable_start_running = variable_start_running  # Add the start_running variable

    # Modify "turn_timer_dial_clockwise" for auto-start functionality
    def turn_timer_dial_clockwise(self):
        # Update the feature progress and adjust the timer variable
        self.feature.update_progress("turn_timer_dial_clockwise")
        current_feature = self.feature.current_value[0]
        if current_feature == "adjust_timer_dial":
            # Rotate the dial to set the next timer value
            self.execute_action_and_set_next("turn_timer_dial_clockwise")
            # Automatically start the microwave when the timer is set
            self.variable_start_running.set_current_value("on")
            # Update display to reflect the timer and operation state

    # Modify "turn_timer_dial_anticlockwise" for auto-start functionality
    def turn_timer_dial_anticlockwise(self):
        # Update the feature progress and adjust the timer variable
        self.feature.update_progress("turn_timer_dial_anticlockwise")
        current_feature = self.feature.current_value[0]
        if current_feature == "adjust_timer_dial":
            # Rotate the dial to set the previous timer value
            self.execute_action_and_set_prev("turn_timer_dial_anticlockwise")
            # Automatically start the microwave when the timer is set
            self.variable_start_running.set_current_value("on")
            # Update display to reflect state

    # Goal variable values to achieve the user command:
    # 1. Set function dial to "Convection"
    # 2. Set temperature dial to "250°C"
    # 3. Set selector dial to "Bottom Heating"
    # 4. Set timer dial to "40 minutes" (auto-start microwave)
    # variable_function_dial: "Convection"
    # variable_temperature_dial: "250°C"
    # variable_selector_dial: "Bottom Heating"
    # variable_timer_dial: "40 minutes"
    # variable_start_running: "on"