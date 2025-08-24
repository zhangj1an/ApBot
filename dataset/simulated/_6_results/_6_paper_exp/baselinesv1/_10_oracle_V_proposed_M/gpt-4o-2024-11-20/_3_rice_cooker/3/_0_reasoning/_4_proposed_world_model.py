class Simulator(Appliance):

    def reset(self):
        # Initialize feature and variables
        self.feature = Feature(
            feature_list={
                "set_delay_timer": [
                    {"step": 1, "actions": ["press_delay_timer_button"]},
                    {"step": 2, "actions": ["press_plus_button", "press_minus_button"], "variable": "variable_delay_timer"}
                ],
                "set_menu": [
                    {"step": 1, "actions": ["press_menu_button"], "variable": "variable_menu_index"},
                    {"step": 2, "actions": ["press_plus_button", "press_minus_button"], "variable": "variable_menu_setting"}
                ],
                "start_cooking": [
                    {"step": 1, "actions": ["press_start_button"], "variable": "variable_start_running", "comment": "value always set to on"}
                ],
                "set_keep_warm_or_stop": [
                    {"step": 1, "actions": ["press_keep_warm_stop_button"], "variable": "variable_keep_warm"}
                ],
                "null": [
                    {"step": 1, "actions": [], "missing_variables": []}
                ]
            },
            current_value=("empty", 1)
        )
        self.variable_start_running = DiscreteVariable(value_range=["on", "off"], current_value="off")
        self.variable_menu_index = DiscreteVariable(value_range=["White Rice", "Brown Rice", "Quinoa", "Steel Cut Oats"], current_value="White Rice")
        self.variable_menu_setting = None
        self.variable_menu_setting_white_rice = ContinuousVariable(value_ranges_steps=[[0, 60, 1]], current_value=0)
        self.variable_menu_setting_brown_rice = ContinuousVariable(value_ranges_steps=[[0, 90, 1]], current_value=0)
        self.variable_menu_setting_quinoa = ContinuousVariable(value_ranges_steps=[[0, 40, 1]], current_value=0)
        self.variable_menu_setting_steel_cut_oats = ContinuousVariable(value_ranges_steps=[[0, 40, 1]], current_value=0)
        self.menu_setting_dict = {
            "White Rice": self.variable_menu_setting_white_rice,
            "Brown Rice": self.variable_menu_setting_brown_rice,
            "Quinoa": self.variable_menu_setting_quinoa,
            "Steel Cut Oats": self.variable_menu_setting_steel_cut_oats
        }
        self.variable_delay_timer = ContinuousVariable(value_ranges_steps=[[0, 24, 0.5]], current_value=0)
        self.variable_keep_warm = DiscreteVariable(value_range=["on", "off"], current_value="off")

    def press_start_button(self):
        # Start cooking, set variable_start_running to "on"
        self.feature.update_progress("press_start_button")
        current_feature = self.feature.current_value[0]
        if current_feature == "start_cooking":
            self.variable_start_running.set_current_value("on")

    def press_delay_timer_button(self):
        # Enter delay timer mode
        self.feature.update_progress("press_delay_timer_button")

    def press_keep_warm_stop_button(self):
        # Toggle keep warm or stop cooking
        self.feature.update_progress("press_keep_warm_stop_button")
        current_feature = self.feature.current_value[0]
        if current_feature == "set_keep_warm_or_stop":
            self.execute_action_and_set_next("press_keep_warm_stop_button")

    def press_plus_button(self):
        # Adjust variable values based on the current feature
        self.feature.update_progress("press_plus_button")
        current_feature = self.feature.current_value[0]
        if current_feature == "set_delay_timer":
            self.execute_action_and_set_next("press_plus_button")
        elif current_feature == "set_menu":
            if self.feature.current_value[1] == 1:
                self.execute_action_and_set_next("press_plus_button")
            elif self.feature.current_value[1] == 2:
                self.execute_action_and_set_next("press_plus_button")

    def press_minus_button(self):
        # Adjust variable values based on the current feature
        self.feature.update_progress("press_minus_button")
        current_feature = self.feature.current_value[0]
        if current_feature == "set_delay_timer":
            self.execute_action_and_set_prev("press_minus_button")
        elif current_feature == "set_menu":
            if self.feature.current_value[1] == 1:
                self.execute_action_and_set_prev("press_minus_button")
            elif self.feature.current_value[1] == 2:
                self.execute_action_and_set_prev("press_minus_button")

    def press_menu_button(self):
        # Change menu and update the corresponding menu setting variable
        self.feature.update_progress("press_menu_button")
        current_feature = self.feature.current_value[0]
        if current_feature == "set_menu":
            self.execute_action_and_set_next("press_menu_button")
            # Update the menu setting variable based on the selected menu
            self.variable_menu_setting = self.menu_setting_dict[self.variable_menu_index.get_current_value()]