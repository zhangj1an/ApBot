class Simulator(Appliance):

    def reset(self):
        # Initialize feature and variables
        self.feature = Feature(
            feature_list={
                'power_on_off': [{'step': 1, 'actions': ['press_on_off_button'], 'variable': 'variable_power_on_off'}],
                'set_operating_mode': [{'step': 1, 'actions': ['press_mode_button'], 'variable': 'variable_mode'}],
                'set_temperature': [{'step': 1, 'actions': ['press_decrease_temp_setting_button', 'press_increase_temp_setting_button'], 'variable': 'variable_temperature_setting'}],
                'set_fan_speed': [{'step': 1, 'actions': ['press_speed_uv_button'], 'variable': 'variable_fan_speed'}],
                'set_timer': [{'step': 1, 'actions': ['press_timer_button'], 'variable': 'variable_timer_setting'}],
                'activate_sleep_mode': [{'step': 1, 'actions': ['press_and_hold_mode_button'], 'variable': 'variable_sleep_mode'}],
                'null': [{'step': 1, 'actions': ['press_and_hold_on_off_button', 'press_and_hold_speed_uv_button', 'press_and_hold_decrease_temp_setting_button_and_increase_temp_setting_button', 'press_and_hold_increase_temp_setting_button'], 'missing_variables': []}]
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
        # Toggle power variable between "on" and "off"
        if self.variable_power_on_off.get_current_value() == "off":
            self.variable_power_on_off.set_current_value("on")
        else:
            self.variable_power_on_off.set_current_value("off")

    # Action: press_mode_button
    def press_mode_button(self):
        # Update feature progress
        self.feature.update_progress("press_mode_button")
        # Change the operating mode to the next value
        self.execute_action_and_set_next("press_mode_button")

    # Action: press_decrease_temp_setting_button
    def press_decrease_temp_setting_button(self):
        # Update feature progress
        self.feature.update_progress("press_decrease_temp_setting_button")
        # Decrease the temperature setting
        self.execute_action_and_set_prev("press_decrease_temp_setting_button")

    # Action: press_increase_temp_setting_button
    def press_increase_temp_setting_button(self):
        # Update feature progress
        self.feature.update_progress("press_increase_temp_setting_button")
        # Increase the temperature setting
        self.execute_action_and_set_next("press_increase_temp_setting_button")

    # Action: press_speed_uv_button
    def press_speed_uv_button(self):
        # Update feature progress
        self.feature.update_progress("press_speed_uv_button")
        # Change the fan speed to the next value
        self.execute_action_and_set_next("press_speed_uv_button")

    # Action: press_timer_button
    def press_timer_button(self):
        # Update feature progress
        self.feature.update_progress("press_timer_button")
        # Increase the timer setting
        self.execute_action_and_set_next("press_timer_button")

    # Action: press_and_hold_mode_button
    def press_and_hold_mode_button(self, duration=3):
        # Update feature progress
        self.feature.update_progress("press_and_hold_mode_button")
        # Activate sleep mode if duration is sufficient
        if duration >= 3:
            self.variable_sleep_mode.set_current_value("on")

    # Overriding run_action to include global condition checks
    def run_action(self, action_name, execution_times=1, **kwargs):
        # Execute the action
        return super().run_action(action_name, execution_times, **kwargs)