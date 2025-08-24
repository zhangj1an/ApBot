class Simulator(Appliance):

    def reset(self):
        # Initialize feature and variables
        self.feature = Feature(
            feature_list={
                'power_adjust': [{'step': 1, 'actions': ['press_power_button'], 'variable': 'variable_power_on_off'}],
                'start_pause_cycle': [{'step': 1, 'actions': ['press_start_pause_button'], 'variable': 'variable_start_running'}],
                'child_lock': [{'step': 1, 'actions': ['press_and_hold_temp_button_and_spin_button'], 'variable': 'variable_child_lock'}],
                'adjust_temperature': [{'step': 1, 'actions': ['press_temp_button'], 'variable': 'variable_temperature'}],
                'adjust_spin_speed': [{'step': 1, 'actions': ['press_spin_button'], 'variable': 'variable_spin_speed'}],
                'adjust_options': [{'step': 1, 'actions': ['press_option_button'], 'variable': 'variable_option'}],
                'adjust_cycle_selector': [{'step': 1, 'actions': ['turn_cycle_selector_dial_clockwise', 'turn_cycle_selector_dial_anticlockwise'], 'variable': 'variable_cycle_selector'}],
                'adjust_delay_end': [{'step': 1, 'actions': ['press_delay_end_button'], 'variable': 'variable_delay_end'}],
                'null': [{'step': 1, 'actions': ['press_and_hold_option_button_and_delay_end_button', 'press_and_hold_spin_button_and_option_button'], 'missing_variables': []}]
            },
            current_value=("empty", 1)
        )
        self.variable_power_on_off = DiscreteVariable(value_range=["on", "off"], current_value="off")
        self.variable_start_running = DiscreteVariable(value_range=["on", "off"], current_value="off")
        self.variable_child_lock = DiscreteVariable(value_range=["activated", "deactivated"], current_value="deactivated")
        self.variable_temperature = DiscreteVariable(value_range=["Cold water", "20°C", "30°C", "40°C", "60°C", "95°C"], current_value="Cold water")
        self.variable_spin_speed = DiscreteVariable(value_range=["Rinse Hold", "No spin", "400", "800", "1200", "1400"], current_value="Rinse Hold")
        self.variable_option = DiscreteVariable(value_range=["Soak", "Intensive", "Prewash", "Rinse+", "Soak + Rinse+", "Intensive + Rinse+", "Prewash + Rinse+", "Off"], current_value="Off")
        self.variable_cycle_selector = DiscreteVariable(value_range=["Cotton", "Synthetics", "15' Quick Wash", "Baby Care", "Daily Wash", "Stain Away", "Super Eco Wash", "Outdoor Care", "Wool", "Hand Wash", "Spin", "Rinse + Spin"], current_value="Cotton")
        self.variable_delay_end = ContinuousVariable(value_ranges_steps=[(0, 3, 3), (3, 19, 1)], current_value=0)

    # Action: press_power_button
    def press_power_button(self):
        # Update feature progress and set power variable to "on" or "off"
        self.feature.update_progress("press_power_button")
        current_feature = self.feature.current_value[0]
        if current_feature == "power_adjust":
            if self.variable_power_on_off.get_current_value() == "off":
                self.variable_power_on_off.set_current_value("on")
            else:
                self.variable_power_on_off.set_current_value("off")

    # Action: press_start_pause_button
    def press_start_pause_button(self):
        # Update feature progress and toggle start/pause variable
        self.feature.update_progress("press_start_pause_button")
        current_feature = self.feature.current_value[0]
        if current_feature == "start_pause_cycle":
            if self.variable_start_running.get_current_value() == "off":
                self.variable_start_running.set_current_value("on")
            else:
                self.variable_start_running.set_current_value("off")

    # Action: press_and_hold_temp_button_and_spin_button
    def press_and_hold_temp_button_and_spin_button(self, duration=3):
        # Update feature progress and toggle child lock if duration >= 3 seconds
        self.feature.update_progress("press_and_hold_temp_button_and_spin_button")
        current_feature = self.feature.current_value[0]
        if current_feature == "child_lock" and duration >= 3:
            if self.variable_child_lock.get_current_value() == "deactivated":
                self.variable_child_lock.set_current_value("activated")
            else:
                self.variable_child_lock.set_current_value("deactivated")

    # Action: press_temp_button
    def press_temp_button(self):
        # Update feature progress and cycle through temperature options
        self.feature.update_progress("press_temp_button")
        current_feature = self.feature.current_value[0]
        if current_feature == "adjust_temperature":
            self.execute_action_and_set_next("press_temp_button")

    # Action: press_spin_button
    def press_spin_button(self):
        # Update feature progress and cycle through spin speed options
        self.feature.update_progress("press_spin_button")
        current_feature = self.feature.current_value[0]
        if current_feature == "adjust_spin_speed":
            self.execute_action_and_set_next("press_spin_button")

    # Action: press_option_button
    def press_option_button(self):
        # Update feature progress and cycle through options
        self.feature.update_progress("press_option_button")
        current_feature = self.feature.current_value[0]
        if current_feature == "adjust_options":
            self.execute_action_and_set_next("press_option_button")

    # Action: turn_cycle_selector_dial_clockwise
    def turn_cycle_selector_dial_clockwise(self):
        # Update feature progress and cycle through cycle selector options clockwise
        self.feature.update_progress("turn_cycle_selector_dial_clockwise")
        current_feature = self.feature.current_value[0]
        if current_feature == "adjust_cycle_selector":
            self.execute_action_and_set_next("turn_cycle_selector_dial_clockwise")

    # Action: turn_cycle_selector_dial_anticlockwise
    def turn_cycle_selector_dial_anticlockwise(self):
        # Update feature progress and cycle through cycle selector options anticlockwise
        self.feature.update_progress("turn_cycle_selector_dial_anticlockwise")
        current_feature = self.feature.current_value[0]
        if current_feature == "adjust_cycle_selector":
            self.execute_action_and_set_prev("turn_cycle_selector_dial_anticlockwise")

    # Action: press_delay_end_button
    def press_delay_end_button(self):
        # Update feature progress and cycle through delay end options
        self.feature.update_progress("press_delay_end_button")
        current_feature = self.feature.current_value[0]
        if current_feature == "adjust_delay_end":
            self.execute_action_and_set_next("press_delay_end_button")