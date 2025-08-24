class Simulator(Appliance):

    def reset(self):
        # Initialize features and variables
        self.feature = Feature(
            feature_list={
                "power_and_start_warming": [
                    {"step": 1, "actions": ["press_power_button"], "variable": "variable_power_on_off", "comment": "variable_start_running: set to on"}
                ],
                "adjust_night_light": [
                    {"step": 1, "actions": ["press_and_hold_power_button"], "variable": "variable_night_light"}
                ],
                "select_bottle_type": [
                    {"step": 1, "actions": ["press_bottle_button"], "variable": "variable_bottle_type"}
                ],
                "select_initial_temperature": [
                    {"step": 1, "actions": ["press_initial_temp_button"], "variable": "variable_initial_temp"}
                ],
                "select_volume": [
                    {"step": 1, "actions": ["press_volume_button"], "variable": "variable_volume"}
                ],
                "null": [
                    {"step": 1, "actions": [], "missing_variables": []}
                ]
            },
            current_value=("empty", 1)
        )
        self.variable_power_on_off = variable_power_on_off
        self.variable_night_light = variable_night_light
        self.variable_bottle_type = variable_bottle_type
        self.variable_initial_temp = variable_initial_temp
        self.variable_volume = variable_volume
        self.variable_start_running = variable_start_running

    # Action: press_power_button
    def press_power_button(self):
        # Update feature progress
        self.feature.update_progress("press_power_button")
        current_feature = self.feature.current_value[0]

        if current_feature == "power_and_start_warming":
            # Toggle power on/off and set start_running accordingly
            if self.variable_power_on_off.get_current_value() == "off":
                self.variable_power_on_off.set_current_value("on")
                self.variable_start_running.set_current_value("on")
            else:
                self.variable_power_on_off.set_current_value("off")
                self.variable_start_running.set_current_value("off")

    # Action: press_and_hold_power_button
    def press_and_hold_power_button(self, duration=3):
        # Update feature progress
        self.feature.update_progress("press_and_hold_power_button")
        current_feature = self.feature.current_value[0]

        if current_feature == "adjust_night_light" and duration >= 3:
            # Toggle night light on/off
            if self.variable_night_light.get_current_value() == "off":
                self.variable_night_light.set_current_value("on")
            else:
                self.variable_night_light.set_current_value("off")

    # Action: press_bottle_button
    def press_bottle_button(self):
        # Update feature progress
        self.feature.update_progress("press_bottle_button")
        current_feature = self.feature.current_value[0]

        if current_feature == "select_bottle_type":
            # Cycle through bottle types
            self.execute_action_and_set_next("press_bottle_button")

    # Action: press_initial_temp_button
    def press_initial_temp_button(self):
        # Update feature progress
        self.feature.update_progress("press_initial_temp_button")
        current_feature = self.feature.current_value[0]

        if current_feature == "select_initial_temperature":
            # Cycle through initial temperature options
            self.execute_action_and_set_next("press_initial_temp_button")

    # Action: press_volume_button
    def press_volume_button(self):
        # Update feature progress
        self.feature.update_progress("press_volume_button")
        current_feature = self.feature.current_value[0]

        if current_feature == "select_volume":
            # Cycle through volume options
            self.execute_action_and_set_next("press_volume_button")

    # Override run_action to handle global conditions
    def run_action(self, action_name, execution_times=1, **kwargs):
        # Execute the action
        return super().run_action(action_name, execution_times, **kwargs)