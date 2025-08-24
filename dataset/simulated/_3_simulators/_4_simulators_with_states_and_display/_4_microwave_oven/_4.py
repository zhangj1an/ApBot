# 4 variables

# Upper and lower heaters temperature knobs
variable_upper_heater_temperature = ContinuousVariable(value_ranges_steps=[(0, 70, 70), (70, 230, 40)], current_value=0)
variable_lower_heater_temperature = ContinuousVariable(value_ranges_steps=[(0, 70, 70), (70, 230, 40)], current_value=0)

# Timer
variable_timer = DiscreteVariable(value_range=["0", "20", "40", "60", "80", "100", "120", "Stay On"], current_value="0")

# Function knob
variable_function = DiscreteVariable(value_range=["Off", "Fermentation", "Lower heater", "Upper heater", "Lower & upper heater", "Convection", "Rotary"], current_value="Off")

feature_list = {}

feature_list["set_upper_heater_temperature"] = [
    {"step": 1, "actions": ["turn_upper_temp_dial_clockwise", "turn_upper_temp_dial_anticlockwise"], "variable": "variable_upper_heater_temperature", "step_size": 6}
]

feature_list["set_lower_heater_temperature"] = [
    {"step": 1, "actions": ["turn_lower_temp_dial_clockwise", "turn_lower_temp_dial_anticlockwise"], "variable": "variable_lower_heater_temperature", "step_size": 6}
]

feature_list["set_timer"] = [
    {"step": 1, "actions": ["turn_time_dial_clockwise", "turn_time_dial_anticlockwise"], "variable": "variable_timer", "step_size": 8}
]

feature_list["set_function"] = [
    {"step": 1, "actions": ["turn_function_dial_clockwise", "turn_function_dial_anticlockwise"], "variable": "variable_function", "step_size": 6}
]

simulator_feature = Feature(feature_list=feature_list, current_value=("empty", 1))

class Simulator(Appliance):

    def reset(self):
        self.feature = simulator_feature
        self.variable_upper_heater_temperature = variable_upper_heater_temperature
        self.variable_lower_heater_temperature = variable_lower_heater_temperature
        self.variable_timer = variable_timer
        self.variable_function = variable_function

    # Action to turn the upper temperature dial clockwise
    def turn_upper_temp_dial_clockwise(self):
        # Update feature progress
        self.feature.update_progress("turn_upper_temp_dial_clockwise")
        # Get the current variable to adjust
        current_variable = self.get_current_variable("turn_upper_temp_dial_clockwise")
        # Assign the variable to the next value
        self.assign_variable_to_next(current_variable)

    # Action to turn the upper temperature dial anticlockwise
    def turn_upper_temp_dial_anticlockwise(self):
        # Update feature progress
        self.feature.update_progress("turn_upper_temp_dial_anticlockwise")
        # Get the current variable to adjust
        current_variable = self.get_current_variable("turn_upper_temp_dial_anticlockwise")
        # Assign the variable to the previous value
        self.assign_variable_to_prev(current_variable)

    # Action to turn the lower temperature dial clockwise
    def turn_lower_temp_dial_clockwise(self):
        # Update feature progress
        self.feature.update_progress("turn_lower_temp_dial_clockwise")
        # Get the current variable to adjust
        current_variable = self.get_current_variable("turn_lower_temp_dial_clockwise")
        # Assign the variable to the next value
        self.assign_variable_to_next(current_variable)

    # Action to turn the lower temperature dial anticlockwise
    def turn_lower_temp_dial_anticlockwise(self):
        # Update feature progress
        self.feature.update_progress("turn_lower_temp_dial_anticlockwise")
        # Get the current variable to adjust
        current_variable = self.get_current_variable("turn_lower_temp_dial_anticlockwise")
        # Assign the variable to the previous value
        self.assign_variable_to_prev(current_variable)

    # Action to turn the timer dial clockwise
    def turn_time_dial_clockwise(self):
        # Update feature progress
        self.feature.update_progress("turn_time_dial_clockwise")
        # Get the current variable to adjust
        current_variable = self.get_current_variable("turn_time_dial_clockwise")
        # Assign the variable to the next value
        self.assign_variable_to_next(current_variable)

    # Action to turn the timer dial anticlockwise
    def turn_time_dial_anticlockwise(self):
        # Update feature progress
        self.feature.update_progress("turn_time_dial_anticlockwise")
        # Get the current variable to adjust
        current_variable = self.get_current_variable("turn_time_dial_anticlockwise")
        # Assign the variable to the previous value
        self.assign_variable_to_prev(current_variable)

    # Action to turn the function dial clockwise
    def turn_function_dial_clockwise(self):
        # Update feature progress
        self.feature.update_progress("turn_function_dial_clockwise")
        # Get the current variable to adjust
        current_variable = self.get_current_variable("turn_function_dial_clockwise")
        # Assign the variable to the next value
        self.assign_variable_to_next(current_variable)

    # Action to turn the function dial anticlockwise
    def turn_function_dial_anticlockwise(self):
        # Update feature progress
        self.feature.update_progress("turn_function_dial_anticlockwise")
        # Get the current variable to adjust
        current_variable = self.get_current_variable("turn_function_dial_anticlockwise")
        # Assign the variable to the previous value
        self.assign_variable_to_prev(current_variable)