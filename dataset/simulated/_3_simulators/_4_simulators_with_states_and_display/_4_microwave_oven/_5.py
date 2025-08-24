# 4 variables

# Variable for function dial
variable_function_dial = DiscreteVariable(
    value_range=["Off", "Convection", "Rotisserie", "Rotisserie & Convection"],
    current_value="Off"
)

# Variable for temperature dial
variable_temperature_dial = DiscreteVariable(
    value_range=["Off", "100°C", "150°C", "200°C", "250°C"],
    current_value="Off"
)

# Variable for selector dial
variable_selector_dial = DiscreteVariable(
    value_range=["Off", "Top Heating", "Bottom Heating", "Top & Bottom Heating"],
    current_value="Off"
)

# Variable for timer dial
variable_timer_dial = DiscreteVariable(
    value_range=["Off", "10", "20", "30", "40", "60"],
    current_value="Off"
)

feature_list = {}

feature_list["temp"] = [
    {"step": 1, "actions": ["turn_temperature_dial_clockwise", "turn_temperature_dial_anticlockwise"], "variable": "variable_temperature_dial", "step_size": 5},
]

feature_list["function"] = [
    {"step": 1, "actions": ["turn_function_dial_clockwise", "turn_function_dial_anticlockwise"], "variable": "variable_function_dial", "step_size": 4},
]

feature_list["selector"] = [
    {"step": 1, "actions": ["turn_selector_dial_clockwise", "turn_selector_dial_anticlockwise"], "variable": "variable_selector_dial", "step_size": 4},
]

feature_list["timer"] = [
    {"step": 1, "actions": ["turn_timer_dial_clockwise", "turn_timer_dial_anticlockwise"], "variable": "variable_timer_dial", "step_size": 6}
]


simulator_feature = Feature(feature_list=feature_list, current_value=("empty", 1))

class Simulator(Appliance):

    def reset(self):
        self.feature = simulator_feature
        self.variable_function_dial = variable_function_dial
        self.variable_temperature_dial = variable_temperature_dial
        self.variable_selector_dial = variable_selector_dial
        self.variable_timer_dial = variable_timer_dial

    def turn_function_dial_clockwise(self):
        # Update feature progress and adjust the function dial to the next setting
        self.feature.update_progress("turn_function_dial_clockwise")
        self.execute_action_and_set_next("turn_function_dial_clockwise")

    def turn_function_dial_anticlockwise(self):
        # Update feature progress and adjust the function dial to the previous setting
        self.feature.update_progress("turn_function_dial_anticlockwise")
        self.execute_action_and_set_prev("turn_function_dial_anticlockwise")

    def turn_temperature_dial_clockwise(self):
        # Update feature progress and adjust the temperature dial to the next setting
        self.feature.update_progress("turn_temperature_dial_clockwise")
        self.execute_action_and_set_next("turn_temperature_dial_clockwise")

    def turn_temperature_dial_anticlockwise(self):
        # Update feature progress and adjust the temperature dial to the previous setting
        self.feature.update_progress("turn_temperature_dial_anticlockwise")
        self.execute_action_and_set_prev("turn_temperature_dial_anticlockwise")

    def turn_selector_dial_clockwise(self):
        # Update feature progress and adjust the selector dial to the next setting
        self.feature.update_progress("turn_selector_dial_clockwise")
        self.execute_action_and_set_next("turn_selector_dial_clockwise")

    def turn_selector_dial_anticlockwise(self):
        # Update feature progress and adjust the selector dial to the previous setting
        self.feature.update_progress("turn_selector_dial_anticlockwise")
        self.execute_action_and_set_prev("turn_selector_dial_anticlockwise")

    def turn_timer_dial_clockwise(self):
        # Update feature progress and adjust the timer dial to the next setting
        self.feature.update_progress("turn_timer_dial_clockwise")
        self.execute_action_and_set_next("turn_timer_dial_clockwise")

    def turn_timer_dial_anticlockwise(self):
        # Update feature progress and adjust the timer dial to the previous setting
        self.feature.update_progress("turn_timer_dial_anticlockwise")
        self.execute_action_and_set_prev("turn_timer_dial_anticlockwise")