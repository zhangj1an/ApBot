class Simulator(Appliance):

    def reset(self):
        # Initialize features and variables
        self.feature = Feature(
            feature_list={
                'power_control': [{'step': 1, 'actions': ['press_power_button'], 'variable': 'variable_power_on_off'}],
                'adjust_fan_speed': [{'step': 1, 'actions': ['press_speed_button'], 'variable': 'variable_fan_speed'}],
                'control_ion_generator': [{'step': 1, 'actions': ['press_ion_button'], 'variable': 'variable_ion_generator'}],
                'adjust_timer': [{'step': 1, 'actions': ['press_timer_button'], 'variable': 'variable_timer'}],
                'enable_sleep_mode': [{'step': 1, 'actions': ['press_sleep_button'], 'variable': 'variable_sleep_mode'}],
                'reset_filter_timer': [{'step': 1, 'actions': ['press_and_hold_sleep_button'], 'variable': 'variable_filter_timer_reset'}],
                'null': [{'step': 1, 'actions': [], 'missing_variables': []}]
            },
            current_value=("empty", 1)
        )
        self.variable_power_on_off = variable_power_on_off
        self.variable_fan_speed = variable_fan_speed
        self.variable_ion_generator = variable_ion_generator
        self.variable_timer = variable_timer
        self.variable_sleep_mode = variable_sleep_mode
        self.variable_filter_timer_reset = variable_filter_timer_reset

    # Action: press_power_button
    # Effect: Toggles the power on/off state of the appliance.
    def press_power_button(self):
        self.feature.update_progress("press_power_button")
        current_feature = self.feature.current_value[0]
        if current_feature == "power_control":
            self.execute_action_and_set_next("press_power_button")

    # Action: press_speed_button
    # Effect: Cycles through fan speed settings (1: Low, 2: Mid, 3: High).
    def press_speed_button(self):
        self.feature.update_progress("press_speed_button")
        current_feature = self.feature.current_value[0]
        if current_feature == "adjust_fan_speed":
            self.execute_action_and_set_next("press_speed_button")

    # Action: press_ion_button
    # Effect: Toggles the negative ion generator on/off.
    def press_ion_button(self):
        self.feature.update_progress("press_ion_button")
        current_feature = self.feature.current_value[0]
        if current_feature == "control_ion_generator":
            self.execute_action_and_set_next("press_ion_button")

    # Action: press_timer_button
    # Effect: Sets an auto-on or auto-off timer (1H, 2H, 4H).
    def press_timer_button(self):
        self.feature.update_progress("press_timer_button")
        current_feature = self.feature.current_value[0]
        if current_feature == "adjust_timer":
            self.execute_action_and_set_next("press_timer_button")

    # Action: press_sleep_button
    # Effect: Enables sleep mode, turning off lights and setting fan to low mode.
    def press_sleep_button(self):
        self.feature.update_progress("press_sleep_button")
        current_feature = self.feature.current_value[0]
        if current_feature == "enable_sleep_mode":
            self.execute_action_and_set_next("press_sleep_button")

    # Action: press_and_hold_sleep_button
    # Effect: Resets the filter timer after holding the button for 5 seconds.
    def press_and_hold_sleep_button(self, duration=5):
        self.feature.update_progress("press_and_hold_sleep_button")
        current_feature = self.feature.current_value[0]
        if current_feature == "reset_filter_timer" and duration >= 5:
            self.execute_action_and_set_next("press_and_hold_sleep_button")