class Simulator(Appliance):

    def reset(self):
        # Initialize features and variables
        self.feature = Feature(
            feature_list={
                'power_toggle_or_start_warming': [
                    {'step': 1, 'actions': ['press_power_button'], 'variable': 'variable_power_on_off', 'comment': "This action toggles 'variable_power_on_off' between 'on' and 'off'. If turning on the device while 'variable_power_on_off' is 'off', it also initializes the warming process."}
                ],
                'adjust_bottle_type': [
                    {'step': 1, 'actions': ['press_bottle_button'], 'variable': 'variable_bottle_type'}
                ],
                'adjust_initial_temp': [
                    {'step': 1, 'actions': ['press_initial_temp_button'], 'variable': 'variable_initial_temp'}
                ],
                'adjust_volume': [
                    {'step': 1, 'actions': ['press_volume_button'], 'variable': 'variable_volume'}
                ],
                'night_light_toggle': [
                    {'step': 1, 'actions': ['press_and_hold_power_button'], 'variable': 'variable_night_light', 'comment': "This action toggles the night light 'variable_night_light' between 'on' and 'off' regardless of the device's power state."}
                ],
                'null': [
                    {'step': 1, 'actions': [], 'missing_variables': []}
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

        if current_feature == "power_toggle_or_start_warming":
            # Toggle power on/off
            if self.variable_power_on_off.get_current_value() == "off":
                self.variable_power_on_off.set_current_value("on")
            else:
                self.variable_power_on_off.set_current_value("off")

    # Action: press_bottle_button
    def press_bottle_button(self):
        # Update feature progress
        self.feature.update_progress("press_bottle_button")
        current_feature = self.feature.current_value[0]

        if current_feature == "adjust_bottle_type":
            # Adjust bottle type to the next value
            self.execute_action_and_set_next("press_bottle_button")

    # Action: press_initial_temp_button
    def press_initial_temp_button(self):
        # Update feature progress
        self.feature.update_progress("press_initial_temp_button")
        current_feature = self.feature.current_value[0]

        if current_feature == "adjust_initial_temp":
            # Adjust initial temperature to the next value
            self.execute_action_and_set_next("press_initial_temp_button")

    # Action: press_volume_button
    def press_volume_button(self):
        # Update feature progress
        self.feature.update_progress("press_volume_button")
        current_feature = self.feature.current_value[0]

        if current_feature == "adjust_volume":
            # Adjust volume to the next value
            self.execute_action_and_set_next("press_volume_button")

    # Action: press_and_hold_power_button
    def press_and_hold_power_button(self, duration=3):
        # Update feature progress
        self.feature.update_progress("press_and_hold_power_button")
        current_feature = self.feature.current_value[0]

        if current_feature == "night_light_toggle" and duration >= 3:
            # Toggle night light on/off
            if self.variable_night_light.get_current_value() == "off":
                self.variable_night_light.set_current_value("on")
            else:
                self.variable_night_light.set_current_value("off")