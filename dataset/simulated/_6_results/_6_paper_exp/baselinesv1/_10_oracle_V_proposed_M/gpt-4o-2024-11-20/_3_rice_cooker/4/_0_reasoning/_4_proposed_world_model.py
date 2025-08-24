class Simulator(Appliance):

    def reset(self):
        # Initialize feature and variables
        self.feature = Feature(
            feature_list={
                'set_menu': [{'step': 1, 'actions': ['press_menu_button'], 'variable': 'variable_menu_index'}],
                'set_reservation_time': [{'step': 1, 'actions': ['press_delay_button'], 'variable': 'variable_reservation_time'}],
                'start_cooking': [{'step': 1, 'actions': ['press_start_button'], 'variable': 'variable_start_running', 'comment': 'value always set to on'}],
                'cancel_cooking': [{'step': 1, 'actions': ['press_keep_warm_cancel_button'], 'variable': 'variable_start_running', 'comment': 'value always set to off'}],
                'quick_rice_function': [{'step': 1, 'actions': ['press_quick_rice_button'], 'variable': 'variable_menu_index', 'comment': 'value always set to QUICK RICE'}],
                'null': [{'step': 1, 'actions': [], 'missing_variables': []}]
            },
            current_value=("empty", 1)
        )
        self.variable_start_running = DiscreteVariable(value_range=["on", "off"], current_value="off")
        self.variable_reservation_time = ContinuousVariable(value_ranges_steps=[(0, 12, 1)], current_value=0)
        self.variable_menu_index = DiscreteVariable(
            value_range=["QUICK RICE", "WHITE RICE", "BROWN", "PORRIDGE", "MIXED", "STEAM", "SOUP", "STEW"],
            current_value="QUICK RICE"
        )
        self.variable_menu_setting = None
        self.variable_menu_setting_quick_rice = ContinuousVariable(value_ranges_steps=[(0, 30, 1)], current_value=0)
        self.variable_menu_setting_white_rice = ContinuousVariable(value_ranges_steps=[(0, 60, 1)], current_value=0)
        self.variable_menu_setting_brown = ContinuousVariable(value_ranges_steps=[(0, 80, 1)], current_value=0)
        self.variable_menu_setting_porridge = ContinuousVariable(value_ranges_steps=[(0, 90, 1)], current_value=0)
        self.variable_menu_setting_mixed = ContinuousVariable(value_ranges_steps=[(0, 40, 1)], current_value=0)
        self.variable_menu_setting_steam = ContinuousVariable(value_ranges_steps=[(0, 30, 1)], current_value=0)
        self.variable_menu_setting_soup = ContinuousVariable(value_ranges_steps=[(0, 120, 1)], current_value=0)
        self.variable_menu_setting_stew = ContinuousVariable(value_ranges_steps=[(0, 120, 1)], current_value=0)
        self.menu_setting_dict = {
            "QUICK RICE": self.variable_menu_setting_quick_rice,
            "WHITE RICE": self.variable_menu_setting_white_rice,
            "BROWN": self.variable_menu_setting_brown,
            "PORRIDGE": self.variable_menu_setting_porridge,
            "MIXED": self.variable_menu_setting_mixed,
            "STEAM": self.variable_menu_setting_steam,
            "SOUP": self.variable_menu_setting_soup,
            "STEW": self.variable_menu_setting_stew
        }

    def press_menu_button(self):
        # Update feature progress
        self.feature.update_progress("press_menu_button")
        current_feature = self.feature.current_value[0]
        if current_feature == "set_menu":
            # Change the menu index to the next value
            self.execute_action_and_set_next("press_menu_button")
            # Update the menu setting variable based on the current menu index
            self.variable_menu_setting = self.menu_setting_dict[self.variable_menu_index.get_current_value()]

    def press_delay_button(self):
        # Update feature progress
        self.feature.update_progress("press_delay_button")
        current_feature = self.feature.current_value[0]
        if current_feature == "set_reservation_time":
            # Adjust the reservation time variable
            self.execute_action_and_set_next("press_delay_button")

    def press_start_button(self):
        # Update feature progress
        self.feature.update_progress("press_start_button")
        current_feature = self.feature.current_value[0]
        if current_feature == "start_cooking":
            # Set the start_running variable to "on"
            self.variable_start_running.set_current_value("on")

    def press_keep_warm_cancel_button(self):
        # Update feature progress
        self.feature.update_progress("press_keep_warm_cancel_button")
        current_feature = self.feature.current_value[0]
        if current_feature == "cancel_cooking":
            # Set the start_running variable to "off"
            self.variable_start_running.set_current_value("off")

    def press_quick_rice_button(self):
        # Update feature progress
        self.feature.update_progress("press_quick_rice_button")
        current_feature = self.feature.current_value[0]
        if current_feature == "quick_rice_function":
            # Set the menu index to "QUICK RICE"
            self.variable_menu_index.set_current_value("QUICK RICE")
            # Update the menu setting variable to the quick rice setting
            self.variable_menu_setting = self.menu_setting_dict["QUICK RICE"]

    def run_action(self, action_name, execution_times=1, **kwargs):
        # Execute the action
        return super().run_action(action_name, execution_times, **kwargs)