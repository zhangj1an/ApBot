class Simulator(Appliance):

    def reset(self):
        # Initialize features and variables
        self.feature = Feature(
            feature_list={
                "activate_sterilizer": [
                    {"step": 1, "actions": ["press_on_off_button"], "variable": "variable_power_on_off"}
                ],
                "automatic_sterilize_dry_time": [
                    {"step": 1, "actions": ["press_automatic_sterilize_dry_button"], "variable": "variable_dry_time"}
                ],
                "dryer_only_time": [
                    {"step": 1, "actions": ["press_dry_only_button"], "variable": "variable_dryer_only_time"}
                ],
                "sterilize_only": [
                    {"step": 1, "actions": ["press_sterilize_only_button"]}
                ],
                "null": [
                    {"step": 1, "actions": [], "missing_variables": []}
                ]
            },
            current_value=("empty", 1)
        )
        self.variable_power_on_off = variable_power_on_off
        self.variable_dry_time = variable_dry_time
        self.variable_dryer_only_time = variable_dryer_only_time

    # Action: press_on_off_button
    def press_on_off_button(self):
        # Update feature progress
        self.feature.update_progress("press_on_off_button")
        current_feature = self.feature.current_value[0]
        if current_feature == "activate_sterilizer":
            # Set power to "on" when this button is pressed
            self.variable_power_on_off.set_current_value("on")

    # Action: press_automatic_sterilize_dry_button
    def press_automatic_sterilize_dry_button(self):
        # Update feature progress
        self.feature.update_progress("press_automatic_sterilize_dry_button")
        current_feature = self.feature.current_value[0]
        if current_feature == "automatic_sterilize_dry_time":
            # Adjust the drying time for automatic sterilize/dry function
            self.execute_action_and_set_next("press_automatic_sterilize_dry_button")

    # Action: press_dry_only_button
    def press_dry_only_button(self):
        # Update feature progress
        self.feature.update_progress("press_dry_only_button")
        current_feature = self.feature.current_value[0]
        if current_feature == "dryer_only_time":
            # Adjust the drying time for dryer-only function
            self.execute_action_and_set_next("press_dry_only_button")

    # Action: press_sterilize_only_button
    def press_sterilize_only_button(self):
        # Update feature progress
        self.feature.update_progress("press_sterilize_only_button")
        current_feature = self.feature.current_value[0]
        if current_feature == "sterilize_only":
            # No additional variable adjustment is required for sterilize-only function
            pass

    # Override run_action to include global condition checks
    def run_action(self, action_name, execution_times=1, **kwargs):
        # Execute the action
        return super().run_action(action_name, execution_times, **kwargs)