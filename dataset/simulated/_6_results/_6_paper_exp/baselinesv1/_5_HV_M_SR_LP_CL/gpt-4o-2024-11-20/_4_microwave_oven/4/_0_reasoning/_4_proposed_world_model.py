class Simulator(Appliance):

    def reset(self):
        # Initialize feature and variables
        self.feature = Feature(
            feature_list={
                'set_function_knob': [{'step': 1, 'actions': ['turn_function_dial_clockwise', 'turn_function_dial_anticlockwise'], 'variable': 'variable_function_knob'}],
                'adjust_upper_heater_temperature': [{'step': 1, 'actions': ['turn_upper_temp_dial_clockwise', 'turn_upper_temp_dial_anticlockwise'], 'variable': 'variable_upper_heater_temperature'}],
                'adjust_lower_heater_temperature': [{'step': 1, 'actions': ['turn_lower_temp_dial_clockwise', 'turn_lower_temp_dial_anticlockwise'], 'variable': 'variable_lower_heater_temperature'}],
                'set_timer': [{'step': 1, 'actions': ['turn_time_dial_clockwise', 'turn_time_dial_anticlockwise'], 'variable': 'variable_timer'}],
                'null': [{'step': 1, 'actions': [], 'missing_variables': []}]
            },
            current_value=("empty", 1)
        )
        self.variable_upper_heater_temperature = variable_upper_heater_temperature
        self.variable_lower_heater_temperature = variable_lower_heater_temperature
        self.variable_timer = variable_timer
        self.variable_function_knob = variable_function_knob

    # Action: turn_function_dial_clockwise
    def turn_function_dial_clockwise(self):
        # Update feature progress and adjust the function knob variable
        self.feature.update_progress("turn_function_dial_clockwise")
        current_feature = self.feature.current_value[0]
        if current_feature == "set_function_knob":
            self.execute_action_and_set_next("turn_function_dial_clockwise")

    # Action: turn_function_dial_anticlockwise
    def turn_function_dial_anticlockwise(self):
        # Update feature progress and adjust the function knob variable
        self.feature.update_progress("turn_function_dial_anticlockwise")
        current_feature = self.feature.current_value[0]
        if current_feature == "set_function_knob":
            self.execute_action_and_set_prev("turn_function_dial_anticlockwise")

    # Action: turn_upper_temp_dial_clockwise
    def turn_upper_temp_dial_clockwise(self):
        # Update feature progress and adjust the upper heater temperature variable
        self.feature.update_progress("turn_upper_temp_dial_clockwise")
        current_feature = self.feature.current_value[0]
        if current_feature == "adjust_upper_heater_temperature":
            self.execute_action_and_set_next("turn_upper_temp_dial_clockwise")

    # Action: turn_upper_temp_dial_anticlockwise
    def turn_upper_temp_dial_anticlockwise(self):
        # Update feature progress and adjust the upper heater temperature variable
        self.feature.update_progress("turn_upper_temp_dial_anticlockwise")
        current_feature = self.feature.current_value[0]
        if current_feature == "adjust_upper_heater_temperature":
            self.execute_action_and_set_prev("turn_upper_temp_dial_anticlockwise")

    # Action: turn_lower_temp_dial_clockwise
    def turn_lower_temp_dial_clockwise(self):
        # Update feature progress and adjust the lower heater temperature variable
        self.feature.update_progress("turn_lower_temp_dial_clockwise")
        current_feature = self.feature.current_value[0]
        if current_feature == "adjust_lower_heater_temperature":
            self.execute_action_and_set_next("turn_lower_temp_dial_clockwise")

    # Action: turn_lower_temp_dial_anticlockwise
    def turn_lower_temp_dial_anticlockwise(self):
        # Update feature progress and adjust the lower heater temperature variable
        self.feature.update_progress("turn_lower_temp_dial_anticlockwise")
        current_feature = self.feature.current_value[0]
        if current_feature == "adjust_lower_heater_temperature":
            self.execute_action_and_set_prev("turn_lower_temp_dial_anticlockwise")

    # Action: turn_time_dial_clockwise
    def turn_time_dial_clockwise(self):
        # Update feature progress and adjust the timer variable
        self.feature.update_progress("turn_time_dial_clockwise")
        current_feature = self.feature.current_value[0]
        if current_feature == "set_timer":
            self.execute_action_and_set_next("turn_time_dial_clockwise")

    # Action: turn_time_dial_anticlockwise
    def turn_time_dial_anticlockwise(self):
        # Update feature progress and adjust the timer variable
        self.feature.update_progress("turn_time_dial_anticlockwise")
        current_feature = self.feature.current_value[0]
        if current_feature == "set_timer":
            self.execute_action_and_set_prev("turn_time_dial_anticlockwise")