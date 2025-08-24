class Simulator(Appliance):

    def reset(self):
        # Initialize feature and variables
        self.feature = Feature(
            feature_list={
                "set_menu": [{"step": 1, "actions": ["press_menu_button"], "variable": "variable_menu_index"}],
                "set_crust_color": [{"step": 1, "actions": ["press_color_button"], "variable": "variable_crust_color"}],
                "set_loaf_size": [{"step": 1, "actions": ["press_loaf_button"], "variable": "variable_loaf_size"}],
                "adjust_delay_time": [{"step": 1, "actions": ["press_plus_button", "press_minus_button"], "variable": "variable_delay_time"}],
                "start_or_stop_bread_maker": [{"step": 1, "actions": ["press_start_stop_button"], "variable": "variable_start_running", "comment": "value always toggles between on and off"}],
                "null": [{"step": 1, "actions": ["press_and_hold_start_stop_button"], "missing_variables": []}]
            },
            current_value=("empty", 1)
        )
        self.variable_menu_index = variable_menu_index
        self.variable_crust_color = variable_crust_color
        self.variable_loaf_size = variable_loaf_size
        self.variable_delay_time = variable_delay_time
        self.variable_start_running = variable_start_running

    # Action: press_menu_button
    def press_menu_button(self):
        # Update feature progress and adjust the menu index variable
        self.feature.update_progress("press_menu_button")
        current_feature = self.feature.current_value[0]
        if current_feature == "set_menu":
            self.execute_action_and_set_next("press_menu_button")

    # Action: press_color_button
    def press_color_button(self):
        # Update feature progress and adjust the crust color variable
        self.feature.update_progress("press_color_button")
        current_feature = self.feature.current_value[0]
        if current_feature == "set_crust_color":
            self.execute_action_and_set_next("press_color_button")

    # Action: press_loaf_button
    def press_loaf_button(self):
        # Update feature progress and adjust the loaf size variable
        self.feature.update_progress("press_loaf_button")
        current_feature = self.feature.current_value[0]
        if current_feature == "set_loaf_size":
            self.execute_action_and_set_next("press_loaf_button")

    # Action: press_plus_button
    def press_plus_button(self):
        # Update feature progress and increase the delay time variable
        self.feature.update_progress("press_plus_button")
        current_feature = self.feature.current_value[0]
        if current_feature == "adjust_delay_time":
            self.execute_action_and_set_next("press_plus_button")

    # Action: press_minus_button
    def press_minus_button(self):
        # Update feature progress and decrease the delay time variable
        self.feature.update_progress("press_minus_button")
        current_feature = self.feature.current_value[0]
        if current_feature == "adjust_delay_time":
            self.execute_action_and_set_prev("press_minus_button")

    # Action: press_start_stop_button
    def press_start_stop_button(self):
        # Update feature progress and toggle the start_running variable
        self.feature.update_progress("press_start_stop_button")
        current_feature = self.feature.current_value[0]
        if current_feature == "start_or_stop_bread_maker":
            # Toggle between "on" and "off"
            current_value = self.variable_start_running.get_current_value()
            new_value = "off" if current_value == "on" else "on"
            self.variable_start_running.set_current_value(new_value)