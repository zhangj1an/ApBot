class Simulator(Appliance):

    def reset(self):
        # Initialize features and variables
        self.feature = Feature(
            feature_list={
                'power_control': [{'step': 1, 'actions': ['press_power_button'], 'variable': 'variable_power_on_off'}],
                'adjust_timer': [{'step': 1, 'actions': ['press_timer_button'], 'variable': 'variable_timer'}],
                'uv_light_control': [{'step': 1, 'actions': ['press_uv_button'], 'variable': 'variable_uv_light'}],
                'reset_uv_indicator': [{'step': 1, 'actions': ['press_and_hold_uv_button']}],
                'ionizer_control': [{'step': 1, 'actions': ['press_ionizer_button'], 'variable': 'variable_ionizer'}],
                'reset_filter_indicator': [{'step': 1, 'actions': ['press_and_hold_ionizer_button']}],
                'adjust_fan_speed_mode': [{'step': 1, 'actions': ['press_speed_mode_button'], 'variable': 'variable_fan_speed_mode'}],
                'null': [{'step': 1, 'actions': [], 'missing_variables': []}]
            },
            current_value=("empty", 1)
        )
        self.variable_power_on_off = DiscreteVariable(value_range=["on", "off"], current_value="off")
        self.variable_timer = DiscreteVariable(value_range=["0", "1H", "2H", "4H", "8H"], current_value="0")
        self.variable_uv_light = DiscreteVariable(value_range=["on", "off"], current_value="off")
        self.variable_ionizer = DiscreteVariable(value_range=["on", "off"], current_value="off")
        self.variable_fan_speed_mode = DiscreteVariable(value_range=["1", "2", "3", "Turbo", "Auto", "Sleep"], current_value="1")

    # Action: press_power_button
    # Effect: Toggles the power state between "on" and "off".
    def press_power_button(self):
        self.feature.update_progress("press_power_button")
        current_feature = self.feature.current_value[0]
        if current_feature == "power_control":
            self.execute_action_and_set_next("press_power_button")

    # Action: press_timer_button
    # Effect: Cycles through timer options: "0", "1H", "2H", "4H", "8H".
    def press_timer_button(self):
        self.feature.update_progress("press_timer_button")
        current_feature = self.feature.current_value[0]
        if current_feature == "adjust_timer":
            self.execute_action_and_set_next("press_timer_button")

    # Action: press_uv_button
    # Effect: Toggles the UV light state between "on" and "off".
    def press_uv_button(self):
        self.feature.update_progress("press_uv_button")
        current_feature = self.feature.current_value[0]
        if current_feature == "uv_light_control":
            self.execute_action_and_set_next("press_uv_button")

    # Action: press_and_hold_uv_button
    # Effect: Resets the UV indicator if held for 3 seconds or more.
    def press_and_hold_uv_button(self, duration=3):
        self.feature.update_progress("press_and_hold_uv_button")
        current_feature = self.feature.current_value[0]
        if current_feature == "reset_uv_indicator" and duration >= 3:
            self.execute_action_and_set_next("press_and_hold_uv_button")

    # Action: press_ionizer_button
    # Effect: Toggles the ionizer state between "on" and "off".
    def press_ionizer_button(self):
        self.feature.update_progress("press_ionizer_button")
        current_feature = self.feature.current_value[0]
        if current_feature == "ionizer_control":
            self.execute_action_and_set_next("press_ionizer_button")

    # Action: press_and_hold_ionizer_button
    # Effect: Resets the filter indicator if held for 3 seconds or more.
    def press_and_hold_ionizer_button(self, duration=3):
        self.feature.update_progress("press_and_hold_ionizer_button")
        current_feature = self.feature.current_value[0]
        if current_feature == "reset_filter_indicator" and duration >= 3:
            self.execute_action_and_set_next("press_and_hold_ionizer_button")

    # Action: press_speed_mode_button
    # Effect: Cycles through fan speed/mode options: "1", "2", "3", "Turbo", "Auto", "Sleep".
    def press_speed_mode_button(self):
        self.feature.update_progress("press_speed_mode_button")
        current_feature = self.feature.current_value[0]
        if current_feature == "adjust_fan_speed_mode":
            self.execute_action_and_set_next("press_speed_mode_button")