class Simulator(Appliance):

    def reset(self):
        # Initialize features and variables
        self.feature = Feature(
            feature_list={
                "power_on_off": [
                    {"step": 1, "actions": ["press_power_button"], "variable": "variable_power_on_off"}
                ],
                "microbe_shield_night_mode": [
                    {"step": 1, "actions": ["press_microbe_shield_night_mode_button"], "variable": "variable_microbe_shield_night_mode"}
                ],
                "adjust_fan_speed": [
                    {"step": 1, "actions": ["press_fan_speed_button"], "variable": "variable_fan_speed"}
                ],
                "set_timer": [
                    {"step": 1, "actions": ["press_timer_button"], "variable": "variable_timer"}
                ],
                "null": [
                    {"step": 1, "actions": ["press_and_hold_power_button"], "missing_variables": []}
                ]
            },
            current_value=("empty", 1)
        )
        self.variable_power_on_off = variable_power_on_off
        self.variable_microbe_shield_night_mode = variable_microbe_shield_night_mode
        self.variable_fan_speed = variable_fan_speed
        self.variable_timer = variable_timer

    # Action: press_power_button
    def press_power_button(self):
        # Update feature progress
        self.feature.update_progress("press_power_button")
        current_feature = self.feature.current_value[0]
        if current_feature == "power_on_off":
            # Toggle power on/off
            self.execute_action_and_set_next("press_power_button")

    # Action: press_and_hold_power_button
    def press_and_hold_power_button(self, duration=5):
        # Update feature progress
        self.feature.update_progress("press_and_hold_power_button")
        current_feature = self.feature.current_value[0]
        if current_feature == "null" and duration >= 5:
            # No specific variable adjustment, just update feature progress
            self.execute_action_and_set_next("press_and_hold_power_button")

    # Action: press_microbe_shield_night_mode_button
    def press_microbe_shield_night_mode_button(self):
        # Update feature progress
        self.feature.update_progress("press_microbe_shield_night_mode_button")
        current_feature = self.feature.current_value[0]
        if current_feature == "microbe_shield_night_mode":
            # Cycle through microbe shield, night mode, and off
            self.execute_action_and_set_next("press_microbe_shield_night_mode_button")

    # Action: press_fan_speed_button
    def press_fan_speed_button(self):
        # Update feature progress
        self.feature.update_progress("press_fan_speed_button")
        current_feature = self.feature.current_value[0]
        if current_feature == "adjust_fan_speed":
            # Cycle through fan speeds: low, medium, high, turbo
            self.execute_action_and_set_next("press_fan_speed_button")

    # Action: press_timer_button
    def press_timer_button(self):
        # Update feature progress
        self.feature.update_progress("press_timer_button")
        current_feature = self.feature.current_value[0]
        if current_feature == "set_timer":
            # Cycle through timer options: 2H, 4H, 8H, off
            self.execute_action_and_set_next("press_timer_button")