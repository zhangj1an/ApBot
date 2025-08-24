class Simulator(Appliance):

    def reset(self):
        # Initialize features and variables
        self.feature = Feature(
            feature_list={
                "adjust_upper_element_temperature": [
                    {"step": 1, "actions": ["turn_upper_element_temperature_dial_clockwise", "turn_upper_element_temperature_dial_anticlockwise"], "variable": "variable_upper_element_temperature"}
                ],
                "adjust_lower_element_temperature": [
                    {"step": 1, "actions": ["turn_lower_element_temperature_dial_clockwise", "turn_lower_element_temperature_dial_anticlockwise"], "variable": "variable_lower_element_temperature"}
                ],
                "adjust_function_dial": [
                    {"step": 1, "actions": ["turn_function_dial_clockwise", "turn_function_dial_anticlockwise"], "variable": "variable_function_dial"}
                ],
                "adjust_timer_dial": [
                    {"step": 1, "actions": ["turn_timer_dial_clockwise", "turn_timer_dial_anticlockwise"], "variable": "variable_timer"}
                ],
                "null": [
                    {"step": 1, "actions": [], "missing_variables": []}
                ]
            },
            current_value=("empty", 1)
        )
        self.variable_upper_element_temperature = DiscreteVariable(
            value_range=["OFF", "Keep Warm", "150", "250", "350", "450"],
            current_value="OFF"
        )
        self.variable_lower_element_temperature = DiscreteVariable(
            value_range=["OFF", "Keep Warm", "150", "250", "350", "450"],
            current_value="OFF"
        )
        self.variable_function_dial = DiscreteVariable(
            value_range=["OFF", "Toast/Broil", "Convection", "Rotisserie", "Convection Rotisserie"],
            current_value="OFF"
        )
        self.variable_timer = ContinuousVariable(
            value_ranges_steps=[[0, 60, 10]],
            current_value=0
        )

    # Action: Turn the upper element temperature dial clockwise
    def turn_upper_element_temperature_dial_clockwise(self):
        # Update feature progress and adjust the variable
        self.feature.update_progress("turn_upper_element_temperature_dial_clockwise")
        current_feature = self.feature.current_value[0]
        if current_feature == "adjust_upper_element_temperature":
            self.execute_action_and_set_next("turn_upper_element_temperature_dial_clockwise")

    # Action: Turn the upper element temperature dial anticlockwise
    def turn_upper_element_temperature_dial_anticlockwise(self):
        # Update feature progress and adjust the variable
        self.feature.update_progress("turn_upper_element_temperature_dial_anticlockwise")
        current_feature = self.feature.current_value[0]
        if current_feature == "adjust_upper_element_temperature":
            self.execute_action_and_set_prev("turn_upper_element_temperature_dial_anticlockwise")

    # Action: Turn the lower element temperature dial clockwise
    def turn_lower_element_temperature_dial_clockwise(self):
        # Update feature progress and adjust the variable
        self.feature.update_progress("turn_lower_element_temperature_dial_clockwise")
        current_feature = self.feature.current_value[0]
        if current_feature == "adjust_lower_element_temperature":
            self.execute_action_and_set_next("turn_lower_element_temperature_dial_clockwise")

    # Action: Turn the lower element temperature dial anticlockwise
    def turn_lower_element_temperature_dial_anticlockwise(self):
        # Update feature progress and adjust the variable
        self.feature.update_progress("turn_lower_element_temperature_dial_anticlockwise")
        current_feature = self.feature.current_value[0]
        if current_feature == "adjust_lower_element_temperature":
            self.execute_action_and_set_prev("turn_lower_element_temperature_dial_anticlockwise")

    # Action: Turn the function dial clockwise
    def turn_function_dial_clockwise(self):
        # Update feature progress and adjust the variable
        self.feature.update_progress("turn_function_dial_clockwise")
        current_feature = self.feature.current_value[0]
        if current_feature == "adjust_function_dial":
            self.execute_action_and_set_next("turn_function_dial_clockwise")

    # Action: Turn the function dial anticlockwise
    def turn_function_dial_anticlockwise(self):
        # Update feature progress and adjust the variable
        self.feature.update_progress("turn_function_dial_anticlockwise")
        current_feature = self.feature.current_value[0]
        if current_feature == "adjust_function_dial":
            self.execute_action_and_set_prev("turn_function_dial_anticlockwise")

    # Action: Turn the timer dial clockwise
    def turn_timer_dial_clockwise(self):
        # Update feature progress and adjust the variable
        self.feature.update_progress("turn_timer_dial_clockwise")
        current_feature = self.feature.current_value[0]
        if current_feature == "adjust_timer_dial":
            self.execute_action_and_set_next("turn_timer_dial_clockwise")

    # Action: Turn the timer dial anticlockwise
    def turn_timer_dial_anticlockwise(self):
        # Update feature progress and adjust the variable
        self.feature.update_progress("turn_timer_dial_anticlockwise")
        current_feature = self.feature.current_value[0]
        if current_feature == "adjust_timer_dial":
            self.execute_action_and_set_prev("turn_timer_dial_anticlockwise")