class Simulator(Appliance):

    def reset(self):
        # Initialize features and variables
        self.feature = Feature(
            feature_list={
                'power_on_off': [{'step': 1, 'actions': ['press_power_button'], 'variable': 'variable_power_on_off'}],
                'sleep_mode': [{'step': 1, 'actions': ['press_sleep_button'], 'variable': 'variable_sleep_mode'}],
                'mode_selection': [{'step': 1, 'actions': ['press_mode_button'], 'variable': 'variable_mode_selection'}],
                'timer_adjustment': [{'step': 1, 'actions': ['press_timer_button'], 'variable': 'variable_timer'}],
                'humidity_level_adjustment': [
                    {'step': 1, 'actions': ['press_humidity_button'], 'variable': 'variable_humidity_level'},
                    {'step': 2, 'actions': ['press_and_hold_humidity_button_and_timer_button'], 'comment': 'Humidity units (°C/°F) toggle using this button combination.'}
                ],
                'internal_drying': [{'step': 1, 'actions': ['press_and_hold_drying_button'], 'variable': 'variable_internal_drying'}],
                'anion_function': [{'step': 1, 'actions': ['press_anion_button'], 'variable': 'variable_anion_function'}],
                'air_swing': [{'step': 1, 'actions': ['press_swing_button'], 'variable': 'variable_air_swing'}],
                'child_lock': [{'step': 1, 'actions': ['press_and_hold_mode_button'], 'variable': 'variable_child_lock'}],
                'null': [{'step': 1, 'actions': [], 'missing_variables': []}]
            },
            current_value=("empty", 1)
        )
        self.variable_power_on_off = DiscreteVariable(value_range=["on", "off"], current_value="off")
        self.variable_sleep_mode = DiscreteVariable(value_range=["on", "off"], current_value="off")
        self.variable_mode_selection = DiscreteVariable(
            value_range=["auto_dehumidification", "continuous_dehumidification", "drying_clothes", "purification", "ventilation"],
            current_value="auto_dehumidification"
        )
        self.variable_timer = ContinuousVariable(value_ranges_steps=[(0, 24, 1)], current_value=0)
        self.variable_humidity_level = ContinuousVariable(value_ranges_steps=[(40, 70, 5)], current_value=40)
        self.variable_internal_drying = DiscreteVariable(value_range=["on", "off"], current_value="off")
        self.variable_anion_function = DiscreteVariable(value_range=["on", "off"], current_value="off")
        self.variable_air_swing = DiscreteVariable(value_range=["on", "off"], current_value="off")
        self.variable_child_lock = DiscreteVariable(value_range=["on", "off"], current_value="off")

    # Action: Press POWER button
    def press_power_button(self):
        # Update feature progress and set power variable to "on" or "off"
        self.feature.update_progress("press_power_button")
        if self.variable_power_on_off.get_current_value() == "off":
            self.variable_power_on_off.set_current_value("on")
        else:
            self.variable_power_on_off.set_current_value("off")

    # Action: Press SLEEP button
    def press_sleep_button(self):
        # Update feature progress and toggle sleep mode
        self.feature.update_progress("press_sleep_button")
        current_variable = self.get_current_variable("press_sleep_button")
        self.assign_variable_to_next(current_variable)

    # Action: Press MODE button
    def press_mode_button(self):
        # Update feature progress and cycle through mode selection
        self.feature.update_progress("press_mode_button")
        current_variable = self.get_current_variable("press_mode_button")
        self.assign_variable_to_next(current_variable)

    # Action: Press and hold MODE button (Child Lock)
    def press_and_hold_mode_button(self, duration=3):
        # Update feature progress and enable child lock if duration >= 3 seconds
        self.feature.update_progress("press_and_hold_mode_button")
        if duration >= 3:
            self.variable_child_lock.set_current_value("on")

    # Action: Press TIMER button
    def press_timer_button(self):
        # Update feature progress and adjust timer
        self.feature.update_progress("press_timer_button")
        current_variable = self.get_current_variable("press_timer_button")
        self.assign_variable_to_next(current_variable)

    # Action: Press HUMIDITY button
    def press_humidity_button(self):
        # Update feature progress and adjust humidity level
        self.feature.update_progress("press_humidity_button")
        current_variable = self.get_current_variable("press_humidity_button")
        self.assign_variable_to_next(current_variable)

    # Action: Press and hold HUMIDITY and TIMER buttons (Toggle °C/°F)
    def press_and_hold_humidity_button_and_timer_button(self, duration=3):
        # Update feature progress and toggle humidity units if duration >= 3 seconds
        self.feature.update_progress("press_and_hold_humidity_button_and_timer_button")
        if duration >= 3:
            # No variable to toggle in this case, but feature progress is updated
            pass

    # Action: Press and hold DRYING button
    def press_and_hold_drying_button(self, duration=2):
        # Update feature progress and enable internal drying if duration >= 2 seconds
        self.feature.update_progress("press_and_hold_drying_button")
        if duration >= 2:
            self.variable_internal_drying.set_current_value("on")

    # Action: Press ANION button
    def press_anion_button(self):
        # Update feature progress and toggle anion function
        self.feature.update_progress("press_anion_button")
        current_variable = self.get_current_variable("press_anion_button")
        self.assign_variable_to_next(current_variable)

    # Action: Press SWING button
    def press_swing_button(self):
        # Update feature progress and toggle air swing
        self.feature.update_progress("press_swing_button")
        current_variable = self.get_current_variable("press_swing_button")
        self.assign_variable_to_next(current_variable)

    # Override run_action to include global condition checks
    def run_action(self, action_name, execution_times=1, **kwargs):
        # Check for child lock
        if self.variable_child_lock.get_current_value() == "on" and action_name not in ["press_power_button", "press_and_hold_mode_button"]:
            self.display = "child lock: locked"
            return self.display

        # Execute the action
        return super().run_action(action_name, execution_times, **kwargs)