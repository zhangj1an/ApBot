class Simulator(Appliance):

    def reset(self):
        # Initialize features and variables
        self.feature = Feature(
            feature_list={
                'power_on_off': [{'step': 1, 'actions': ['press_power_button'], 'variable': 'variable_power_on_off'}],
                'adjust_sleep_mode': [{'step': 1, 'actions': ['press_sleep_button'], 'variable': 'variable_sleep_mode'}],
                'mode_selection': [
                    {'step': 1, 'actions': ['press_mode_button'], 'variable': 'variable_mode_selection'},
                    {'step': 2, 'actions': ['press_and_hold_mode_button'], 'variable': 'variable_child_lock'}
                ],
                'adjust_timer': [{'step': 1, 'actions': ['press_timer_button', 'press_and_hold_timer_button'], 'variable': 'variable_timer'}],
                'adjust_humidity': [{'step': 1, 'actions': ['press_humidity_button'], 'variable': 'variable_humidity_level'}],
                'adjust_humidity_unit': [{'step': 1, 'actions': ['press_and_hold_humidity_button_and_timer_button'], 'comment': 'changes between °C and °F'}],
                'internal_drying_process': [{'step': 1, 'actions': ['press_and_hold_drying_button'], 'variable': 'variable_internal_drying'}],
                'adjust_anion_function': [{'step': 1, 'actions': ['press_anion_button'], 'variable': 'variable_anion_function'}],
                'adjust_air_swing': [{'step': 1, 'actions': ['press_swing_button'], 'variable': 'variable_air_swing'}],
                'null': [{'step': 1, 'actions': ['press_drying_button'], 'missing_variables': []}]
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

    # Action: press_power_button
    def press_power_button(self):
        # Update feature progress and set power variable to "on" or "off"
        self.feature.update_progress("press_power_button")
        current_variable = self.get_current_variable("press_power_button")
        if current_variable:
            self.assign_variable_to_next(current_variable)

    # Action: press_sleep_button
    def press_sleep_button(self):
        # Update feature progress and toggle sleep mode
        self.feature.update_progress("press_sleep_button")
        current_variable = self.get_current_variable("press_sleep_button")
        if current_variable:
            self.assign_variable_to_next(current_variable)

    # Action: press_mode_button
    def press_mode_button(self):
        # Update feature progress and cycle through mode selection
        self.feature.update_progress("press_mode_button")
        current_feature = self.feature.current_value[0]
        if current_feature == "mode_selection":
            self.execute_action_and_set_next("press_mode_button")

    # Action: press_and_hold_mode_button
    def press_and_hold_mode_button(self, duration=3):
        # Update feature progress and enable child lock if duration >= 3 seconds
        self.feature.update_progress("press_and_hold_mode_button")
        current_feature = self.feature.current_value[0]
        if current_feature == "mode_selection" and duration >= 3:
            self.variable_child_lock.set_current_value("on")

    # Action: press_timer_button
    def press_timer_button(self):
        # Update feature progress and adjust timer
        self.feature.update_progress("press_timer_button")
        current_variable = self.get_current_variable("press_timer_button")
        if current_variable:
            self.assign_variable_to_next(current_variable)

    # Action: press_and_hold_timer_button
    def press_and_hold_timer_button(self, duration=3):
        # Update feature progress and adjust timer continuously if duration >= 3 seconds
        self.feature.update_progress("press_and_hold_timer_button")
        current_variable = self.get_current_variable("press_and_hold_timer_button")
        if current_variable and duration >= 3:
            self.assign_variable_to_next(current_variable)

    # Action: press_humidity_button
    def press_humidity_button(self):
        # Update feature progress and adjust humidity level
        self.feature.update_progress("press_humidity_button")
        current_variable = self.get_current_variable("press_humidity_button")
        if current_variable:
            self.assign_variable_to_next(current_variable)

    # Action: press_and_hold_humidity_button_and_timer_button
    def press_and_hold_humidity_button_and_timer_button(self, duration=3):
        # Update feature progress and toggle between °C and °F if duration >= 3 seconds
        self.feature.update_progress("press_and_hold_humidity_button_and_timer_button")
        if duration >= 3:
            # This action toggles between °C and °F, but no variable is explicitly defined for this in the given code
            pass

    # Action: press_and_hold_drying_button
    def press_and_hold_drying_button(self, duration=2):
        # Update feature progress and start internal drying process if duration >= 2 seconds
        self.feature.update_progress("press_and_hold_drying_button")
        if duration >= 2:
            self.variable_internal_drying.set_current_value("on")

    # Action: press_anion_button
    def press_anion_button(self):
        # Update feature progress and toggle anion function
        self.feature.update_progress("press_anion_button")
        current_variable = self.get_current_variable("press_anion_button")
        if current_variable:
            self.assign_variable_to_next(current_variable)

    # Action: press_swing_button
    def press_swing_button(self):
        # Update feature progress and toggle air swing function
        self.feature.update_progress("press_swing_button")
        current_variable = self.get_current_variable("press_swing_button")
        if current_variable:
            self.assign_variable_to_next(current_variable)