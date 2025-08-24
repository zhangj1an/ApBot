class Simulator(Appliance):

    def reset(self):
        # Initialize feature and variables
        self.feature = Feature(
            feature_list={
                'set_menu': [
                    {'step': 1, 'actions': ['press_menu_button'], 'variable': 'variable_menu_index'},
                    {'step': 2, 'actions': ['press_plus_button', 'press_minus_button'], 'variable': 'variable_menu_setting'}
                ],
                'adjust_delay_timer': [
                    {'step': 1, 'actions': ['press_delay_timer_button']},
                    {'step': 2, 'actions': ['press_plus_button', 'press_minus_button'], 'variable': 'variable_delay_timer'}
                ],
                'toggle_keep_warm_mode': [
                    {'step': 1, 'actions': ['press_keep_warm_stop_button'], 'variable': 'variable_keep_warm', 'comment': 'value toggles between on and off depending on mode'}
                ],
                'start_cooking': [
                    {'step': 1, 'actions': ['press_start_button'], 'variable': 'variable_start_running', 'comment': 'value always set to on'}
                ],
                'stop_cooking': [
                    {'step': 1, 'actions': ['press_and_hold_keep_warm_stop_button'], 'variable': 'variable_start_running', 'comment': 'value always set to off'}
                ],
                'null': [{'step': 1, 'actions': [], 'missing_variables': []}]
            },
            current_value=("empty", 1)
        )
        self.variable_start_running = variable_start_running
        self.variable_on_off = variable_on_off
        self.variable_delay_timer = variable_delay_timer
        self.variable_keep_warm = variable_keep_warm
        self.variable_menu_index = variable_menu_index
        self.variable_menu_setting = variable_menu_setting
        self.variable_menu_setting_white_rice = variable_menu_setting_white_rice
        self.variable_menu_setting_brown_rice = variable_menu_setting_brown_rice
        self.variable_menu_setting_quinoa = variable_menu_setting_quinoa
        self.variable_menu_setting_steel_cut_oats = variable_menu_setting_steel_cut_oats
        self.menu_setting_dict = menu_setting_dict

    def press_menu_button(self):
        # Update feature progress
        self.feature.update_progress("press_menu_button")
        current_feature = self.feature.current_value[0]

        if current_feature == "set_menu":
            # Change the menu index to the next value
            self.execute_action_and_set_next("press_menu_button")
            # Update the menu setting variable based on the selected menu
            self.variable_menu_setting = self.menu_setting_dict[self.variable_menu_index.get_current_value()]

    def press_plus_button(self):
        # Update feature progress
        self.feature.update_progress("press_plus_button")
        current_feature = self.feature.current_value[0]

        if current_feature == "set_menu":
            # Adjust the menu setting variable
            self.execute_action_and_set_next("press_plus_button")
        elif current_feature == "adjust_delay_timer":
            # Adjust the delay timer variable
            self.execute_action_and_set_next("press_plus_button")

    def press_minus_button(self):
        # Update feature progress
        self.feature.update_progress("press_minus_button")
        current_feature = self.feature.current_value[0]

        if current_feature == "set_menu":
            # Adjust the menu setting variable
            self.execute_action_and_set_prev("press_minus_button")
        elif current_feature == "adjust_delay_timer":
            # Adjust the delay timer variable
            self.execute_action_and_set_prev("press_minus_button")

    def press_delay_timer_button(self):
        # Update feature progress
        self.feature.update_progress("press_delay_timer_button")
        current_feature = self.feature.current_value[0]

        if current_feature == "adjust_delay_timer":
            # No variable adjustment, just progress the feature
            pass

    def press_keep_warm_stop_button(self):
        # Update feature progress
        self.feature.update_progress("press_keep_warm_stop_button")
        current_feature = self.feature.current_value[0]

        if current_feature == "toggle_keep_warm_mode":
            # Toggle the keep warm mode
            current_value = self.variable_keep_warm.get_current_value()
            new_value = "off" if current_value == "on" else "on"
            self.variable_keep_warm.set_current_value(new_value)

    def press_start_button(self):
        # Update feature progress
        self.feature.update_progress("press_start_button")
        current_feature = self.feature.current_value[0]

        if current_feature == "start_cooking":
            # Set the start running variable to "on"
            self.variable_start_running.set_current_value("on")

    def press_and_hold_keep_warm_stop_button(self, duration=3):
        # Update feature progress
        self.feature.update_progress("press_and_hold_keep_warm_stop_button")
        current_feature = self.feature.current_value[0]

        if current_feature == "stop_cooking" and duration >= 3:
            # Set the start running variable to "off"
            self.variable_start_running.set_current_value("off")