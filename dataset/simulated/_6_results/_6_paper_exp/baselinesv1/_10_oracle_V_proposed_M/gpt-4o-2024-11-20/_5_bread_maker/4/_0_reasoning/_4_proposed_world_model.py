class Simulator(Appliance):

    def reset(self):
        # Initialize feature and variables
        self.feature = Feature(
            feature_list={
                "set_auto_menu": [{"step": 1, "actions": ["press_menu_button"], "variable": "variable_menu_index"}],
                "set_crust_color": [{"step": 1, "actions": ["press_crust_colour_button"], "variable": "variable_crust_colour"}],
                "set_loaf_size": [{"step": 1, "actions": ["press_loaf_size_button"], "variable": "variable_loaf_size"}],
                "set_gluten_free_mode": [{"step": 1, "actions": ["press_gluten_free_button"], "variable": "variable_gluten_free_mode", "comment": "value always set to on"}],
                "set_timer": [{"step": 1, "actions": ["press_timer_up_button", "press_timer_down_button"], "variable": "variable_timer_setting"}],
                "start_or_cancel": [{"step": 1, "actions": ["press_start_cancel_button"], "variable": "variable_start_running", "comment": "value always set to on"}],
                "null": [{"step": 1, "actions": [], "missing_variables": []}]
            },
            current_value=("empty", 1)
        )
        self.variable_menu_index = variable_menu_index
        self.variable_crust_colour = variable_crust_colour
        self.variable_loaf_size = variable_loaf_size
        self.variable_gluten_free_mode = variable_gluten_free_mode
        self.variable_timer_setting = variable_timer_setting
        self.variable_start_running = variable_start_running

    # Action: press_menu_button
    def press_menu_button(self):
        # Update feature progress and adjust the menu index variable
        self.feature.update_progress("press_menu_button")
        current_variable = self.get_current_variable("press_menu_button")
        self.assign_variable_to_next(current_variable)

    # Action: press_crust_colour_button
    def press_crust_colour_button(self):
        # Update feature progress and adjust the crust color variable
        self.feature.update_progress("press_crust_colour_button")
        current_variable = self.get_current_variable("press_crust_colour_button")
        self.assign_variable_to_next(current_variable)

    # Action: press_loaf_size_button
    def press_loaf_size_button(self):
        # Update feature progress and adjust the loaf size variable
        self.feature.update_progress("press_loaf_size_button")
        current_variable = self.get_current_variable("press_loaf_size_button")
        self.assign_variable_to_next(current_variable)

    # Action: press_gluten_free_button
    def press_gluten_free_button(self):
        # Update feature progress and set gluten-free mode to "on"
        self.feature.update_progress("press_gluten_free_button")
        self.variable_gluten_free_mode.set_current_value("on")

    # Action: press_timer_up_button
    def press_timer_up_button(self):
        # Update feature progress and increase the timer setting
        self.feature.update_progress("press_timer_up_button")
        current_variable = self.get_current_variable("press_timer_up_button")
        self.assign_variable_to_next(current_variable)

    # Action: press_timer_down_button
    def press_timer_down_button(self):
        # Update feature progress and decrease the timer setting
        self.feature.update_progress("press_timer_down_button")
        current_variable = self.get_current_variable("press_timer_down_button")
        self.assign_variable_to_prev(current_variable)

    # Action: press_start_cancel_button
    def press_start_cancel_button(self):
        # Update feature progress and set start_running to "on"
        self.feature.update_progress("press_start_cancel_button")
        self.variable_start_running.set_current_value("on")