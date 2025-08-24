class Simulator(Appliance):

    def reset(self):
        # Initialize the feature and variables
        self.feature = Feature(
            feature_list={
                'sterilise_only_function': [{'step': 1, 'actions': ['press_sterilise_only_button'], 'variable': 'variable_sterilise_only_duration'}],
                'drying_only_function': [{'step': 1, 'actions': ['press_drying_only_button'], 'variable': 'variable_drying_only_duration'}],
                'auto_mode': [{'step': 1, 'actions': ['press_auto_mode_button'], 'variable': 'variable_auto_mode_duration'}],
                'storage_function': [{'step': 1, 'actions': ['press_storage_button'], 'variable': 'variable_storage_mode'}],
                'power_on_off': [{'step': 1, 'actions': ['press_power_on_off_button'], 'variable': 'variable_power_on_off'}],
                'button_sound': [{'step': 1, 'actions': ['press_and_hold_sterilise_only_button_and_power_on_off_button'], 'variable': 'variable_button_sound'}],
                'null': [{'step': 1, 'actions': [], 'missing_variables': []}]
            },
            current_value=("empty", 1)
        )
        self.variable_power_on_off = DiscreteVariable(value_range=["on", "off"], current_value="off")
        self.variable_sterilise_only_duration = DiscreteVariable(value_range=["10 minutes", "35 minutes"], current_value="10 minutes")
        self.variable_drying_only_duration = DiscreteVariable(value_range=["30 minutes", "40 minutes", "50 minutes"], current_value="30 minutes")
        self.variable_auto_mode_duration = DiscreteVariable(value_range=["35 minutes", "60 minutes"], current_value="35 minutes")
        self.variable_storage_mode = DiscreteVariable(value_range=["off", "on"], current_value="off")
        self.variable_button_sound = DiscreteVariable(value_range=["on", "off"], current_value="on")

    # Action: press_power_on_off_button
    def press_power_on_off_button(self):
        # This action toggles the power state between "on" and "off"
        self.feature.update_progress("press_power_on_off_button")
        current_feature = self.feature.current_value[0]
        if current_feature == "power_on_off":
            self.execute_action_and_set_next("press_power_on_off_button")

    # Action: press_sterilise_only_button
    def press_sterilise_only_button(self):
        # This action toggles the sterilise-only duration between "10 minutes" and "35 minutes"
        self.feature.update_progress("press_sterilise_only_button")
        current_feature = self.feature.current_value[0]
        if current_feature == "sterilise_only_function":
            self.execute_action_and_set_next("press_sterilise_only_button")

    # Action: press_drying_only_button
    def press_drying_only_button(self):
        # This action toggles the drying-only duration between "30 minutes", "40 minutes", and "50 minutes"
        self.feature.update_progress("press_drying_only_button")
        current_feature = self.feature.current_value[0]
        if current_feature == "drying_only_function":
            self.execute_action_and_set_next("press_drying_only_button")

    # Action: press_auto_mode_button
    def press_auto_mode_button(self):
        # This action toggles the auto mode duration between "35 minutes" and "60 minutes"
        self.feature.update_progress("press_auto_mode_button")
        current_feature = self.feature.current_value[0]
        if current_feature == "auto_mode":
            self.execute_action_and_set_next("press_auto_mode_button")

    # Action: press_storage_button
    def press_storage_button(self):
        # This action toggles the storage mode between "on" and "off"
        self.feature.update_progress("press_storage_button")
        current_feature = self.feature.current_value[0]
        if current_feature == "storage_function":
            self.execute_action_and_set_next("press_storage_button")

    # Action: press_and_hold_sterilise_only_button_and_power_on_off_button
    def press_and_hold_sterilise_only_button_and_power_on_off_button(self, duration=3):
        # This action toggles the button sound between "on" and "off" when held for 3 seconds
        self.feature.update_progress("press_and_hold_sterilise_only_button_and_power_on_off_button")
        current_feature = self.feature.current_value[0]
        if current_feature == "button_sound" and duration >= 3:
            self.execute_action_and_set_next("press_and_hold_sterilise_only_button_and_power_on_off_button")