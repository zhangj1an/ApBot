class Simulator(Appliance):

    def reset(self):
        # Initialize features and variables
        self.feature = Feature(
            feature_list={
                'power_on_off': [{'step': 1, 'actions': ['press_on_off_button'], 'variable': 'variable_power_on_off'}],
                'adjust_mode': [{'step': 1, 'actions': ['press_mode_button'], 'variable': 'variable_mode'}],
                'adjust_temperature': [{'step': 1, 'actions': ['press_increase_temp_setting_button', 'press_decrease_temp_setting_button'], 'variable': 'variable_temperature_setting'}],
                'adjust_fan_speed': [{'step': 1, 'actions': ['press_speed_uv_button'], 'variable': 'variable_fan_speed'}],
                'adjust_timer_setting': [{'step': 1, 'actions': ['press_timer_button'], 'variable': 'variable_timer_setting'}],
                'null': [{'step': 1, 'actions': [], 'missing_variables': []}]
            },
            current_value=("empty", 1)
        )
        self.variable_power_on_off = DiscreteVariable(value_range=["on", "off"], current_value="off")
        self.variable_mode = DiscreteVariable(value_range=["COOL", "DRY", "FAN", "SMART"], current_value="COOL")
        self.variable_temperature_setting = ContinuousVariable(value_ranges_steps=[(18, 32, 1)], current_value=18)
        self.variable_fan_speed = DiscreteVariable(value_range=["HIGH", "MEDIUM", "LOW", "AUTO"], current_value="HIGH")
        self.variable_timer_setting = ContinuousVariable(value_ranges_steps=[(1, 24, 1)], current_value=1)
        self.variable_sleep_mode = DiscreteVariable(value_range=["on", "off"], current_value="off")

    # Action: press_on_off_button
    def press_on_off_button(self):
        # Update feature progress
        self.feature.update_progress("press_on_off_button")
        # Set the power variable to toggle between "on" and "off"
        current_variable = self.get_current_variable("press_on_off_button")
        self.assign_variable_to_next(current_variable)

    # Action: press_mode_button
    def press_mode_button(self):
        # Update feature progress
        self.feature.update_progress("press_mode_button")
        # Adjust the mode variable to the next value in its range
        current_variable = self.get_current_variable("press_mode_button")
        self.assign_variable_to_next(current_variable)

    # Action: press_increase_temp_setting_button
    def press_increase_temp_setting_button(self):
        # Update feature progress
        self.feature.update_progress("press_increase_temp_setting_button")
        # Adjust the temperature setting variable to the next value in its range
        current_variable = self.get_current_variable("press_increase_temp_setting_button")
        self.assign_variable_to_next(current_variable)

    # Action: press_decrease_temp_setting_button
    def press_decrease_temp_setting_button(self):
        # Update feature progress
        self.feature.update_progress("press_decrease_temp_setting_button")
        # Adjust the temperature setting variable to the previous value in its range
        current_variable = self.get_current_variable("press_decrease_temp_setting_button")
        self.assign_variable_to_prev(current_variable)

    # Action: press_speed_uv_button
    def press_speed_uv_button(self):
        # Update feature progress
        self.feature.update_progress("press_speed_uv_button")
        # Adjust the fan speed variable to the next value in its range
        current_variable = self.get_current_variable("press_speed_uv_button")
        self.assign_variable_to_next(current_variable)

    # Action: press_timer_button
    def press_timer_button(self):
        # Update feature progress
        self.feature.update_progress("press_timer_button")
        # Adjust the timer setting variable to the next value in its range
        current_variable = self.get_current_variable("press_timer_button")
        self.assign_variable_to_next(current_variable)