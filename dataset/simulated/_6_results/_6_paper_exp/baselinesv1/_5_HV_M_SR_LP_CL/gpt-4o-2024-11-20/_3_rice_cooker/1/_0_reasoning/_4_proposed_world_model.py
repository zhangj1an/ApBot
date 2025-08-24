class Simulator(Appliance):

    def reset(self):
        # Initialize feature and variables
        self.feature = Feature(
            feature_list={
                "start_appliance": [
                    {"step": 1, "actions": ["press_start_button"], "variable": "variable_start_running", "comment": "value always set to on"}
                ],
                "adjust_cooking_time": [
                    {"step": 1, "actions": ["press_cooking_time_button"]},
                    {"step": 2, "actions": ["press_hr_button"], "variable": "variable_cooking_time_hr"},
                    {"step": 3, "actions": ["press_min_button"], "variable": "variable_cooking_time_min"}
                ],
                "set_preset_time": [
                    {"step": 1, "actions": ["press_preset_timer_button"]},
                    {"step": 2, "actions": ["press_hr_button"], "variable": "variable_preset_time_hr"},
                    {"step": 3, "actions": ["press_min_button"], "variable": "variable_preset_time_min"}
                ],
                "set_cooking_mode": [
                    {"step": 1, "actions": ["press_menu_button"], "variable": "variable_cooking_mode"}
                ],
                "set_rice_type": [
                    {"step": 1, "actions": ["press_white_button", "press_brown_rice_button"], "variable": "variable_rice_type"}
                ],
                "cancel_or_keep_warm": [
                    {"step": 1, "actions": ["press_keep_warm_cancel_button"], "variable": "variable_keep_warm_cancel"}
                ],
                "null": [
                    {"step": 1, "actions": [], "missing_variables": []}
                ]
            },
            current_value=("empty", 1)
        )
        self.variable_start_running = DiscreteVariable(value_range=["on", "off"], current_value="off")
        self.variable_cooking_mode = DiscreteVariable(
            value_range=[
                "Glutinous rice", 
                "Porridge", 
                "Bean", 
                "Soup", 
                "Steam", 
                "Reheat"
            ],
            current_value="Glutinous rice"
        )
        self.variable_cooking_time_hr = ContinuousVariable(value_ranges_steps=[[0, 59, 1]], current_value=0)
        self.variable_cooking_time_min = ContinuousVariable(value_ranges_steps=[[0, 59, 1]], current_value=0)
        self.variable_preset_time_hr = ContinuousVariable(value_ranges_steps=[[0, 23, 1]], current_value=0)
        self.variable_preset_time_min = ContinuousVariable(value_ranges_steps=[[0, 59, 1]], current_value=0)
        self.variable_keep_warm_cancel = DiscreteVariable(value_range=["keep_warm", "cancel"], current_value="keep_warm")
        self.variable_rice_type = DiscreteVariable(value_range=["white", "brown"], current_value="white")

    # Action: press_start_button
    def press_start_button(self):
        # Always sets variable_start_running to "on"
        self.feature.update_progress("press_start_button")
        self.variable_start_running.set_current_value("on")

    # Action: press_cooking_time_button
    def press_cooking_time_button(self):
        # Progresses to the cooking time adjustment feature
        self.feature.update_progress("press_cooking_time_button")

    # Action: press_hr_button
    def press_hr_button(self):
        # Adjusts the hour for cooking time or preset time
        self.feature.update_progress("press_hr_button")
        current_feature = self.feature.current_value[0]
        if current_feature == "adjust_cooking_time":
            self.execute_action_and_set_next("press_hr_button")
        elif current_feature == "set_preset_time":
            self.execute_action_and_set_next("press_hr_button")

    # Action: press_min_button
    def press_min_button(self):
        # Adjusts the minutes for cooking time or preset time
        self.feature.update_progress("press_min_button")
        current_feature = self.feature.current_value[0]
        if current_feature == "adjust_cooking_time":
            self.execute_action_and_set_next("press_min_button")
        elif current_feature == "set_preset_time":
            self.execute_action_and_set_next("press_min_button")

    # Action: press_preset_timer_button
    def press_preset_timer_button(self):
        # Progresses to the preset time adjustment feature
        self.feature.update_progress("press_preset_timer_button")

    # Action: press_menu_button
    def press_menu_button(self):
        # Adjusts the cooking mode
        self.feature.update_progress("press_menu_button")
        self.execute_action_and_set_next("press_menu_button")

    # Action: press_white_button
    def press_white_button(self):
        # Sets rice type to "white"
        self.feature.update_progress("press_white_button")
        self.variable_rice_type.set_current_value("white")

    # Action: press_brown_rice_button
    def press_brown_rice_button(self):
        # Sets rice type to "brown"
        self.feature.update_progress("press_brown_rice_button")
        self.variable_rice_type.set_current_value("brown")

    # Action: press_keep_warm_cancel_button
    def press_keep_warm_cancel_button(self):
        # Toggles between "keep_warm" and "cancel"
        self.feature.update_progress("press_keep_warm_cancel_button")
        self.execute_action_and_set_next("press_keep_warm_cancel_button")