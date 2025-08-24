class Simulator(Appliance):

    def reset(self):
        # Initialize features and variables
        self.feature = Feature(
            feature_list={
                "power_on_off": [
                    {"step": 1, "actions": ["press_on_off_button"], "variable": "variable_power_on_off"}
                ],
                "automatic_sterilize_dry": [
                    {"step": 1, "actions": ["press_automatic_sterilize_dry_button"], "variable": "variable_dry_time", "comment": "Variable dry_time is dynamically set based on button press. Pressing button 1 time for 30 minutes dry time, 2 times for 45 minutes, 3 times for 60 minutes"}
                ],
                "dryer_only": [
                    {"step": 1, "actions": ["press_dry_only_button"], "variable": "variable_dryer_only_time", "comment": "Variable dryer_only_time is dynamically set based on button press. Pressing button 1 time for 30 minutes dry time, 2 times for 45 minutes, 3 times for 60 minutes"}
                ],
                "sterilize_only": [
                    {"step": 1, "actions": ["press_sterilize_only_button"], "comment": "Sterilize only function starts sterilization process and automatically switches off when complete"}
                ],
                "null": [
                    {"step": 1, "actions": [], "missing_variables": []}
                ]
            },
            current_value=("empty", 1)
        )
        self.variable_power_on_off = DiscreteVariable(value_range=["on", "off"], current_value="off")
        self.variable_dry_time = DiscreteVariable(value_range=["0", "30", "45", "60"], current_value="0")
        self.variable_dryer_only_time = DiscreteVariable(value_range=["0", "30", "45", "60"], current_value="0")

    # Action: press_on_off_button
    def press_on_off_button(self):
        # Update feature progress
        self.feature.update_progress("press_on_off_button")
        current_feature = self.feature.current_value[0]
        if current_feature == "power_on_off":
            # Toggle power state between "on" and "off"
            if self.variable_power_on_off.get_current_value() == "off":
                self.variable_power_on_off.set_current_value("on")
            else:
                self.variable_power_on_off.set_current_value("off")

    # Action: press_automatic_sterilize_dry_button
    def press_automatic_sterilize_dry_button(self):
        # Update feature progress
        self.feature.update_progress("press_automatic_sterilize_dry_button")
        current_feature = self.feature.current_value[0]
        if current_feature == "automatic_sterilize_dry":
            # Adjust dry time based on button press
            self.execute_action_and_set_next("press_automatic_sterilize_dry_button")

    # Action: press_dry_only_button
    def press_dry_only_button(self):
        # Update feature progress
        self.feature.update_progress("press_dry_only_button")
        current_feature = self.feature.current_value[0]
        if current_feature == "dryer_only":
            # Adjust dryer-only time based on button press
            self.execute_action_and_set_next("press_dry_only_button")

    # Action: press_sterilize_only_button
    def press_sterilize_only_button(self):
        # Update feature progress
        self.feature.update_progress("press_sterilize_only_button")
        current_feature = self.feature.current_value[0]
        if current_feature == "sterilize_only":
            # No variable adjustment, sterilization starts and automatically switches off
            pass

    # Wrapper function to handle global conditions and execute actions
    def run_action(self, action_name, execution_times=1, **kwargs):
        # Execute the action
        action = getattr(self, action_name, None)
        if callable(action):
            for _ in range(execution_times):
                action(**kwargs)

        # Update display after action execution
        self.update_display()
        return self.display