class Simulator(Appliance):

    def reset(self):
        # Initialize feature and variables
        self.feature = Feature(
            feature_list={
                "set_program_menu": [{"step": 1, "actions": ["press_menu_button"], "variable": "variable_menu_index"}],
                "adjust_loaf_size": [{"step": 1, "actions": ["press_loaf_size_button"], "variable": "variable_loaf_size"}],
                "adjust_crust_color": [{"step": 1, "actions": ["press_color_button"], "variable": "variable_crust_color"}],
                "adjust_delay_timer": [{"step": 1, "actions": ["press_time_plus_button", "press_time_minus_button"], "variable": "variable_delay_timer"}],
                "start_stop_appliance": [{"step": 1, "actions": ["press_start_stop_button"], "variable": "variable_start_running", "comment": "value toggles between 'on' and 'off'"}],
                "null": [{"step": 1, "actions": [], "missing_variables": []}]
            },
            current_value=("empty", 1)
        )
        self.variable_menu_index = variable_menu_index
        self.variable_loaf_size = variable_loaf_size
        self.variable_crust_color = variable_crust_color
        self.variable_delay_timer = variable_delay_timer
        self.variable_start_running = variable_start_running

    # Action: press_menu_button
    def press_menu_button(self):
        # Update feature progress and adjust the menu index variable
        self.feature.update_progress("press_menu_button")
        current_feature = self.feature.current_value[0]
        if current_feature == "set_program_menu":
            self.execute_action_and_set_next("press_menu_button")

    # Action: press_loaf_size_button
    def press_loaf_size_button(self):
        # Update feature progress and adjust the loaf size variable
        self.feature.update_progress("press_loaf_size_button")
        current_feature = self.feature.current_value[0]
        if current_feature == "adjust_loaf_size":
            self.execute_action_and_set_next("press_loaf_size_button")

    # Action: press_color_button
    def press_color_button(self):
        # Update feature progress and adjust the crust color variable
        self.feature.update_progress("press_color_button")
        current_feature = self.feature.current_value[0]
        if current_feature == "adjust_crust_color":
            self.execute_action_and_set_next("press_color_button")

    # Action: press_time_plus_button
    def press_time_plus_button(self):
        # Update feature progress and increase the delay timer variable
        self.feature.update_progress("press_time_plus_button")
        current_feature = self.feature.current_value[0]
        if current_feature == "adjust_delay_timer":
            self.execute_action_and_set_next("press_time_plus_button")

    # Action: press_time_minus_button
    def press_time_minus_button(self):
        # Update feature progress and decrease the delay timer variable
        self.feature.update_progress("press_time_minus_button")
        current_feature = self.feature.current_value[0]
        if current_feature == "adjust_delay_timer":
            self.execute_action_and_set_prev("press_time_minus_button")

    # Action: press_start_stop_button
    def press_start_stop_button(self):
        # Update feature progress and toggle the start/stop variable
        self.feature.update_progress("press_start_stop_button")
        current_feature = self.feature.current_value[0]
        if current_feature == "start_stop_appliance":
            self.execute_action_and_set_next("press_start_stop_button")