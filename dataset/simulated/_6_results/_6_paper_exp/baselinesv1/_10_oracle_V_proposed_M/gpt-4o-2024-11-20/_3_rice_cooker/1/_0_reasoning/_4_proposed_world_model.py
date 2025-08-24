class Simulator(Appliance):

    def reset(self):
        # Initialize feature and variables
        self.feature = simulator_feature
        self.variable_menu_index = DiscreteVariable(
            value_range=["Glutinous rice", "Porridge", "Bean", "Soup", "Steam", "Reheat"],
            current_value="Glutinous rice"
        )
        self.variable_preset_timer_hours = ContinuousVariable(
            value_ranges_steps=[(0, 23, 1)], current_value=0
        )
        self.variable_preset_timer_minutes = ContinuousVariable(
            value_ranges_steps=[(0, 59, 1)], current_value=0
        )
        self.variable_cooking_time_hours = ContinuousVariable(
            value_ranges_steps=[(0, 23, 1)], current_value=0
        )
        self.variable_cooking_time_minutes = ContinuousVariable(
            value_ranges_steps=[(0, 59, 1)], current_value=0
        )
        self.variable_cooking_mode = DiscreteVariable(
            value_range=["white", "brown"], current_value="white"
        )
        self.variable_start_cooking = DiscreteVariable(
            value_range=["off", "on"], current_value="off"
        )
        self.variable_cancel_action = DiscreteVariable(
            value_range=["none", "cancel"], current_value="none"
        )

    def press_menu_button(self):
        # Update feature and adjust menu index
        self.feature.update_progress("press_menu_button")
        current_feature = self.feature.current_value[0]
        if current_feature == "select_menu_option":
            self.execute_action_and_set_next("press_menu_button")

    def press_preset_timer_button(self):
        # Update feature for preset timer
        self.feature.update_progress("press_preset_timer_button")

    def press_hr_button(self):
        # Update feature and adjust hour variables
        self.feature.update_progress("press_hr_button")
        current_feature = self.feature.current_value[0]
        if current_feature == "set_preset_timer":
            self.execute_action_and_set_next("press_hr_button")
        elif current_feature == "set_cooking_time":
            self.execute_action_and_set_next("press_hr_button")

    def press_min_button(self):
        # Update feature and adjust minute variables
        self.feature.update_progress("press_min_button")
        current_feature = self.feature.current_value[0]
        if current_feature == "set_preset_timer":
            self.execute_action_and_set_next("press_min_button")
        elif current_feature == "set_cooking_time":
            self.execute_action_and_set_next("press_min_button")

    def press_cooking_time_button(self):
        # Update feature for cooking time
        self.feature.update_progress("press_cooking_time_button")

    def press_white_button(self):
        # Update feature and set cooking mode to white rice
        self.feature.update_progress("press_white_button")
        current_feature = self.feature.current_value[0]
        if current_feature == "select_white_rice_mode":
            self.variable_cooking_mode.set_current_value("white")

    def press_brown_rice_button(self):
        # Update feature and set cooking mode to brown rice
        self.feature.update_progress("press_brown_rice_button")
        current_feature = self.feature.current_value[0]
        if current_feature == "select_brown_rice_mode":
            self.variable_cooking_mode.set_current_value("brown")

    def press_start_button(self):
        # Update feature and set start cooking to on
        self.feature.update_progress("press_start_button")
        current_feature = self.feature.current_value[0]
        if current_feature == "start_cooking":
            self.variable_start_cooking.set_current_value("on")

    def press_keep_warm_cancel_button(self):
        # Update feature and set cancel action to cancel
        self.feature.update_progress("press_keep_warm_cancel_button")
        current_feature = self.feature.current_value[0]
        if current_feature == "cancel_or_reset":
            self.variable_cancel_action.set_current_value("cancel")

    def run_action(self, action_name, execution_times=1, **kwargs):
        # Execute action
        action = getattr(self, action_name, None)
        if callable(action):
            for _ in range(execution_times):
                action(**kwargs)

        # Update display
        self.update_display()
        return self.display