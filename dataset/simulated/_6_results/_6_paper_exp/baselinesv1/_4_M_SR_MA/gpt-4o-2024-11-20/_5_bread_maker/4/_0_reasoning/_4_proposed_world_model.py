class Simulator(Appliance):

    def reset(self):
        # Initialize features and variables
        self.feature = Feature(
            feature_list={
                "set_auto_menu": [{"step": 1, "actions": ["press_menu_button"], "variable": "variable_menu_index"}],
                "adjust_crust_color": [{"step": 1, "actions": ["press_crust_colour_button"], "variable": "variable_crust_color"}],
                "adjust_loaf_size": [{"step": 1, "actions": ["press_loaf_size_button"], "variable": "variable_loaf_size"}],
                "adjust_timer": [{"step": 1, "actions": ["press_timer_up_button", "press_timer_down_button"], "variable": "variable_timer"}],
                "activate_gluten_free_mode": [{"step": 1, "actions": ["press_gluten_free_button"], "variable": "variable_gluten_free_mode"}],
                "start_or_cancel_program": [{"step": 1, "actions": ["press_start_cancel_button"], "variable": "variable_start_running", "comment": "value always set to on or off"}],
                "hold_to_cancel_keep_warm": [{"step": 1, "actions": ["press_and_hold_start_cancel_button"], "variable": "variable_start_running", "comment": "value always set to off"}],
                "null": [{"step": 1, "actions": [], "missing_variables": []}]
            },
            current_value=("empty", 1)
        )
        self.variable_menu_index = variable_menu_index
        self.variable_menu_setting = variable_menu_setting
        self.variable_menu_setting_basic = variable_menu_setting_basic
        self.variable_menu_setting_french = variable_menu_setting_french
        self.variable_menu_setting_whole_wheat = variable_menu_setting_whole_wheat
        self.variable_menu_setting_sweet = variable_menu_setting_sweet
        self.variable_menu_setting_express_680g = variable_menu_setting_express_680g
        self.variable_menu_setting_express_900g = variable_menu_setting_express_900g
        self.variable_menu_setting_yeast_free = variable_menu_setting_yeast_free
        self.variable_menu_setting_continental = variable_menu_setting_continental
        self.variable_menu_setting_dough = variable_menu_setting_dough
        self.variable_menu_setting_gluten_free = variable_menu_setting_gluten_free
        self.variable_menu_setting_jam = variable_menu_setting_jam
        self.variable_menu_setting_bake = variable_menu_setting_bake
        self.menu_setting_dict = menu_setting_dict
        self.variable_crust_color = variable_crust_color
        self.variable_loaf_size = variable_loaf_size
        self.variable_timer = variable_timer
        self.variable_gluten_free_mode = variable_gluten_free_mode
        self.variable_start_running = variable_start_running

    def press_menu_button(self):
        # Update feature progress and adjust menu index
        self.feature.update_progress("press_menu_button")
        current_feature = self.feature.current_value[0]
        if current_feature == "set_auto_menu":
            # Change menu index to the next value
            self.execute_action_and_set_next("press_menu_button")
            # Update the menu setting variable based on the current menu index
            self.variable_menu_setting = self.menu_setting_dict[str(self.variable_menu_index.get_current_value())]

    def press_crust_colour_button(self):
        # Update feature progress and adjust crust color
        self.feature.update_progress("press_crust_colour_button")
        current_feature = self.feature.current_value[0]
        if current_feature == "adjust_crust_color":
            self.execute_action_and_set_next("press_crust_colour_button")

    def press_loaf_size_button(self):
        # Update feature progress and adjust loaf size
        self.feature.update_progress("press_loaf_size_button")
        current_feature = self.feature.current_value[0]
        if current_feature == "adjust_loaf_size":
            self.execute_action_and_set_next("press_loaf_size_button")

    def press_timer_up_button(self):
        # Update feature progress and increase timer value
        self.feature.update_progress("press_timer_up_button")
        current_feature = self.feature.current_value[0]
        if current_feature == "adjust_timer":
            self.execute_action_and_set_next("press_timer_up_button")

    def press_timer_down_button(self):
        # Update feature progress and decrease timer value
        self.feature.update_progress("press_timer_down_button")
        current_feature = self.feature.current_value[0]
        if current_feature == "adjust_timer":
            self.execute_action_and_set_prev("press_timer_down_button")

    def press_gluten_free_button(self):
        # Update feature progress and activate gluten-free mode
        self.feature.update_progress("press_gluten_free_button")
        current_feature = self.feature.current_value[0]
        if current_feature == "activate_gluten_free_mode":
            self.variable_gluten_free_mode.set_current_value("on")

    def press_start_cancel_button(self):
        # Update feature progress and start or cancel the program
        self.feature.update_progress("press_start_cancel_button")
        current_feature = self.feature.current_value[0]
        if current_feature == "start_or_cancel_program":
            self.variable_start_running.set_current_value("on")

    def press_and_hold_start_cancel_button(self, duration=1):
        # Update feature progress and cancel keep warm if held for 1 second
        self.feature.update_progress("press_and_hold_start_cancel_button")
        current_feature = self.feature.current_value[0]
        if current_feature == "hold_to_cancel_keep_warm" and duration >= 1:
            self.variable_start_running.set_current_value("off")