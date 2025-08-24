class Simulator(Appliance):

    def reset(self):
        # Initialize features and variables
        self.feature = Feature(feature_list={'power_on_off': [{'step': 1, 'actions': ['press_power_button'], 'variable': 'variable_power_on_off'}], 'set_menu_and_adjust_setting': [{'step': 1, 'actions': ['press_menu_button'], 'variable': 'variable_menu_index'}, {'step': 2, 'actions': ['press_plus_button', 'press_minus_button'], 'variable': 'variable_menu_setting'}], 'null': [{'step': 1, 'actions': [], 'missing_variables': []}]}, current_value=("empty", 1))
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

    # Power button action: Toggles power on/off
    def press_power_button(self):
        self.feature.update_progress("press_power_button")
        current_feature = self.feature.current_value[0]
        if current_feature == "power_on_off":
            # Toggle power state
            if self.variable_power_on_off.get_current_value() == "off":
                self.variable_power_on_off.set_current_value("on")
            else:
                self.variable_power_on_off.set_current_value("off")

    # Menu button action: Cycles through menu options and updates the menu setting variable
    def press_menu_button(self):
        self.feature.update_progress("press_menu_button")
        current_feature = self.feature.current_value[0]
        if current_feature == "set_menu_and_adjust_setting":
            # Update menu index to the next value
            self.execute_action_and_set_next("press_menu_button")
            # Update the menu setting variable based on the current menu index
            self.variable_menu_setting = self.menu_setting_dict[self.variable_menu_index.get_current_value()]

    # Plus button action: Increases the value of the current menu setting
    def press_plus_button(self):
        self.feature.update_progress("press_plus_button")
        current_feature = self.feature.current_value[0]
        if current_feature == "set_menu_and_adjust_setting":
            # Increase the value of the current menu setting
            self.execute_action_and_set_next("press_plus_button")

    # Minus button action: Decreases the value of the current menu setting
    def press_minus_button(self):
        self.feature.update_progress("press_minus_button")
        current_feature = self.feature.current_value[0]
        if current_feature == "set_menu_and_adjust_setting":
            # Decrease the value of the current menu setting
            self.execute_action_and_set_prev("press_minus_button")