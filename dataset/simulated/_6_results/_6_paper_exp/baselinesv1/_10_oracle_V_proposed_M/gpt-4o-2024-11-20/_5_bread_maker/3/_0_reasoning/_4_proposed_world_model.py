class Simulator(Appliance):

    def reset(self):
        # Initialize feature and variables
        self.feature = simulator_feature
        self.variable_start_running = variable_start_running
        self.variable_cycle = variable_cycle
        self.variable_crust_color = variable_crust_color
        self.variable_loaf_size = variable_loaf_size
        self.variable_delay_timer = variable_delay_timer

    # Action: press_cycle_button
    # Effect: Updates the feature progress and adjusts the cycle variable to the next value.
    def press_cycle_button(self):
        self.feature.update_progress("press_cycle_button")
        current_feature = self.feature.current_value[0]
        if current_feature == "select_cycle":
            self.execute_action_and_set_next("press_cycle_button")

    # Action: press_crust_button
    # Effect: Updates the feature progress and adjusts the crust color variable to the next value.
    def press_crust_button(self):
        self.feature.update_progress("press_crust_button")
        current_feature = self.feature.current_value[0]
        if current_feature == "select_crust_color":
            self.execute_action_and_set_next("press_crust_button")

    # Action: press_loaf_size_button
    # Effect: Updates the feature progress and adjusts the loaf size variable to the next value.
    def press_loaf_size_button(self):
        self.feature.update_progress("press_loaf_size_button")
        current_feature = self.feature.current_value[0]
        if current_feature == "select_loaf_size":
            self.execute_action_and_set_next("press_loaf_size_button")

    # Action: press_delay_timer_plus_button
    # Effect: Updates the feature progress and increases the delay timer variable by one step.
    def press_delay_timer_plus_button(self):
        self.feature.update_progress("press_delay_timer_plus_button")
        current_feature = self.feature.current_value[0]
        if current_feature == "set_delay_timer":
            self.execute_action_and_set_next("press_delay_timer_plus_button")

    # Action: press_delay_timer_minus_button
    # Effect: Updates the feature progress and decreases the delay timer variable by one step.
    def press_delay_timer_minus_button(self):
        self.feature.update_progress("press_delay_timer_minus_button")
        current_feature = self.feature.current_value[0]
        if current_feature == "set_delay_timer":
            self.execute_action_and_set_prev("press_delay_timer_minus_button")

    # Action: press_start_stop_button
    # Effect: Updates the feature progress and sets the start_running variable to "on".
    def press_start_stop_button(self):
        self.feature.update_progress("press_start_stop_button")
        current_feature = self.feature.current_value[0]
        if current_feature == "start_stop_operation":
            self.variable_start_running.set_current_value("on")

    # Action: press_and_hold_start_stop_button
    # Effect: Updates the feature progress and sets the start_running variable to "off".
    def press_and_hold_start_stop_button(self, duration=2):
        self.feature.update_progress("press_and_hold_start_stop_button")
        current_feature = self.feature.current_value[0]
        if current_feature == "cancel_operation" and duration >= 2:
            self.variable_start_running.set_current_value("off")