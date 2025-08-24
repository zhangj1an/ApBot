# 4 variables

# Variable for upper tube temperature adjustment
variable_upper_tube_temperature = ContinuousVariable(value_ranges_steps=[(0, 70, 70), (70, 230, 40)], current_value=0)

# Variable for function selection
variable_function_selection = DiscreteVariable(value_range=[
    "lower heating tube", 
    "upper heating tube", 
    "upper and lower heating tube", 
    "upper and lower heating tube with convection", 
    "upper heating tube with Rotisserie Motor"
], current_value="lower heating tube")

# Variable for lower tube temperature adjustment
variable_lower_tube_temperature = ContinuousVariable(value_ranges_steps=[(0, 70, 70), (70, 230, 40)], current_value=0)

# Variable for time adjustment
variable_time_adjustment = ContinuousVariable(value_ranges_steps=[(0, 60, 10)], current_value=0)

feature_list = {}

feature_list["adjust_upper_tube_temperature"] = [
    {"step": 1, "actions": ["turn_upper_tube_temperature_adjustment_dial_clockwise", "turn_upper_tube_temperature_adjustment_dial_anticlockwise"], "variable": "variable_upper_tube_temperature", "step_size": 6}
]

feature_list["adjust_lower_tube_temperature"] = [
    {"step": 1, "actions": ["turn_lower_tube_temperature_adjustment_dial_clockwise", "turn_lower_tube_temperature_adjustment_dial_anticlockwise"], "variable": "variable_lower_tube_temperature", "step_size": 6}
]

feature_list["select_cooking_function"] = [
    {"step": 1, "actions": ["turn_function_selection_dial_clockwise", "turn_function_selection_dial_anticlockwise"], "variable": "variable_function_selection", "step_size": 5}
]

feature_list["adjust_cooking_time"] = [
    {"step": 1, "actions": ["turn_time_adjustment_dial_clockwise", "turn_time_adjustment_dial_anticlockwise"], "variable": "variable_time_adjustment", "step_size": 7}
]

simulator_feature = Feature(feature_list=feature_list, current_value=("empty", 1))

class Simulator(Appliance):

    def reset(self):
        self.feature = simulator_feature
        self.variable_upper_tube_temperature = variable_upper_tube_temperature
        self.variable_function_selection = variable_function_selection
        self.variable_lower_tube_temperature = variable_lower_tube_temperature
        self.variable_time_adjustment = variable_time_adjustment

    def turn_function_selection_dial_anticlockwise(self):
        # Update feature and adjust the function selection variable to the previous value
        self.feature.update_progress("turn_function_selection_dial_anticlockwise")
        self.execute_action_and_set_prev("turn_function_selection_dial_anticlockwise")

    def turn_function_selection_dial_clockwise(self):
        # Update feature and adjust the function selection variable to the next value
        self.feature.update_progress("turn_function_selection_dial_clockwise")
        self.execute_action_and_set_next("turn_function_selection_dial_clockwise")

    def turn_lower_tube_temperature_adjustment_dial_anticlockwise(self):
        # Update feature and adjust the lower tube temperature variable to the previous value
        self.feature.update_progress("turn_lower_tube_temperature_adjustment_dial_anticlockwise")
        self.execute_action_and_set_prev("turn_lower_tube_temperature_adjustment_dial_anticlockwise")

    def turn_lower_tube_temperature_adjustment_dial_clockwise(self):
        # Update feature and adjust the lower tube temperature variable to the next value
        self.feature.update_progress("turn_lower_tube_temperature_adjustment_dial_clockwise")
        self.execute_action_and_set_next("turn_lower_tube_temperature_adjustment_dial_clockwise")

    def turn_upper_tube_temperature_adjustment_dial_anticlockwise(self):
        # Update feature and adjust the upper tube temperature variable to the previous value
        self.feature.update_progress("turn_upper_tube_temperature_adjustment_dial_anticlockwise")
        self.execute_action_and_set_prev("turn_upper_tube_temperature_adjustment_dial_anticlockwise")

    def turn_upper_tube_temperature_adjustment_dial_clockwise(self):
        # Update feature and adjust the upper tube temperature variable to the next value
        self.feature.update_progress("turn_upper_tube_temperature_adjustment_dial_clockwise")
        self.execute_action_and_set_next("turn_upper_tube_temperature_adjustment_dial_clockwise")

    def turn_time_adjustment_dial_anticlockwise(self):
        # Update feature and adjust the time adjustment variable to the previous value
        self.feature.update_progress("turn_time_adjustment_dial_anticlockwise")
        self.execute_action_and_set_prev("turn_time_adjustment_dial_anticlockwise")

    def turn_time_adjustment_dial_clockwise(self):
        # Update feature and adjust the time adjustment variable to the next value
        self.feature.update_progress("turn_time_adjustment_dial_clockwise")
        self.execute_action_and_set_next("turn_time_adjustment_dial_clockwise")