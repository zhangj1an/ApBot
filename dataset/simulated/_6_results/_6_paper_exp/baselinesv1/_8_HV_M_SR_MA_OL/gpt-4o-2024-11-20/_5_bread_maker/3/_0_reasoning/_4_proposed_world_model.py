class Simulator(Appliance):

    def reset(self):
        # Initialize feature and variables
        self.feature = Feature(
            feature_list={
                "select_cycle": [{"step": 1, "actions": ["press_cycle_button"], "variable": "variable_cycle"}],
                "adjust_crust_color": [{"step": 1, "actions": ["press_crust_button"], "variable": "variable_crust_color"}],
                "adjust_loaf_size": [{"step": 1, "actions": ["press_loaf_size_button"], "variable": "variable_loaf_size"}],
                "adjust_delay_timer": [{"step": 1, "actions": ["press_delay_timer_plus_button", "press_delay_timer_minus_button"], "variable": "variable_delay_timer"}],
                "start_or_stop_operation": [{"step": 1, "actions": ["press_start_stop_button"], "variable": "variable_start_running", "comment": "value alternates between on and off"}],
                "cancel_operation": [{"step": 1, "actions": ["press_and_hold_start_stop_button"], "variable": "variable_start_running", "comment": "value set to off"}],
                "null": [{"step": 1, "actions": [], "missing_variables": []}]
            },
            current_value=("empty", 1)
        )
        self.variable_start_running = DiscreteVariable(value_range=["on", "off"], current_value="off")
        self.variable_cycle = DiscreteVariable(
            value_range=["Basic", "French", "Gluten-Free", "Quick", "Sweet", 
                         "1.5lb. Express", "2.0lb. Express", "Dough", "Jam", 
                         "Cake", "Whole Grain", "Bake"], 
            current_value="Basic"
        )
        self.variable_crust_color = DiscreteVariable(
            value_range=["Light", "Medium", "Dark"],
            current_value="Medium"
        )
        self.variable_loaf_size = DiscreteVariable(
            value_range=["1.5lb", "2.0lb"],
            current_value="1.5lb"
        )
        self.variable_delay_timer = ContinuousVariable(
            value_ranges_steps=[(0, 780, 1)],  # Delay timer ranges from 0 minutes to 13 hours (780 minutes) with a step of 1 minute.
            current_value=0
        )

    # Action: press_cycle_button
    # Effect: Updates the feature progress and changes the cycle to the next value in the range.
    def press_cycle_button(self):
        self.feature.update_progress("press_cycle_button")
        self.execute_action_and_set_next("press_cycle_button")

    # Action: press_crust_button
    # Effect: Updates the feature progress and changes the crust color to the next value in the range.
    def press_crust_button(self):
        self.feature.update_progress("press_crust_button")
        self.execute_action_and_set_next("press_crust_button")

    # Action: press_loaf_size_button
    # Effect: Updates the feature progress and changes the loaf size to the next value in the range.
    def press_loaf_size_button(self):
        self.feature.update_progress("press_loaf_size_button")
        self.execute_action_and_set_next("press_loaf_size_button")

    # Action: press_delay_timer_plus_button
    # Effect: Updates the feature progress and increases the delay timer by 1 minute.
    def press_delay_timer_plus_button(self):
        self.feature.update_progress("press_delay_timer_plus_button")
        self.execute_action_and_set_next("press_delay_timer_plus_button")

    # Action: press_delay_timer_minus_button
    # Effect: Updates the feature progress and decreases the delay timer by 1 minute.
    def press_delay_timer_minus_button(self):
        self.feature.update_progress("press_delay_timer_minus_button")
        self.execute_action_and_set_prev("press_delay_timer_minus_button")

    # Action: press_start_stop_button
    # Effect: Toggles the start_running variable between "on" and "off".
    def press_start_stop_button(self):
        self.feature.update_progress("press_start_stop_button")
        if self.variable_start_running.get_current_value() == "off":
            self.variable_start_running.set_current_value("on")
        else:
            self.variable_start_running.set_current_value("off")

    # Action: press_and_hold_start_stop_button
    # Effect: Sets the start_running variable to "off" when held for 2 seconds.
    def press_and_hold_start_stop_button(self, duration=2):
        self.feature.update_progress("press_and_hold_start_stop_button")
        if duration >= 2:
            self.variable_start_running.set_current_value("off")