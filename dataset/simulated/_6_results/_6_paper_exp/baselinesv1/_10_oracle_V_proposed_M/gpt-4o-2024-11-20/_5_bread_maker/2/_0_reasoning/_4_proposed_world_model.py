class Simulator(Appliance):

    def reset(self):
        # Initialize feature and variables
        self.feature = Feature(
            feature_list={
                'set_menu': [{'step': 1, 'actions': ['press_menu_button'], 'variable': 'variable_menu_index'}],
                'adjust_loaf_size': [{'step': 1, 'actions': ['press_loaf_size_button'], 'variable': 'variable_loaf_size'}],
                'adjust_crust_color': [{'step': 1, 'actions': ['press_crust_button'], 'variable': 'variable_crust_color'}],
                'adjust_timer': [{'step': 1, 'actions': ['press_time_up_button', 'press_time_down_button'], 'variable': 'variable_timer_delay', 'comment': 'This feature also covers adjusting extra bake time conditionally for menu 12 if applicable.'}],
                'start_stop': [{'step': 1, 'actions': ['press_start_stop_button'], 'variable': 'variable_start_running', 'comment': "value always set to 'on' if starting, or 'off' if stopping."}],
                'null': [{'step': 1, 'actions': [], 'missing_variables': []}]
            },
            current_value=("empty", 1)
        )
        self.variable_crust_color = variable_crust_color
        self.variable_loaf_size = variable_loaf_size
        self.variable_menu_index = variable_menu_index
        self.variable_timer_delay = variable_timer_delay
        self.variable_menu_setting_12_extra_bake_time = variable_menu_setting_12_extra_bake_time
        self.variable_start_running = variable_start_running

    # Action: press_menu_button
    def press_menu_button(self):
        # Update feature progress
        self.feature.update_progress("press_menu_button")
        current_feature = self.feature.current_value[0]

        if current_feature == "set_menu":
            # Change the menu index to the next value
            self.execute_action_and_set_next("press_menu_button")

    # Action: press_loaf_size_button
    def press_loaf_size_button(self):
        # Update feature progress
        self.feature.update_progress("press_loaf_size_button")
        current_feature = self.feature.current_value[0]

        if current_feature == "adjust_loaf_size":
            # Change the loaf size to the next value
            self.execute_action_and_set_next("press_loaf_size_button")

    # Action: press_crust_button
    def press_crust_button(self):
        # Update feature progress
        self.feature.update_progress("press_crust_button")
        current_feature = self.feature.current_value[0]

        if current_feature == "adjust_crust_color":
            # Change the crust color to the next value
            self.execute_action_and_set_next("press_crust_button")

    # Action: press_time_up_button
    def press_time_up_button(self):
        # Update feature progress
        self.feature.update_progress("press_time_up_button")
        current_feature = self.feature.current_value[0]

        if current_feature == "adjust_timer":
            # Adjust the timer delay or extra bake time upwards
            current_variable = self.get_current_variable("press_time_up_button")
            self.assign_variable_to_next(current_variable)

    # Action: press_time_down_button
    def press_time_down_button(self):
        # Update feature progress
        self.feature.update_progress("press_time_down_button")
        current_feature = self.feature.current_value[0]

        if current_feature == "adjust_timer":
            # Adjust the timer delay or extra bake time downwards
            current_variable = self.get_current_variable("press_time_down_button")
            self.assign_variable_to_prev(current_variable)

    # Action: press_start_stop_button
    def press_start_stop_button(self):
        # Update feature progress
        self.feature.update_progress("press_start_stop_button")
        current_feature = self.feature.current_value[0]

        if current_feature == "start_stop":
            # Toggle the start/stop state
            if self.variable_start_running.get_current_value() == "off":
                self.variable_start_running.set_current_value("on")
            else:
                self.variable_start_running.set_current_value("off")