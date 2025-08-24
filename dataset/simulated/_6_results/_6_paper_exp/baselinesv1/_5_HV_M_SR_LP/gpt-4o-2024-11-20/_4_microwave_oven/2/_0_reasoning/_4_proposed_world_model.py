class Simulator(Appliance):

    def reset(self):
        # Initialize features and variables
        self.feature = Feature(
            feature_list={
                "set_upper_element_temperature": [
                    {"step": 1, "actions": ["turn_upper_element_temperature_dial_clockwise", "turn_upper_element_temperature_dial_anticlockwise"], "variable": "variable_upper_element_temperature"}
                ],
                "set_lower_element_temperature": [
                    {"step": 1, "actions": ["turn_lower_element_temperature_dial_clockwise", "turn_lower_element_temperature_dial_anticlockwise"], "variable": "variable_lower_element_temperature"}
                ],
                "set_function_dial": [
                    {"step": 1, "actions": ["turn_function_dial_clockwise", "turn_function_dial_anticlockwise"], "variable": "variable_function_dial"}
                ],
                "set_timer": [
                    {"step": 1, "actions": ["turn_timer_dial_clockwise", "turn_timer_dial_anticlockwise"], "variable": "variable_timer"}
                ],
                "null": [
                    {"step": 1, "actions": [], "missing_variables": []}
                ]
            },
            current_value=("empty", 1)
        )
        self.variable_upper_element_temperature = variable_upper_element_temperature
        self.variable_lower_element_temperature = variable_lower_element_temperature
        self.variable_function_dial = variable_function_dial
        self.variable_timer = variable_timer

    # Action: Turn upper element temperature dial clockwise
    def turn_upper_element_temperature_dial_clockwise(self):
        # Update feature progress and adjust the variable
        self.feature.update_progress("turn_upper_element_temperature_dial_clockwise")
        current_feature = self.feature.current_value[0]
        if current_feature == "set_upper_element_temperature":
            self.execute_action_and_set_next("turn_upper_element_temperature_dial_clockwise")

    # Action: Turn upper element temperature dial anticlockwise
    def turn_upper_element_temperature_dial_anticlockwise(self):
        # Update feature progress and adjust the variable
        self.feature.update_progress("turn_upper_element_temperature_dial_anticlockwise")
        current_feature = self.feature.current_value[0]
        if current_feature == "set_upper_element_temperature":
            self.execute_action_and_set_prev("turn_upper_element_temperature_dial_anticlockwise")

    # Action: Turn lower element temperature dial clockwise
    def turn_lower_element_temperature_dial_clockwise(self):
        # Update feature progress and adjust the variable
        self.feature.update_progress("turn_lower_element_temperature_dial_clockwise")
        current_feature = self.feature.current_value[0]
        if current_feature == "set_lower_element_temperature":
            self.execute_action_and_set_next("turn_lower_element_temperature_dial_clockwise")

    # Action: Turn lower element temperature dial anticlockwise
    def turn_lower_element_temperature_dial_anticlockwise(self):
        # Update feature progress and adjust the variable
        self.feature.update_progress("turn_lower_element_temperature_dial_anticlockwise")
        current_feature = self.feature.current_value[0]
        if current_feature == "set_lower_element_temperature":
            self.execute_action_and_set_prev("turn_lower_element_temperature_dial_anticlockwise")

    # Action: Turn function dial clockwise
    def turn_function_dial_clockwise(self):
        # Update feature progress and adjust the variable
        self.feature.update_progress("turn_function_dial_clockwise")
        current_feature = self.feature.current_value[0]
        if current_feature == "set_function_dial":
            self.execute_action_and_set_next("turn_function_dial_clockwise")

    # Action: Turn function dial anticlockwise
    def turn_function_dial_anticlockwise(self):
        # Update feature progress and adjust the variable
        self.feature.update_progress("turn_function_dial_anticlockwise")
        current_feature = self.feature.current_value[0]
        if current_feature == "set_function_dial":
            self.execute_action_and_set_prev("turn_function_dial_anticlockwise")

    # Action: Turn timer dial clockwise
    def turn_timer_dial_clockwise(self):
        # Update feature progress and adjust the variable
        self.feature.update_progress("turn_timer_dial_clockwise")
        current_feature = self.feature.current_value[0]
        if current_feature == "set_timer":
            self.execute_action_and_set_next("turn_timer_dial_clockwise")

    # Action: Turn timer dial anticlockwise
    def turn_timer_dial_anticlockwise(self):
        # Update feature progress and adjust the variable
        self.feature.update_progress("turn_timer_dial_anticlockwise")
        current_feature = self.feature.current_value[0]
        if current_feature == "set_timer":
            self.execute_action_and_set_prev("turn_timer_dial_anticlockwise")