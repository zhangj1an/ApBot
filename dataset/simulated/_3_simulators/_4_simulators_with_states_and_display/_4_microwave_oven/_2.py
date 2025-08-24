# 4 variables

# Variable for upper element temperature
variable_upper_element_temperature = DiscreteVariable(
    value_range=["off", "Keep Warm", "250°F", "350°F", "450°F"],
    current_value="off"
)

# Variable for function dial
variable_function = DiscreteVariable(
    value_range=["Off", "Convection", "Rotisserie", "Convection Rotisserie", "Toast/Broil", "Bake"],
    current_value="Off"
)

# Variable for lower element temperature
variable_lower_element_temperature = DiscreteVariable(
    value_range=["off", "Keep Warm", "250°F", "350°F", "450°F"],
    current_value="off"
)

# Variable for timer
variable_timer = DiscreteVariable(
    value_range=["off", "10", "20", "30", "40", "50", "60"],
    current_value="off"
)


feature_list = {}

feature_list["adjust_upper"] = [
    {"step": 1, "actions": ["turn_upper_element_temperature_dial_clockwise", "turn_upper_element_temperature_dial_anticlockwise"], "variable": "variable_upper_element_temperature", "step_size": 5}
]

feature_list["adjust_lower"] = [
    {"step": 1, "actions": ["turn_lower_element_temperature_dial_clockwise", "turn_lower_element_temperature_dial_anticlockwise"], "variable": "variable_lower_element_temperature", "step_size": 5},
]

feature_list["adjust_timer"] = [
    {"step": 1, "actions": ["turn_timer_dial_clockwise", "turn_timer_dial_anticlockwise"], "variable": "variable_timer", "step_size": 7}
]

feature_list["adjust_function"] = [
    {"step": 1, "actions": ["turn_function_dial_clockwise", "turn_function_dial_anticlockwise"], "variable": "variable_function", "step_size": 6},
    
]

simulator_feature = Feature(feature_list=feature_list, current_value=("empty", 1))

class Simulator(Appliance):

    def reset(self):
        self.feature = simulator_feature
        self.variable_upper_element_temperature = variable_upper_element_temperature
        self.variable_function = variable_function
        self.variable_lower_element_temperature = variable_lower_element_temperature
        self.variable_timer = variable_timer

    def turn_upper_element_temperature_dial_clockwise(self):
        # Update feature progress and adjust the upper element temperature to the next setting
        self.feature.update_progress("turn_upper_element_temperature_dial_clockwise")
        self.execute_action_and_set_next("turn_upper_element_temperature_dial_clockwise")

    def turn_upper_element_temperature_dial_anticlockwise(self):
        # Update feature progress and adjust the upper element temperature to the previous setting
        self.feature.update_progress("turn_upper_element_temperature_dial_anticlockwise")
        self.execute_action_and_set_prev("turn_upper_element_temperature_dial_anticlockwise")

    def turn_function_dial_clockwise(self):
        # Update feature progress and adjust the function to the next setting
        self.feature.update_progress("turn_function_dial_clockwise")
        self.execute_action_and_set_next("turn_function_dial_clockwise")

    def turn_function_dial_anticlockwise(self):
        # Update feature progress and adjust the function to the previous setting
        self.feature.update_progress("turn_function_dial_anticlockwise")
        self.execute_action_and_set_prev("turn_function_dial_anticlockwise")

    def turn_lower_element_temperature_dial_clockwise(self):
        # Update feature progress and adjust the lower element temperature to the next setting
        self.feature.update_progress("turn_lower_element_temperature_dial_clockwise")
        self.execute_action_and_set_next("turn_lower_element_temperature_dial_clockwise")

    def turn_lower_element_temperature_dial_anticlockwise(self):
        # Update feature progress and adjust the lower element temperature to the previous setting
        self.feature.update_progress("turn_lower_element_temperature_dial_anticlockwise")
        self.execute_action_and_set_prev("turn_lower_element_temperature_dial_anticlockwise")

    def turn_timer_dial_clockwise(self):
        # Update feature progress and adjust the timer to the next setting
        self.feature.update_progress("turn_timer_dial_clockwise")
        self.execute_action_and_set_next("turn_timer_dial_clockwise")

    def turn_timer_dial_anticlockwise(self):
        # Update feature progress and adjust the timer to the previous setting
        self.feature.update_progress("turn_timer_dial_anticlockwise")
        self.execute_action_and_set_prev("turn_timer_dial_anticlockwise")
