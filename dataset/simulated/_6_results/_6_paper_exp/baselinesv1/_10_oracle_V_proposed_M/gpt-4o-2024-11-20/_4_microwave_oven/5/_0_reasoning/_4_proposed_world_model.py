class Simulator(Appliance):

    def reset(self):
        # Initialize feature and variables
        self.feature = Feature(
            feature_list={
                "adjust_function_dial": [
                    {"step": 1, "actions": ["turn_function_dial_clockwise", "turn_function_dial_anticlockwise"], "variable": "variable_function_dial"}
                ],
                "adjust_temperature_dial": [
                    {"step": 1, "actions": ["turn_temperature_dial_clockwise", "turn_temperature_dial_anticlockwise"], "variable": "variable_temperature_dial"}
                ],
                "adjust_selector_dial": [
                    {"step": 1, "actions": ["turn_selector_dial_clockwise", "turn_selector_dial_anticlockwise"], "variable": "variable_selector_dial"}
                ],
                "adjust_timer_dial": [
                    {"step": 1, "actions": ["turn_timer_dial_clockwise", "turn_timer_dial_anticlockwise"], "variable": "variable_timer_dial"}
                ],
                "null": [
                    {"step": 1, "actions": [], "missing_variables": []}
                ]
            },
            current_value=("empty", 1)
        )
        self.variable_function_dial = DiscreteVariable(
            value_range=["Off", "Convection", "Rotisserie", "Rotisserie & Convection"],
            current_value="Off"
        )
        self.variable_temperature_dial = DiscreteVariable(
            value_range=["Off", "100°C", "150°C", "200°C", "250°C"],
            current_value="Off"
        )
        self.variable_selector_dial = DiscreteVariable(
            value_range=["Off", "Top Heating", "Bottom Heating", "Top & Bottom Heating"],
            current_value="Off"
        )
        self.variable_timer_dial = DiscreteVariable(
            value_range=["Off", "10 minutes", "20 minutes", "30 minutes", "40 minutes"],
            current_value="Off"
        )

    # Action: Turn function dial clockwise
    def turn_function_dial_clockwise(self):
        # Update feature progress and adjust the function dial variable
        self.feature.update_progress("turn_function_dial_clockwise")
        current_feature = self.feature.current_value[0]
        if current_feature == "adjust_function_dial":
            self.execute_action_and_set_next("turn_function_dial_clockwise")

    # Action: Turn function dial anticlockwise
    def turn_function_dial_anticlockwise(self):
        # Update feature progress and adjust the function dial variable
        self.feature.update_progress("turn_function_dial_anticlockwise")
        current_feature = self.feature.current_value[0]
        if current_feature == "adjust_function_dial":
            self.execute_action_and_set_prev("turn_function_dial_anticlockwise")

    # Action: Turn temperature dial clockwise
    def turn_temperature_dial_clockwise(self):
        # Update feature progress and adjust the temperature dial variable
        self.feature.update_progress("turn_temperature_dial_clockwise")
        current_feature = self.feature.current_value[0]
        if current_feature == "adjust_temperature_dial":
            self.execute_action_and_set_next("turn_temperature_dial_clockwise")

    # Action: Turn temperature dial anticlockwise
    def turn_temperature_dial_anticlockwise(self):
        # Update feature progress and adjust the temperature dial variable
        self.feature.update_progress("turn_temperature_dial_anticlockwise")
        current_feature = self.feature.current_value[0]
        if current_feature == "adjust_temperature_dial":
            self.execute_action_and_set_prev("turn_temperature_dial_anticlockwise")

    # Action: Turn selector dial clockwise
    def turn_selector_dial_clockwise(self):
        # Update feature progress and adjust the selector dial variable
        self.feature.update_progress("turn_selector_dial_clockwise")
        current_feature = self.feature.current_value[0]
        if current_feature == "adjust_selector_dial":
            self.execute_action_and_set_next("turn_selector_dial_clockwise")

    # Action: Turn selector dial anticlockwise
    def turn_selector_dial_anticlockwise(self):
        # Update feature progress and adjust the selector dial variable
        self.feature.update_progress("turn_selector_dial_anticlockwise")
        current_feature = self.feature.current_value[0]
        if current_feature == "adjust_selector_dial":
            self.execute_action_and_set_prev("turn_selector_dial_anticlockwise")

    # Action: Turn timer dial clockwise
    def turn_timer_dial_clockwise(self):
        # Update feature progress and adjust the timer dial variable
        self.feature.update_progress("turn_timer_dial_clockwise")
        current_feature = self.feature.current_value[0]
        if current_feature == "adjust_timer_dial":
            self.execute_action_and_set_next("turn_timer_dial_clockwise")

    # Action: Turn timer dial anticlockwise
    def turn_timer_dial_anticlockwise(self):
        # Update feature progress and adjust the timer dial variable
        self.feature.update_progress("turn_timer_dial_anticlockwise")
        current_feature = self.feature.current_value[0]
        if current_feature == "adjust_timer_dial":
            self.execute_action_and_set_prev("turn_timer_dial_anticlockwise")