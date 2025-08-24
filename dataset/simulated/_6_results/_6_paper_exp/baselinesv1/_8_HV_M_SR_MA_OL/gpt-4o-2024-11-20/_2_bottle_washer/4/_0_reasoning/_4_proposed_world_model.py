class Simulator(Appliance):

    def reset(self):
        # Initialize features and variables
        self.feature = Feature(
            feature_list={
                'turn_on_off_appliance': [{'step': 1, 'actions': ['press_power_button'], 'variable': 'variable_power_on_off'}],
                'set_and_adjust_menu': [
                    {'step': 1, 'actions': ['press_menu_button'], 'variable': 'variable_menu_index'},
                    {'step': 2, 'actions': ['press_plus_button', 'press_minus_button'], 'variable': 'variable_menu_setting'}
                ],
                'null': [{'step': 1, 'actions': ['press_and_hold_power_button', 'press_and_hold_minus_button', 'press_and_hold_plus_button', 'press_and_hold_menu_button'], 'missing_variables': []}]
            },
            current_value=("empty", 1)
        )
        self.variable_power_on_off = variable_power_on_off
        self.variable_menu_index = variable_menu_index
        self.variable_menu_setting = variable_menu_setting
        self.variable_menu_setting_quick = variable_menu_setting_quick
        self.variable_menu_setting_slow = variable_menu_setting_slow
        self.variable_menu_setting_defrost = variable_menu_setting_defrost
        self.variable_menu_setting_sterilize = variable_menu_setting_sterilize
        self.variable_menu_setting_steam = variable_menu_setting_steam
        self.variable_menu_setting_preset = variable_menu_setting_preset
        self.menu_setting_dict = menu_setting_dict

    # Action: press_power_button
    def press_power_button(self):
        # Update feature progress
        self.feature.update_progress("press_power_button")
        current_feature = self.feature.current_value[0]
        if current_feature == "turn_on_off_appliance":
            # Toggle power state
            if self.variable_power_on_off.get_current_value() == "off":
                self.variable_power_on_off.set_current_value("on")
            else:
                self.variable_power_on_off.set_current_value("off")

    # Action: press_menu_button
    def press_menu_button(self):
        # Update feature progress
        self.feature.update_progress("press_menu_button")
        current_feature = self.feature.current_value[0]
        if current_feature == "set_and_adjust_menu":
            # Change menu index and update menu setting variable
            self.execute_action_and_set_next("press_menu_button")
            self.variable_menu_setting = self.menu_setting_dict[self.variable_menu_index.get_current_value()]

    # Action: press_plus_button
    def press_plus_button(self):
        # Update feature progress
        self.feature.update_progress("press_plus_button")
        current_feature = self.feature.current_value[0]
        if current_feature == "set_and_adjust_menu":
            # Adjust the current menu setting variable to the next value
            current_variable = self.get_current_variable("press_plus_button")
            self.assign_variable_to_next(current_variable)

    # Action: press_minus_button
    def press_minus_button(self):
        # Update feature progress
        self.feature.update_progress("press_minus_button")
        current_feature = self.feature.current_value[0]
        if current_feature == "set_and_adjust_menu":
            # Adjust the current menu setting variable to the previous value
            current_variable = self.get_current_variable("press_minus_button")
            self.assign_variable_to_prev(current_variable)