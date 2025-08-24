class Simulator(Appliance):

    def reset(self):
        # Initialize feature and variables
        self.feature = simulator_feature
        self.variable_function_dial = variable_function_dial
        self.variable_temperature_dial = variable_temperature_dial
        self.variable_selector_dial = variable_selector_dial
        self.variable_timer_dial = variable_timer_dial

    # Action: Turn the function dial clockwise
    def turn_function_dial_clockwise(self):
        # Update feature progress
        self.feature.update_progress("turn_function_dial_clockwise")
        current_feature = self.feature.current_value[0]

        if current_feature in ["general_cooking", "rotisserie_use"]:
            # Adjust the function dial to the next value
            self.execute_action_and_set_next("turn_function_dial_clockwise")

    # Action: Turn the function dial anticlockwise
    def turn_function_dial_anticlockwise(self):
        # Update feature progress
        self.feature.update_progress("turn_function_dial_anticlockwise")
        current_feature = self.feature.current_value[0]

        if current_feature in ["null"]:
            # Adjust the function dial to the previous value
            self.execute_action_and_set_prev("turn_function_dial_anticlockwise")

    # Action: Turn the selector dial clockwise
    def turn_selector_dial_clockwise(self):
        # Update feature progress
        self.feature.update_progress("turn_selector_dial_clockwise")
        current_feature = self.feature.current_value[0]

        if current_feature in ["general_cooking", "rotisserie_use", "grill_cooking"]:
            # Adjust the selector dial to the next value
            self.execute_action_and_set_next("turn_selector_dial_clockwise")

    # Action: Turn the selector dial anticlockwise
    def turn_selector_dial_anticlockwise(self):
        # Update feature progress
        self.feature.update_progress("turn_selector_dial_anticlockwise")
        current_feature = self.feature.current_value[0]

        if current_feature in ["null"]:
            # Adjust the selector dial to the previous value
            self.execute_action_and_set_prev("turn_selector_dial_anticlockwise")

    # Action: Turn the timer dial clockwise
    def turn_timer_dial_clockwise(self):
        # Update feature progress
        self.feature.update_progress("turn_timer_dial_clockwise")
        current_feature = self.feature.current_value[0]

        if current_feature in ["general_cooking", "rotisserie_use", "grill_cooking"]:
            # Adjust the timer dial to the next value
            self.execute_action_and_set_next("turn_timer_dial_clockwise")

    # Action: Turn the timer dial anticlockwise
    def turn_timer_dial_anticlockwise(self):
        # Update feature progress
        self.feature.update_progress("turn_timer_dial_anticlockwise")
        current_feature = self.feature.current_value[0]

        if current_feature in ["null"]:
            # Adjust the timer dial to the previous value
            self.execute_action_and_set_prev("turn_timer_dial_anticlockwise")

    # Action: Turn the temperature dial clockwise
    def turn_temperature_dial_clockwise(self):
        # Update feature progress
        self.feature.update_progress("turn_temperature_dial_clockwise")
        current_feature = self.feature.current_value[0]

        if current_feature in ["general_cooking", "rotisserie_use", "grill_cooking"]:
            # Adjust the temperature dial to the next value
            self.execute_action_and_set_next("turn_temperature_dial_clockwise")

    # Action: Turn the temperature dial anticlockwise
    def turn_temperature_dial_anticlockwise(self):
        # Update feature progress
        self.feature.update_progress("turn_temperature_dial_anticlockwise")
        current_feature = self.feature.current_value[0]

        if current_feature in ["null"]:
            # Adjust the temperature dial to the previous value
            self.execute_action_and_set_prev("turn_temperature_dial_anticlockwise")

    # Wrapper function to handle global conditions and execute actions
    def run_action(self, action_name, execution_times=1, **kwargs):
        # Execute the action
        action = getattr(self, action_name, None)
        if callable(action):
            for _ in range(execution_times):
                action(**kwargs)

        # Update the display after action execution
        self.update_display()
        return self.display