class Simulator(Appliance):

    def reset(self):
        # Initialize feature and variables
        self.feature = Feature(feature_list={
            "adjust_lower_tube_temperature": [
                {"step": 1, "actions": ["turn_lower_tube_temperature_adjustment_dial_clockwise", "turn_lower_tube_temperature_adjustment_dial_anticlockwise"], "variable": "variable_lower_tube_temperature"}
            ],
            "adjust_upper_tube_temperature": [
                {"step": 1, "actions": ["turn_upper_tube_temperature_adjustment_dial_clockwise", "turn_upper_tube_temperature_adjustment_dial_anticlockwise"], "variable": "variable_upper_tube_temperature"}
            ],
            "adjust_function_selection": [
                {"step": 1, "actions": ["turn_function_selection_dial_clockwise", "turn_function_selection_dial_anticlockwise"], "variable": "variable_function_selection"}
            ],
            "adjust_time_or_stay_on": [
                {"step": 1, "actions": ["turn_time_adjustment_dial_clockwise", "turn_time_adjustment_dial_anticlockwise"], "variable": "variable_time_adjustment", "comment": "if 'Stay On' is selected, variable_start_running: set to 'on'"}
            ],
            "null": [
                {"step": 1, "actions": [], "missing_variables": []}
            ]
        }, current_value=("empty", 1))

        # Initialize variables
        self.variable_upper_tube_temperature = ContinuousVariable(value_ranges_steps=[(0, 70, 70), (70, 230, 40)], current_value=0)
        self.variable_function_selection = DiscreteVariable(value_range=["off", "lower_tube", "upper_tube", "upper_and_lower_tubes", "upper_and_lower_tubes_with_convection", "upper_tube_with_rotisserie"], current_value="off")
        self.variable_lower_tube_temperature = ContinuousVariable(value_ranges_steps=[(0, 70, 70), (70, 230, 40)], current_value=0)
        self.variable_time_adjustment = ContinuousVariable(value_ranges_steps=[(0, 10, 10), (10, 60, 10)], current_value=0)
        self.variable_start_running = DiscreteVariable(value_range=["on", "off"], current_value="off")

    # Action: turn_lower_tube_temperature_adjustment_dial_clockwise
    def turn_lower_tube_temperature_adjustment_dial_clockwise(self):
        # Update feature progress
        self.feature.update_progress("turn_lower_tube_temperature_adjustment_dial_clockwise")
        current_feature = self.feature.current_value[0]
        if current_feature == "adjust_lower_tube_temperature":
            # Adjust the lower tube temperature to the next value
            self.execute_action_and_set_next("turn_lower_tube_temperature_adjustment_dial_clockwise")

    # Action: turn_lower_tube_temperature_adjustment_dial_anticlockwise
    def turn_lower_tube_temperature_adjustment_dial_anticlockwise(self):
        # Update feature progress
        self.feature.update_progress("turn_lower_tube_temperature_adjustment_dial_anticlockwise")
        current_feature = self.feature.current_value[0]
        if current_feature == "adjust_lower_tube_temperature":
            # Adjust the lower tube temperature to the previous value
            self.execute_action_and_set_prev("turn_lower_tube_temperature_adjustment_dial_anticlockwise")

    # Action: turn_upper_tube_temperature_adjustment_dial_clockwise
    def turn_upper_tube_temperature_adjustment_dial_clockwise(self):
        # Update feature progress
        self.feature.update_progress("turn_upper_tube_temperature_adjustment_dial_clockwise")
        current_feature = self.feature.current_value[0]
        if current_feature == "adjust_upper_tube_temperature":
            # Adjust the upper tube temperature to the next value
            self.execute_action_and_set_next("turn_upper_tube_temperature_adjustment_dial_clockwise")

    # Action: turn_upper_tube_temperature_adjustment_dial_anticlockwise
    def turn_upper_tube_temperature_adjustment_dial_anticlockwise(self):
        # Update feature progress
        self.feature.update_progress("turn_upper_tube_temperature_adjustment_dial_anticlockwise")
        current_feature = self.feature.current_value[0]
        if current_feature == "adjust_upper_tube_temperature":
            # Adjust the upper tube temperature to the previous value
            self.execute_action_and_set_prev("turn_upper_tube_temperature_adjustment_dial_anticlockwise")

    # Action: turn_function_selection_dial_clockwise
    def turn_function_selection_dial_clockwise(self):
        # Update feature progress
        self.feature.update_progress("turn_function_selection_dial_clockwise")
        current_feature = self.feature.current_value[0]
        if current_feature == "adjust_function_selection":
            # Adjust the function selection to the next value
            self.execute_action_and_set_next("turn_function_selection_dial_clockwise")

    # Action: turn_function_selection_dial_anticlockwise
    def turn_function_selection_dial_anticlockwise(self):
        # Update feature progress
        self.feature.update_progress("turn_function_selection_dial_anticlockwise")
        current_feature = self.feature.current_value[0]
        if current_feature == "adjust_function_selection":
            # Adjust the function selection to the previous value
            self.execute_action_and_set_prev("turn_function_selection_dial_anticlockwise")

    # Action: turn_time_adjustment_dial_clockwise
    def turn_time_adjustment_dial_clockwise(self):
        # Update feature progress
        self.feature.update_progress("turn_time_adjustment_dial_clockwise")
        current_feature = self.feature.current_value[0]
        if current_feature == "adjust_time_or_stay_on":
            # Adjust the time to the next value
            self.execute_action_and_set_next("turn_time_adjustment_dial_clockwise")
            # If "Stay On" is selected, set variable_start_running to "on"
            if self.variable_time_adjustment.get_current_value() == 60:  # Assuming "Stay On" corresponds to max time
                self.variable_start_running.set_current_value("on")

    # Action: turn_time_adjustment_dial_anticlockwise
    def turn_time_adjustment_dial_anticlockwise(self):
        # Update feature progress
        self.feature.update_progress("turn_time_adjustment_dial_anticlockwise")
        current_feature = self.feature.current_value[0]
        if current_feature == "adjust_time_or_stay_on":
            # Adjust the time to the previous value
            self.execute_action_and_set_prev("turn_time_adjustment_dial_anticlockwise")
            # If "Stay On" is deselected, set variable_start_running to "off"
            if self.variable_time_adjustment.get_current_value() < 60:  # Assuming "Stay On" corresponds to max time
                self.variable_start_running.set_current_value("off")