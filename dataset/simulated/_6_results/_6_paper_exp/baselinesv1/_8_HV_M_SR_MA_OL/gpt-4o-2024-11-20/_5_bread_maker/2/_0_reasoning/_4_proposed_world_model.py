class Simulator(Appliance):

    def reset(self):
        # Initialize features
        feature_list = {
            "set_menu_and_setting": [
                {"step": 1, "actions": ["press_menu_button"], "variable": "variable_menu_index"}
            ],
            "adjust_crust_color": [
                {"step": 1, "actions": ["press_crust_button"], "variable": "variable_crust_color"}
            ],
            "adjust_loaf_size": [
                {"step": 1, "actions": ["press_loaf_size_button"], "variable": "variable_loaf_size"}
            ],
            "adjust_timer_delay": [
                {"step": 1, "actions": ["press_time_up_button", "press_time_down_button"], "variable": "variable_timer_delay"}
            ],
            "start_stop_operation": [
                {"step": 1, "actions": ["press_start_stop_button"], "variable": "variable_start_running", "comment": "value always set to on or off"}
            ],
            "null": [
                {"step": 1, "actions": ["press_and_hold_start_stop_button"], "missing_variables": []}
            ]
        }
        self.feature = Feature(feature_list=feature_list, current_value=("empty", 1))

        # Initialize variables
        self.variable_menu_index = variable_menu_index
        self.variable_menu_setting = variable_menu_setting
        self.variable_menu_setting_1 = variable_menu_setting_1
        self.variable_menu_setting_2 = variable_menu_setting_2
        self.variable_menu_setting_3 = variable_menu_setting_3
        self.variable_menu_setting_4 = variable_menu_setting_4
        self.variable_menu_setting_5 = variable_menu_setting_5
        self.variable_menu_setting_6 = variable_menu_setting_6
        self.variable_menu_setting_7 = variable_menu_setting_7
        self.variable_menu_setting_8 = variable_menu_setting_8
        self.variable_menu_setting_9 = variable_menu_setting_9
        self.variable_menu_setting_10 = variable_menu_setting_10
        self.variable_menu_setting_11 = variable_menu_setting_11
        self.variable_menu_setting_12 = variable_menu_setting_12
        self.menu_setting_dict = menu_setting_dict
        self.variable_crust_color = variable_crust_color
        self.variable_loaf_size = variable_loaf_size
        self.variable_start_running = variable_start_running
        self.variable_timer_delay = variable_timer_delay

    def press_menu_button(self):
        # Update feature progress
        self.feature.update_progress("press_menu_button")
        current_feature = self.feature.current_value[0]

        if current_feature == "set_menu_and_setting":
            # Change the menu index to the next value
            self.execute_action_and_set_next("press_menu_button")
            # Update the menu setting variable based on the current menu index
            self.variable_menu_setting = self.menu_setting_dict[str(self.variable_menu_index.get_current_value())]

    def press_crust_button(self):
        # Update feature progress
        self.feature.update_progress("press_crust_button")
        current_feature = self.feature.current_value[0]

        if current_feature == "adjust_crust_color":
            # Adjust the crust color to the next value
            self.execute_action_and_set_next("press_crust_button")

    def press_loaf_size_button(self):
        # Update feature progress
        self.feature.update_progress("press_loaf_size_button")
        current_feature = self.feature.current_value[0]

        if current_feature == "adjust_loaf_size":
            # Adjust the loaf size to the next value
            self.execute_action_and_set_next("press_loaf_size_button")

    def press_time_up_button(self):
        # Update feature progress
        self.feature.update_progress("press_time_up_button")
        current_feature = self.feature.current_value[0]

        if current_feature == "adjust_timer_delay":
            # Increase the timer delay
            self.execute_action_and_set_next("press_time_up_button")

    def press_time_down_button(self):
        # Update feature progress
        self.feature.update_progress("press_time_down_button")
        current_feature = self.feature.current_value[0]

        if current_feature == "adjust_timer_delay":
            # Decrease the timer delay
            self.execute_action_and_set_prev("press_time_down_button")

    def press_start_stop_button(self):
        # Update feature progress
        self.feature.update_progress("press_start_stop_button")
        current_feature = self.feature.current_value[0]

        if current_feature == "start_stop_operation":
            # Toggle the start/stop operation
            if self.variable_start_running.get_current_value() == "off":
                self.variable_start_running.set_current_value("on")
            else:
                self.variable_start_running.set_current_value("off")