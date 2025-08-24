class Simulator(Appliance):

    def reset(self):
        # Initialize the feature and variables
        self.feature = Feature(
            feature_list={
                'power_on_off': [{'step': 1, 'actions': ['press_power_on_off_button'], 'variable': 'variable_power_on_off'}],
                'sterilise_only': [{'step': 1, 'actions': ['press_sterilise_only_button'], 'variable': 'variable_sterilise_only_time'}],
                'drying_only': [{'step': 1, 'actions': ['press_drying_only_button'], 'variable': 'variable_drying_only_time'}],
                'auto_mode': [{'step': 1, 'actions': ['press_auto_mode_button'], 'variable': 'variable_auto_mode'}],
                'storage_mode': [{'step': 1, 'actions': ['press_storage_button'], 'variable': 'variable_storage_mode'}],
                'null': [{'step': 1, 'actions': [], 'missing_variables': []}]
            },
            current_value=("empty", 1)
        )
        self.variable_power_on_off = variable_power_on_off
        self.variable_auto_mode = variable_auto_mode
        self.variable_sterilise_only_time = variable_sterilise_only_time
        self.variable_drying_only_time = variable_drying_only_time
        self.variable_storage_mode = variable_storage_mode

    # Action: press_power_on_off_button
    def press_power_on_off_button(self):
        # Update feature progress
        self.feature.update_progress("press_power_on_off_button")
        current_feature = self.feature.current_value[0]
        if current_feature == "power_on_off":
            # Toggle the power state between "on" and "off"
            if self.variable_power_on_off.get_current_value() == "off":
                self.variable_power_on_off.set_current_value("on")
            else:
                self.variable_power_on_off.set_current_value("off")

    # Action: press_sterilise_only_button
    def press_sterilise_only_button(self):
        # Update feature progress
        self.feature.update_progress("press_sterilise_only_button")
        current_feature = self.feature.current_value[0]
        if current_feature == "sterilise_only":
            # Toggle between 10 minutes and 35 minutes sterilisation
            self.execute_action_and_set_next("press_sterilise_only_button")

    # Action: press_drying_only_button
    def press_drying_only_button(self):
        # Update feature progress
        self.feature.update_progress("press_drying_only_button")
        current_feature = self.feature.current_value[0]
        if current_feature == "drying_only":
            # Cycle through 30, 40, and 50 minutes drying options
            self.execute_action_and_set_next("press_drying_only_button")

    # Action: press_auto_mode_button
    def press_auto_mode_button(self):
        # Update feature progress
        self.feature.update_progress("press_auto_mode_button")
        current_feature = self.feature.current_value[0]
        if current_feature == "auto_mode":
            # Toggle between 35 minutes and 60 minutes auto mode
            self.execute_action_and_set_next("press_auto_mode_button")

    # Action: press_storage_button
    def press_storage_button(self):
        # Update feature progress
        self.feature.update_progress("press_storage_button")
        current_feature = self.feature.current_value[0]
        if current_feature == "storage_mode":
            # Toggle storage mode between "on" and "off"
            if self.variable_storage_mode.get_current_value() == "off":
                self.variable_storage_mode.set_current_value("on")
            else:
                self.variable_storage_mode.set_current_value("off")

    # Override run_action to include global conditions
    def run_action(self, action_name, execution_times=1, **kwargs):
        # Execute the action
        action = getattr(self, action_name, None)
        if callable(action):
            for _ in range(execution_times):
                action(**kwargs)

        # Update the display after action execution
        self.update_display()
        return self.display