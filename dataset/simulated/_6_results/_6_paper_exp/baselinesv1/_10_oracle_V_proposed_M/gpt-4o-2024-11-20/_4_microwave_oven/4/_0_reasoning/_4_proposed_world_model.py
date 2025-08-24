class Simulator(Appliance):

    def reset(self):
        # Initialize feature and variables
        self.feature = Feature(
            feature_list={
                'adjust_upper_heater_temperature': [{'step': 1, 'actions': ['turn_upper_temp_dial_clockwise', 'turn_upper_temp_dial_anticlockwise'], 'variable': 'variable_upper_heater_temperature'}],
                'adjust_lower_heater_temperature': [{'step': 1, 'actions': ['turn_lower_temp_dial_clockwise', 'turn_lower_temp_dial_anticlockwise'], 'variable': 'variable_lower_heater_temperature'}],
                'adjust_timer': [{'step': 1, 'actions': ['turn_time_dial_clockwise', 'turn_time_dial_anticlockwise'], 'variable': 'variable_timer'}],
                'select_function': [{'step': 1, 'actions': ['turn_function_dial_clockwise', 'turn_function_dial_anticlockwise'], 'variable': 'variable_function_knob'}],
                'null': [{'step': 1, 'actions': [], 'missing_variables': []}]
            },
            current_value=("empty", 1)
        )
        self.variable_upper_heater_temperature = ContinuousVariable(value_ranges_steps=[(0, 70, 70), (70, 230, 40)], current_value=0)
        self.variable_lower_heater_temperature = ContinuousVariable(value_ranges_steps=[(0, 70, 70), (70, 230, 40)], current_value=0)
        self.variable_timer = DiscreteVariable(
            value_range=["0", "20", "40", "60", "100", "120", "Stay On"],
            current_value="0"
        )
        self.variable_function_knob = DiscreteVariable(
            value_range=["Off", "Fermentation", "Convection", "Lower & Upper Heater", "Upper Heater"],
            current_value="Off"
        )

    # Action: Turn the upper heater temperature dial clockwise
    def turn_upper_temp_dial_clockwise(self):
        # Update feature progress
        self.feature.update_progress("turn_upper_temp_dial_clockwise")
        current_feature = self.feature.current_value[0]
        if current_feature == "adjust_upper_heater_temperature":
            # Adjust the upper heater temperature to the next value
            self.execute_action_and_set_next("turn_upper_temp_dial_clockwise")

    # Action: Turn the upper heater temperature dial anticlockwise
    def turn_upper_temp_dial_anticlockwise(self):
        # Update feature progress
        self.feature.update_progress("turn_upper_temp_dial_anticlockwise")
        current_feature = self.feature.current_value[0]
        if current_feature == "adjust_upper_heater_temperature":
            # Adjust the upper heater temperature to the previous value
            self.execute_action_and_set_prev("turn_upper_temp_dial_anticlockwise")

    # Action: Turn the lower heater temperature dial clockwise
    def turn_lower_temp_dial_clockwise(self):
        # Update feature progress
        self.feature.update_progress("turn_lower_temp_dial_clockwise")
        current_feature = self.feature.current_value[0]
        if current_feature == "adjust_lower_heater_temperature":
            # Adjust the lower heater temperature to the next value
            self.execute_action_and_set_next("turn_lower_temp_dial_clockwise")

    # Action: Turn the lower heater temperature dial anticlockwise
    def turn_lower_temp_dial_anticlockwise(self):
        # Update feature progress
        self.feature.update_progress("turn_lower_temp_dial_anticlockwise")
        current_feature = self.feature.current_value[0]
        if current_feature == "adjust_lower_heater_temperature":
            # Adjust the lower heater temperature to the previous value
            self.execute_action_and_set_prev("turn_lower_temp_dial_anticlockwise")

    # Action: Turn the timer dial clockwise
    def turn_time_dial_clockwise(self):
        # Update feature progress
        self.feature.update_progress("turn_time_dial_clockwise")
        current_feature = self.feature.current_value[0]
        if current_feature == "adjust_timer":
            # Adjust the timer to the next value
            self.execute_action_and_set_next("turn_time_dial_clockwise")

    # Action: Turn the timer dial anticlockwise
    def turn_time_dial_anticlockwise(self):
        # Update feature progress
        self.feature.update_progress("turn_time_dial_anticlockwise")
        current_feature = self.feature.current_value[0]
        if current_feature == "adjust_timer":
            # Adjust the timer to the previous value
            self.execute_action_and_set_prev("turn_time_dial_anticlockwise")

    # Action: Turn the function knob clockwise
    def turn_function_dial_clockwise(self):
        # Update feature progress
        self.feature.update_progress("turn_function_dial_clockwise")
        current_feature = self.feature.current_value[0]
        if current_feature == "select_function":
            # Adjust the function knob to the next value
            self.execute_action_and_set_next("turn_function_dial_clockwise")

    # Action: Turn the function knob anticlockwise
    def turn_function_dial_anticlockwise(self):
        # Update feature progress
        self.feature.update_progress("turn_function_dial_anticlockwise")
        current_feature = self.feature.current_value[0]
        if current_feature == "select_function":
            # Adjust the function knob to the previous value
            self.execute_action_and_set_prev("turn_function_dial_anticlockwise")