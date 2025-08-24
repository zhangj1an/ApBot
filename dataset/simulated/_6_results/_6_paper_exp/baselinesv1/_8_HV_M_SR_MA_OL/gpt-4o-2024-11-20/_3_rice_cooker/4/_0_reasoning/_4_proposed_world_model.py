class Simulator(Appliance):

    def reset(self):
        # Initialize features and variables
        self.feature = Feature(feature_list={
            'set_menu': [{'step': 1, 'actions': ['press_menu_button'], 'variable': 'variable_menu_index'}],
            'set_delay_time': [{'step': 1, 'actions': ['press_delay_button'], 'variable': 'variable_delay_time'}],
            'start_cooking': [{'step': 1, 'actions': ['press_start_button'], 'variable': 'variable_start_running', 'comment': 'value always set to on'}],
            'keep_warm_cancel': [{'step': 1, 'actions': ['press_keep_warm_cancel_button'], 'variable': 'variable_keep_warm'}],
            'quick_rice_function': [{'step': 1, 'actions': ['press_quick_rice_button'], 'variable': 'variable_menu_index', 'comment': 'value always set to quick_rice'}],
            'null': [{'step': 1, 'actions': [], 'missing_variables': []}]
        }, current_value=("empty", 1))

        # Initialize variables
        self.variable_start_running = DiscreteVariable(value_range=["on", "off"], current_value="off")
        self.variable_keep_warm = DiscreteVariable(value_range=["on", "off"], current_value="off")
        self.variable_delay_time = ContinuousVariable(value_ranges_steps=[(0, 12, 1)], current_value=0)
        self.variable_menu_index = DiscreteVariable(value_range=["quick_rice", "white_rice", "brown", "porridge", "grains", "mixed", "steam", "soup", "stew"], current_value="quick_rice")
        self.variable_menu_setting = None
        self.variable_menu_setting_quick_rice = DiscreteVariable(["default"], "default")
        self.variable_menu_setting_white_rice = DiscreteVariable(["default"], "default")
        self.variable_menu_setting_brown = ContinuousVariable(value_ranges_steps=[(0, 2, 0.1)], current_value=0)
        self.variable_menu_setting_porridge = ContinuousVariable(value_ranges_steps=[(0, 2, 0.1)], current_value=0)
        self.variable_menu_setting_grains = ContinuousVariable(value_ranges_steps=[(0, 2, 0.1)], current_value=0)
        self.variable_menu_setting_mixed = ContinuousVariable(value_ranges_steps=[(0, 2, 0.1)], current_value=0)
        self.variable_menu_setting_steam = ContinuousVariable(value_ranges_steps=[(0, 3, 0.1)], current_value=0)
        self.variable_menu_setting_soup = ContinuousVariable(value_ranges_steps=[(0, 3, 0.1)], current_value=0)
        self.variable_menu_setting_stew = ContinuousVariable(value_ranges_steps=[(0, 3, 0.1)], current_value=0)

        # Dictionary mapping menu index to respective settings
        self.menu_setting_dict = {
            "quick_rice": self.variable_menu_setting_quick_rice,
            "white_rice": self.variable_menu_setting_white_rice,
            "brown": self.variable_menu_setting_brown,
            "porridge": self.variable_menu_setting_porridge,
            "grains": self.variable_menu_setting_grains,
            "mixed": self.variable_menu_setting_mixed,
            "steam": self.variable_menu_setting_steam,
            "soup": self.variable_menu_setting_soup,
            "stew": self.variable_menu_setting_stew
        }

    # Action: press_menu_button
    def press_menu_button(self):
        # Update feature progress
        self.feature.update_progress("press_menu_button")
        current_feature = self.feature.current_value[0]

        if current_feature == "set_menu":
            # Change the menu index to the next value
            self.execute_action_and_set_next("press_menu_button")
            # Update the menu setting variable based on the current menu index
            self.variable_menu_setting = self.menu_setting_dict[self.variable_menu_index.get_current_value()]

    # Action: press_delay_button
    def press_delay_button(self):
        # Update feature progress
        self.feature.update_progress("press_delay_button")
        current_feature = self.feature.current_value[0]

        if current_feature == "set_delay_time":
            # Adjust the delay time variable
            self.execute_action_and_set_next("press_delay_button")

    # Action: press_start_button
    def press_start_button(self):
        # Update feature progress
        self.feature.update_progress("press_start_button")
        current_feature = self.feature.current_value[0]

        if current_feature == "start_cooking":
            # Set the start_running variable to "on"
            self.variable_start_running.set_current_value("on")

    # Action: press_keep_warm_cancel_button
    def press_keep_warm_cancel_button(self):
        # Update feature progress
        self.feature.update_progress("press_keep_warm_cancel_button")
        current_feature = self.feature.current_value[0]

        if current_feature == "keep_warm_cancel":
            # Toggle the keep warm variable
            self.execute_action_and_set_next("press_keep_warm_cancel_button")

    # Action: press_quick_rice_button
    def press_quick_rice_button(self):
        # Update feature progress
        self.feature.update_progress("press_quick_rice_button")
        current_feature = self.feature.current_value[0]

        if current_feature == "quick_rice_function":
            # Set the menu index to "quick_rice"
            self.variable_menu_index.set_current_value("quick_rice")
            # Update the menu setting variable to quick_rice settings
            self.variable_menu_setting = self.menu_setting_dict["quick_rice"]

    # Wrapper function for action execution
    def run_action(self, action_name, execution_times=1, **kwargs):
        # Execute the action
        return super().run_action(action_name, execution_times, **kwargs)